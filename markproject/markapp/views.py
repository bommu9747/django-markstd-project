from django.shortcuts import render,redirect
from .models import marks
from .models import details


# Create your views here.
#  def mark(request):
#     return render(request,'mark.html')

def std(request):
    data=marks.objects.all()
    print(data)
    return render(request,'mark.html',{'data':data})
def add(request):
    if request.method =='POST':
        name = request.POST['name']
        markstd=request.POST['markstd']
        grade =request.POST['grade']
        task2=marks(name=name,mark2=markstd,garde=grade)
        task2.save()
        data=marks.objects.all()
        print(data)
        return render(request,'mark.html',{'data':data})
    return render(request,'mark.html')

def deta(request):
    data2=details.objects.all()
    print(data2)
    return render(request,'contact.html',{'data2':data2})

def add2(request):
    if request.method == 'POST':
        std=request.POST['student']
        address=request.POST['address']
        phone=request.POST['phone']
        task3=details(std=std,address=address,phone=phone)
        task3.save()
        data2=details.objects.all()
        print(data2)
        return render(request,'contact.html',{'data2':data2})
    return render(request,'contact.html')

def delete(request,dele):
    add=marks.objects.get(id=dele)
    add.delete()
    return redirect('stds')

def edit(request,ed):
    data=marks.objects.get(id=ed)
    print(data)
    return render(request,'edit.html',{'data':data})

def formupdate(request,con):
    if request.method=='POST':
        ADD=marks.objects.get(id=con)
        ADD.name=request.POST['name']
        ADD.mark2=request.POST['markstd']
        ADD.garde=request.POST['grade']
        ADD.save()
    return redirect('stds')



def delete2(request,dell):
    add2=details.objects.get(id=dell)
    add2.delete()
    return redirect('details')
def edit2(request,edd):
    data1=details.objects.get(id=edd)
    print(data1)
    return render(request,'editt2.html',{'data1':data1})

def formupdate2(request,conn):
    if request.method=='POST':
        add3=details.objects.get(id=conn)
        add3.std=request.POST['student']
        add3.address=request.POST['address']
        add3.phone=request.POST['phone']
        add3.save()
    return redirect('details')