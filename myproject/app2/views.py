from django.shortcuts import render
from . models import bmwlist
from .form import bmwform

# Create your views here.

def hello(request):
   
    movies = bmwlist.objects.all()
    return render(request, 'hello.html', {'movies': movies})

def hi(request):
    
    if request.method == 'POST':
        form = bmwform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = bmwform()
        
    return render(request, 'hi.html',{'form': form})