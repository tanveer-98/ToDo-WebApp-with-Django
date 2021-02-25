from django.shortcuts import render,redirect
from task.models import *
from task.forms import *
# Create your views here.
def index(request):
    task = Task.objects.all()
    form = TaskForm()

    if request.method=='POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            form.save()
        else:
            print('error in form')
        return redirect('index')
    return render(request,'tasks/index.html',{'task':task ,'form':form})


def updateTask(request,pk):

    task = Task.objects.get(id=pk)

    newtaskform= TaskForm(instance=task)

    if request.method=='POST':
        newtaskform = TaskForm(request.POST,instance = task)
        if newtaskform.is_valid():
            newtaskform.save()
        return redirect('index')

    return render(request,'tasks/update_task.html',{'newtaskform':newtaskform})


def deleteTask(request,pk):
    task=Task.objects.get(id=pk)

    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'tasks/delete.html')



    return redirect('index')
