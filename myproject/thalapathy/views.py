from django.shortcuts import render
from .forms import thalapathyform

# Create your views here.
def fvtview(request):
    if request.method == 'POST':
        forms = thalapathyform(request.POST)
        if forms.is_valid():
            forms.save()
    else:
        forms = thalapathyform()
    return render(request,'thalapathy.html',{'form':forms})

