from django.contrib import admin
from .models import Loan
from .forms import LoanForm
# Register your models here.


class LoanAdmin(admin.ModelAdmin):
    form = LoanForm

    def get_form(self, request, **kwargs):
        form = super(LoanAdmin, self).get_form(request, **kwargs)
        form.current_user = request.user
        return form

admin.site.register(Loan, LoanAdmin)
