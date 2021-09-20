from django.shortcuts import render, redirect, get_object_or_404
from .models import ToDo, Attachment
from .forms import TDForm, AttachmentForm
from settings.models import TD_Priority, TD_Status
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import DeleteView


def TD_index(request):
    todos = ToDo.objects.all()
    return render(request, 'ToDo_Index.html', {'todos': todos})


def add_todo(request):
    if request.method == 'GET':
        return render(request, 'todo_form.html', {'form': TDForm})
    elif request.method == 'POST':
        form = TDForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('todos:todo'))


def td_detail(request, pk):
    td = ToDo.objects.get(pk=pk)
    context = {
        'td': td,
        'priorities': TD_Priority.objects.all(),
        'statuses': TD_Status.objects.all()
    }
    return render(request, 'todo_detail.html', context)


def td_update(request, pk):
    obj = get_object_or_404(ToDo, pk=pk)
    form = TDForm(request.POST or None, instance=obj)
    if request.method == 'GET':
        return render(request, 'todo_form.html', {"form": form})
    elif request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('todos:todo_detail', kwargs={'pk': pk}))


class DeleteToDo(DeleteView):
    model = ToDo
    success_url = "/"


def get_task_attachments(request, pk):
    attachments = Attachment.objects.filter(attached_to__pk=pk)
    obj = get_object_or_404(ToDo, pk=pk)
    return render(request, 'task_attachments.html', {'attachments': attachments, 'todo': obj})


def attached_details(request, pk, id):
    entry = Attachment.objects.get(id=id)
    context = {
        'entry': entry,
        'pk': pk
    }
    return render(request, 'attached_detail.html', context)


def add_attachment(request, pk):
    if request.method == 'POST':
        form = AttachmentForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.attached_to = ToDo.objects.get(pk=pk)
            post.save()
            return redirect(reverse('todos:tasks_attachments', kwargs={'pk': pk}))
    else:
        form = AttachmentForm()
    return render(request, 'attach_form.html', {"form": form, 'pk': pk})


def update_attachment(request, pk, id):
    obj = get_object_or_404(Attachment, id=id)
    form = AttachmentForm(request.POST or None, instance=obj)
    if request.method == 'GET':
        return render(request, 'attach_form.html', {"form": form, 'pk': pk})
    elif request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.attached_to = ToDo.objects.get(pk=pk)
            post.save()
            return HttpResponseRedirect(reverse('todos:attached_detail', kwargs={'id': id, 'pk': pk}))
        else:
            return render(request, 'attach_form.html', {"form": form, 'pk': pk})


def delete_attachment(request, pk, id):
    query = Attachment.objects.get(id=id)
    query.delete()
    return redirect(reverse('todos:task_attachments', kwargs={'pk': pk}))
