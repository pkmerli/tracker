from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Bug, Attachment, Entry
from settings.models import Bug_Category, Bug_Status, Bug_Priority
from .forms import BugForm, AttachmentForm, EntryForm
from django.urls import reverse
from django.views.generic.edit import DeleteView


def bugIndex(request):
    bugs = Bug.objects.all()
    return render(request, 'bugIndex.html', {'bugs': bugs})


def add_issue(request):
    if request.method == "GET":
        return render(request, "bugcreate.html", {"form": BugForm})
    elif request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('issues:issues'))


def bug_detailview(request, pk):
    bug = Bug.objects.get_by_pk(pk)
    context = {
        'bug': bug,
        'statuses': Bug_Status.objects.list(),
        'priorities': Bug_Priority.objects.list(),
        'categories': Bug_Category.objects.list()
    }
    return render(request, 'bug_detail.html', context)


def update_bug(request, pk):
    context = {}
    obj = Bug.objects.get_by_pk(pk)
    form = BugForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponse("/"+pk)
    context['form'] = form
    return render(request, 'bug_update.html', context)


class DeleteBug(DeleteView):
    model = Bug
    success_url = "/"


def get_bug_attachments(request, pk):
    attachments = Attachment.objects.get_by_related_pk(pk)
    obj = Bug.objects.get_by_pk(pk)
    return render(request, 'attachments.html', {'attachments': attachments, 'bug': obj})


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
            post.attached_to = Bug.objects.get(pk=pk)
            post.save()
            return redirect(reverse('issues:bug_attachments', kwargs={'pk': pk}))
    else:
        form = AttachmentForm()
    return render(request, 'attachment_form.html', {"form": form, 'pk': pk})


def update_attachment(request, pk, id):
    obj = get_object_or_404(Attachment, id=id)
    form = AttachmentForm(request.POST or None, instance=obj)
    if request.method == 'GET':
        return render(request, 'attachment_form.html', {"form": form, 'pk': pk})
    elif request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.attached_to = Bug.objects.get(pk=pk)
            post.save()
            return HttpResponseRedirect(reverse('issues:attached_entries', kwargs={'id': id, 'pk': pk}))
        else:
            return render(request, 'attachment_form.html', {"form": form, 'pk': pk})


def delete_attachment(request, pk, id):
    query = Attachment.objects.get(id=id)
    query.delete()
    return redirect(reverse('issues:bug_attachments', kwargs={'pk': pk}))


def bug_notes(request, pk):
    notes = Entry.objects.get_by_related_pk(pk)
    bug = Bug.objects.get_by_pk(pk)
    return render(request, 'bug_entries.html', {'notes': notes, 'bug': bug})


def entry_detail(request, pk, id):
    entry = Entry.objects.get(id=id)
    return render(request, 'bugentry_detail.html', {'pk': pk, 'entry': entry})


def add_entry(request, pk):
    if request.method == 'GET':
        obj = Bug.objects.get(pk=pk)
        return render(request, 'bugentry_form.html', {'form': EntryForm, 'bug': obj})
    elif request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.entry_for = Bug.objects.get(pk=pk)
            post.save()
            return redirect(reverse('issues:bug_entries', kwargs={'pk': pk}))


def update_entry(request, pk, id):
    obj = get_object_or_404(Entry, id=id)
    form = EntryForm(request.POST or None, instance=obj)
    bug = Bug.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'bugentry_form.html', {'form': form, 'bug': bug})
    elif request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('issues:bug_entries', kwargs={'pk': pk}))


def delete_entry(requests, pk, id):
    query = Entry.objects.get(id=id)
    query.delete()
    return redirect(reverse('issues:bug_entries', kwargs={'pk': pk}))
