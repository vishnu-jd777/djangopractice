from django.shortcuts import render, get_object_or_404, redirect
from . models import fvrtmodel
from . forms import fvrtform

# Create your views here.

def fvrtlist(request):
    fvrtmodelobj = fvrtmodel.objects.all()

    return render(request,'fvrt/fvrtlist.html',{'fvrtobj': fvrtmodelobj })

def fvrtcreate(request):
    if request.method == "POST":
        frm = fvrtform(request.POST,request.FILES)
        if frm.is_valid():
            frm.save()
            return redirect('fvrtpair')
    else:
        frm = fvrtform()
    return render(request,'fvrt/create.html',{'form': frm})

def fvrtedit(request,pk):
    model=get_object_or_404(fvrtmodel,pk=pk)
    if request.method == 'POST':
        frm = fvrtform(request.POST,request.FILES,instance=model)
        if frm.is_valid():
            frm.save()
            return redirect('fvrtpair')
    else:
        frm = fvrtform(instance=model)
    return render(request,'fvrt/create.html',{'form': frm})

def fvrtdelete(request,pk):
    model=get_object_or_404(fvrtmodel,pk=pk)
    model.delete()
    return redirect('fvrtpair')
