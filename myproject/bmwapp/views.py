from django.shortcuts import render

# Create your views here.
def bmw_view(request):
    return render(request, 'bmw.html')

def quote_view(request):
    return render(request, 'quotes.html')