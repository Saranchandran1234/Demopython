from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import task
from.forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


class Tasklistview(ListView):
    model=task
    template_name='home.html'
    context_object_name = 'tsk1'
class TaskDetailview(DetailView):
    model = task
    template_name='detail.html'
    context_object_name = 'tsk'
class TaskUpdateView(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'tsk'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class TaskDeleteView(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url=reverse_lazy('cbvhome')


# Create your views here.
def sheet(request):
    tsk1 = task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        tsk=task(name=name,priority=priority,date=date)
        tsk.save()
    return render(request, "home.html", {'tsk1': tsk1})
def delete(request,tskid):
    tsk=task.objects.get(id=tskid)
    if request.method=='POST':
        tsk.delete()
        return redirect('/')
    return render(request,'delete.html')


def details(request):

    return render(request,'detail.html')
def update(request,id):
    tsk=task.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=tsk)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'tsk':tsk})