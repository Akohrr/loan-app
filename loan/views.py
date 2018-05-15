from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse
from .forms import LoanForm
from account.models import Profile

# Create your views here.
def new_loan(request):
    info = dict()
    if request.method == 'POST':
        form = LoanForm(request.user, request.POST)   
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = Profile.objects.get(user=request.user)
            instance.save()
            info['saved_successfully'] = True
        else:
            info['saved_successfully'] = False

    else:
        form = LoanForm(request.user)  

    context = {'form':form}
    info['html'] = render_to_string('includes/form.html', context)
    return JsonResponse(info)      