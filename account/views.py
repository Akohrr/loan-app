from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile
from loan.models import Loan
# Create your views here.

@login_required
def dashboard(request):
    loans = Loan.objects.filter(author=Profile.objects.get(user=request.user))
    context = {'loans':loans}
    return render(request, 'dashboard.html', context=context)
