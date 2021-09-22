from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .models import LinkedTasks, Task, Entry, Attachment
from .forms import LinkedTaskForm, TaskForm, EntryForm, AttachmentForm
from settings.models import LT_Status, LT_Category, T_Status, T_Rank


def linkedtaskIndex(request):
    lk_tasks = LinkedTasks.objects.all()
    return render(request, 'linked_tasks.html', {'lts': lk_tasks})


def linked_task_detail(request, pk):
    lt = LinkedTasks.objects.get(pk=pk)
    context = {
        'lt': lt,
        'ltstatus': LT_Status,
        'ltgategory': LT_Category
    }
    return render(request, 'linkedtask_detail.html', context)


def add_linked_task(request):
    if request.method == 'GET':
        return render(request, 'linked_task_form.html', {'form': LinkedTaskForm})
    elif request.method == 'POST':
        form = LinkedTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('linkedtask:linked_tasks'))


def update_linked_task(request, pk):
    obj = get_object_or_404(LinkedTasks, pk=pk)
    form = LinkedTaskForm(request.POST or None, instance=obj)
    if request.method == 'GET':
        return render(request, 'linked_task_form.html', {'form': form})
    elif request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('linkedtask:linked_task_detail', kwargs={'pk': pk}))


def delete_linked_task(request, pk):
    query = LinkedTasks.objects.get(pk=pk)
    query.delete()
    return redirect(reverse('linkedtask:linked_tasks'))


def taskIndex(request, pk):
    tasks = Task.objects.filter(linked_to__pk=pk)
    obj = get_object_or_404(LinkedTasks, pk=pk)
    return render(request, 'tasks.html', {'tasks': tasks, 'linked_list': obj})


def task_detail(request, pk, id):
    task = Task.objects.get(id=id)
    types = ['To Do', 'Issue', 'Standard', 'Other']
    context ={
        'task': task,
        'linked': LinkedTasks.objects.get(pk=pk),
        'ranks': T_Rank.objects.all(),
        'statuses': T_Status.objects.all(),
        'types': types
    }
    return render(request, 'task_detail.html', context)


# def add_task(request, pk):
#     if request.method == 'GET':
#         return render(request, 'task_form.html', {'form': TaskForm, 'pk': pk})
#     elif request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.linked_to = LinkedTasks.objects.get(pk=pk)
#             post.save()
#             return redirect(reverse('linkedtask:tasks', kwargs={'pk': pk}))


# def add_task(request, pk):
#     lt = get_object_or_404(LinkedTasks, pk=pk)
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             task = form.save(commit=False)
#             task.linked_to = lt
#             task.save()
#             return redirect(reverse('linkedtask:tasks', kwargs={'pk': pk}))
#     else:
#         form = TaskForm()
#     return render(request, 'task_form.html', {'form': form, 'pk': pk})

class NewTask(View):
    def render(self, request, pk):
        return render(request, 'task_form.html', {'form': self.form, 'pk': pk})

    def post(self, request, pk):
        self.form = TaskForm(request.POST)
        if self.form.is_valid():
            task = self.form.save(commit=False)
            task.linked_to__pk = pk
            task.save()
            return redirect(reverse('linkedtask:tasks', kwargs={'pk': pk}))
        return self.render(request, pk)

    def get(self, request, pk):
        self.form = TaskForm()
        return self.render(request, pk)


def update_task(request, pk, id):
    obj = get_object_or_404(Task, id=id)
    form = TaskForm(request.POST or None, instance=obj)
    if request.method == 'GET':
        return render(request, 'task_form.html', {'form': form, 'pk': pk})
    elif request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('linkedtask:task_detail', kwargs={'pk': pk, 'id': id}))


def delete_task(request, pk, id):
    query = Task.objects.get(id=id)
    query.delete()
    return redirect(reverse('linkedtask:tasks', kwargs={'pk': pk}))


def task_notes(request, id):
    notes = Entry.objects.filter(entry_for__pk=id)
    obj = get_object_or_404(Task, id)
    return render(request, 'task_entries.html', {'notes': notes, 'obj': obj})


def entry_detail(request, id, ix):
    entry = Entry.objects.get(id=ix)
    return render(request, 'entry_detail.html', {'id': id, 'entry': entry})


def add_entry(request, id):
    obj = get_object_or_404(Task, id)
    if request.method == 'GET':
        return render(request, 'entry_form.html', {'form': EntryForm, 'obj': obj})
    elif request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(reverse('linkedtask:task_entries', kwargs={'obj': obj}))


def update_entry(request, id, ix):
    obj = get_object_or_404(Entry, id=ix)
    form = EntryForm(request.POST or None, instance=obj)
    if request.method == 'GET':
        return render(request, 'entry_form.html', {"form": form, 'id': id})
    elif request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('linkedtask:entry_detail', kwargs={'id': id, 'ix': ix}))


def delete_entry(request, id, ix):
    query = Entry.objects.get(id=ix)
    query.delete()
    return redirect(reverse('linkedtask:task_entries', kwargs={'id': id}))


def lt_attachments(request, pk):
    attachments = Attachment.objects.filter(attached_to__pk=pk)
    obj = get_object_or_404(LinkedTasks, pk=pk)
    return render(request, 'lt_attachments.html', {'attachments': attachments, 'linked': obj})


def attached_details(request, pk, id):
    attach = Attachment.objects.get(id=id)
    context = {
        'attach': attach,
        'pk': pk
    }
    return render(request, 'ltattached_detail.html', context)


def add_attachment(request, pk):
    if request.method == 'POST':
        form = AttachmentForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.attached_to = LinkedTasks.objects.get(pk=pk)
            post.save()
            return redirect(reverse('linkedtask:lt_attachments', kwargs={'pk': pk}))
    else:
        form = AttachmentForm()
    return render(request, 'ltattach_form.html', {'form': form, 'pk': pk})


def update_attachment(request, pk, id):
    obj = get_object_or_404(Attachment, id=id)
    form = AttachmentForm(request.POST or None, instance=obj)
    if request.method == 'GET':
        return render(request, 'ltattach_form.html', {"form": form, 'pk': pk})
    elif request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.attached_to = LinkedTasks.objects.get(pk=pk)
            post.save()
            return HttpResponseRedirect(reverse('linkedtask:ltattached_detail', kwargs={'id': id, 'pk': pk}))
        else:
            return render(request, 'ltattach_form.html', {'form': form, 'pk': pk})


def delete_attachment(request, pk, id):
    query = Attachment.objects.get(id=id)
    query.delete()
    return redirect(reverse('linkedtask:lt_attachments', kwargs={'pk': pk}))

