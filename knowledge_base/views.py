from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import KB_Entry, Attachment
from .forms import KBForm, AttachmentForm
from settings.models import KB_Type


def kb_index(request):
    kbs = KB_Entry.objects.all()
    return render(request, 'kb_entries.html', {'kbs': kbs})


def kb_detail(request, pk):
    kb = KB_Entry.objects.get(pk=pk)
    context = {
        'kb': kb,
        'kb_type': KB_Type.objects.all()
    }
    return render(request, 'kb_detail.html', context)


def add_kb(request):
    if request.method == 'GET':
        return render(request, 'kb_form.html', {'form': KBForm})
    elif request.method == 'POST':
        form = KBForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('knowledgebase:kb_entries'))


def update_kb(request, pk):
    obj = get_object_or_404(KB_Entry, pk=pk)
    form = KBForm(request.POST or None, instance=obj)
    if request.method == 'GET':
        return render(request, 'kb_form.html', {"form": form})
    elif request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('knowledgebase:kb_detail', kwargs={'pk': pk}))


def delete_kb(request, pk):
    query = KB_Entry.objects.get(pk=pk)
    query.delete()
    return redirect(reverse('knowledgebase:kb_entries'))


def kb_attachments(request, pk):
    attachments = Attachment.objects.filter(attached_to__pk=pk)
    obj = get_object_or_404(KB_Entry, pk=pk)
    return render(request, 'kb_attachments.html', {'attachments': attachments, 'kb': obj})


def attached_details(request, pk, id):
    attach = Attachment.objects.get(id=id)
    context = {
        'attach': attach,
        'pk': pk
    }
    return render(request, 'kbattached_detail.html', context)


def add_attachment(request, pk):
    if request.method == 'POST':
        form = AttachmentForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.attached_to = KB_Entry.objects.get(pk=pk)
            post.save()
            return redirect(reverse('knowledgebase:kb_attachments', kwargs={'pk': pk}))
    else:
        form = AttachmentForm()
    return render(request, 'kbattach_form.html', {'form': form, 'pk': pk})


def update_attachment(request, pk, id):
    obj = get_object_or_404(Attachment, id=id)
    form = AttachmentForm(request.POST or None, instance=obj)
    if request.method == 'GET':
        return render(request, 'kbattach_form.html', {"form": form, 'pk': pk})
    elif request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.attached_to = KB_Entry.objects(pk=pk)
            post.save()
            return HttpResponseRedirect(reverse('knowledgebase:attached_detail', kwargs={'id': id, 'pk': pk}))
        else:
            return render(request, 'attach_form.html', {"form": form, 'pk': pk})


def delete_attachment(request, pk, id):
    query = Attachment.objects.get(id=id)
    query.delete()
    return redirect(reverse('knowledgebase:kb_attachments', kwargs={'pk': pk}))
