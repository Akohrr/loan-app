from django import forms
from .models import Loan
from account.models import Profile

class LoanForm(forms.ModelForm):
    installments = forms.CharField(max_length=10, help_text='Amount to be paid monthly in installments')
    amount = forms.CharField(max_length=10, help_text='Amount you desire to borrow')
    

    class Meta:
        model = Loan
        fields = ('amount', 'installments', 'guarantor',)


    def __init__(self, user,*args, **kwargs):
        super(LoanForm, self).__init__(*args, **kwargs)
        self.salary = Profile.objects.get(user=user).salary
        self.pending_loans = Loan.objects.filter(author=Profile.objects.get(user=user), status='pending')
        self.fields['guarantor'].queryset = Profile.objects.exclude(user=user)

    def clean(self):
        data = self.cleaned_data
        data['salary'] = int(self.salary)
        if len(self.pending_loans) > 0:
            raise forms.ValidationError('You can not submit new loan request until previous loan has been approved')
    
        try:
            int(data['amount'])
        except:
            raise forms.ValidationError('Amount should be in numbers only')
        
        if not ok_to_loan('salary', data):
            raise forms.ValidationError('Loan amount must not exceed twice of your savings')
        
        if not ok_to_loan('installments', data):
            raise forms.ValidationError('Monthly installments should not exceed 30% of saving')

        if not ok_to_loan('installments_timeline', data):
            raise forms.ValidationError('Amount must be paid in 6 months or less')

        if int(data['installments']) > int(data['amount']):
            raise forms.ValidationError('Installments can not be greater than amount')
        
        return data
    

def ok_to_loan(choice, data):
    if choice == 'salary' and int(data['amount']) > (2 * data['salary']):
        print('False')
        return False

    if choice == 'installments' and int(data['installments']) > (0.3 * data['salary']):
        return False

    if choice == 'installments_timeline' and (int(data['amount'])/int(data['installments'])) > 6:
        return False

    return True


    