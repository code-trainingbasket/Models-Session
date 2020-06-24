from django.shortcuts import render,redirect
from .models import info

# Create your views here.
def home(request):
    if request.method=='POST':
        name=request.POST['name']
        roll = request.POST['roll']
        obj= info.objects.create(name=name,roll=roll)
        obj.save()
        return redirect('home')

    obj = info.objects.all()
    return render(request,'index.html',{'obj':obj})
