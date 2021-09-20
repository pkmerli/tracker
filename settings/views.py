from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView
from .models import Bug_Priority, Bug_Status, Bug_Category, TD_Priority, TD_Status, \
    T_Rank, T_Status, LT_Status, LT_Category, KB_Type
from .forms import BugStatusForm, BugCategoryForm, BugPriorityForm, StatusForm, PriorityForm, \
    TRankForm, LTStatusForm, LTCategoryForm, TStatusForm, KBTypeForm


class SettingsView(TemplateView):
    template_name = 'settingsIndex.html'


def bugstatus_list(request):
    items = Bug_Status.objects.all()
    context = {
        'itemset': 'bstatus',
        'items': items
    }
    return render(request, 'setting_list.html', context)


def bugpriority_list(request):
    items = Bug_Priority.objects.all()
    context = {
        'itemset': 'bpriority',
        'items': items
    }
    return render(request, 'setting_list.html', context)


def bugcategory_list(request):
    items = Bug_Category.objects.all()
    context = {
        'itemset': 'bcategory',
        'items': items
    }
    return render(request, 'setting_list.html', context)


def bugstatus_detail(request, pk):
    status = Bug_Status.objects.get(pk=pk)
    context = {
        'item': status,
        'set': 'bstatus'
    }

    return render(request, 'setting_detail.html', context)


def update_bugstatus(request, pk):
    obj = get_object_or_404(Bug_Status, pk=pk)
    form = BugStatusForm(request.POST or None, instance=obj)
    if request.method == "GET":
        return render(request, 'setting_form.html', {"form": form})
    elif request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('settings:bstatus_detail', kwargs={'pk': pk}))


def bugpriority_detail(request, pk):
    priority = Bug_Priority.objects.get(pk=pk)
    context = {
        'item': priority,
        'set': 'bpriority'
    }
    return render(request, 'setting_detail.html', context)


def update_bugpriority(request, pk):
    obj = get_object_or_404(Bug_Priority, pk=pk)
    form = BugPriorityForm(request.POST or None, instance=obj)
    if request.method == "GET":
        return render(request, 'setting_form.html', {"form": form})
    elif request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('settings:bpriority_detail', kwargs={'pk': pk}))


def category_bugdetail(request, pk):
    category = Bug_Category.objects.get(pk=pk)
    context = {
        'item': category,
        'set': 'bcategory'
    }
    return render(request, 'setting_detail.html', context)


def update_bugcategory(request, pk):
    obj = get_object_or_404(Bug_Category, pk=pk)
    form = BugCategoryForm(request.POST or None, instance=obj)
    if request.method == 'GET':
        return render(request, 'setting_form.html', {"form": form})
    elif request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('settings:bcategory_detail', kwargs={'pk': pk}))


def add_bugstatus(request):
    if request.method == "GET":
        return render(request, "setting_form.html", {"form": BugStatusForm})

    elif request.method == 'POST':
        form = BugStatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('settings:bug_status'))


def add_bugpriority(request):
    if request.method == 'GET':
        return render(request, "setting_form.html", {"form": BugPriorityForm})
    elif request.method == 'POST':
        form = BugPriorityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('settings:bug_priority'))


def add_bugcategory(request):
    if request.method == 'GET':
        return render(request, "setting_form.html", {"form": BugCategoryForm})
    elif request.method == 'POST':
        form = BugCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('settings:bug_category'))


def delete_bugstatus(request, pk):
    query = Bug_Status.objects.get(pk=pk)
    query.delete()
    return redirect(reverse('settings:bug_status'))


def delete_bugpriority(request, pk):
    query = Bug_Priority.objects.get(pk=pk)
    query.delete()
    return redirect(reverse('settings:bug_priority'))


def delete_bugcategory(request, pk):
    query = Bug_Category.objects.get(pk=pk)
    query.delete()
    return redirect(reverse('settings:bug_category'))


def td_priority_list(request):
    items = TD_Priority.objects.all()
    context = {
        'itemset': 'tdpriority',
        'items': items
    }
    return render(request, 'setting_list.html', context)


def td_status_list(request):
    items = TD_Status.objects.all()
    context = {
        'itemset': 'tdstatus',
        'items': items
    }
    return render(request, 'setting_list.html', context)


def td_priority_detail(request, pk):
    priority = TD_Priority.objects.get(pk=pk)
    context = {
        'item': priority,
        'set': 'tdpriority'
    }
    return render(request, 'setting_detail.html', context)


def td_status_detail(request, pk):
    status = TD_Status.objects.get(pk=pk)
    context = {
        'item': status,
        'set': 'tdstatus'
    }
    return render(request, 'setting_detail.html', context)


def add_td_priority(request):
    if request.method == "GET":
        return render(request, "setting_form.html", {"form": PriorityForm})
    elif request.method == 'POST':
        form = PriorityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('settings:td_priority'))


def add_td_status(request):
    if request.method == "GET":
        return render(request, "setting_form.html", {"form": StatusForm})
    elif request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('settings:td_status'))


def update_td_status(request, pk):
    obj = get_object_or_404(TD_Status, pk=pk)
    form = StatusForm(request.POST or None, instance=obj)
    if request.method == 'GET':
        return render(request, 'setting_form.html', {"form": form})
    elif request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('settings:tdstatus_detail', kwargs={'pk': pk}))


def update_td_priority(request, pk):
    obj = get_object_or_404(TD_Priority, pk=pk)
    form = PriorityForm(request.POST or None, instance=obj)
    if request.method == 'GET':
        return render(request, 'setting_form.html', {"form": form})
    elif request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('settings:td_priority_detail', kwargs={'pk': pk}))


def delete_td_status(request, pk):
    query = TD_Status.objects.get(pk=pk)
    query.delete()
    return redirect(reverse('settings:td_status'))


def delete_td_priority(request, pk):
    query = TD_Priority.objects.get(pk=pk)
    query.delete()
    return redirect(reverse('settings:td_priority'))


def lt_status_list(request):
    items = LT_Status.objects.all()
    context = {
        'itemset': 'ltstatus',
        'items': items
    }
    return render(request, 'setting_list.html', context)


def lt_status_detail(request, pk):
    status = LT_Status.objects.get(pk=pk)
    context = {
        'item': status,
        'set': 'ltstatus'
    }
    return render(request, 'setting_detail.html', context)


def add_lt_status(request):
    if request.method == "GET":
        return render(request, "setting_form.html", {"form": LTStatusForm})
    elif request.method == 'POST':
        form = LTStatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('settings:lt_status'))


def update_lt_status(request, pk):
    obj = get_object_or_404(LT_Status, pk=pk)
    form = LTStatusForm(request.POST or None, instance=obj)
    if request.method == 'GET':
        return render(request, 'setting_form.html', {"form": form})
    elif request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('settings:ltstatus_detail', kwargs={'pk': pk}))


def delete_lt_status(request, pk):
    query = LT_Status.objects.get(pk=pk)
    query.delete()
    return redirect(reverse('settings:lt_status'))


def lt_category_list(request):
    items = LT_Category.objects.all()
    context = {
        'itemset': 'ltcategory',
        'items': items
    }
    return render(request, 'setting_list.html', context)


def lt_category_detail(request, pk):
    category = LT_Category.objects.get(pk=pk)
    context = {
        'item': category,
        'set': 'ltcategory'
    }
    return render(request, 'setting_detail.html', context)


def add_lt_category(request):
    if request.method == "GET":
        return render(request, "setting_form.html", {"form": LTCategoryForm})
    elif request.method == 'POST':
        form = LTCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('settings:lt_category'))


def update_lt_category(request, pk):
    obj = get_object_or_404(LT_Category, pk=pk)
    form = LTCategoryForm(request.POST or None, instance=obj)
    if request.method == 'GET':
        return render(request, 'setting_form.html', {"form": form})
    elif request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('settings:ltcategory_detail', kwargs={'pk': pk}))


def delete_lt_category(request, pk):
    query = LT_Category.objects.get(pk=pk)
    query.delete()
    return redirect(reverse('settings:lt_category'))


def t_status_list(request):
    items = T_Status.objects.all()
    context = {
        'itemset': 'tstatus',
        'items': items
    }
    return render(request, 'setting_list.html', context)


def t_status_detail(request, pk):
    status = T_Status.objects.get(pk=pk)
    context = {
        'item': status,
        'set': 'tstatus'
    }
    return render(request, 'setting_detail.html', context)


def add_tstatus(request):
    if request.method == "GET":
        return render(request, "setting_form.html", {"form": TStatusForm})
    elif request.method == 'POST':
        form = TStatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('settings:t_status'))


def update_tstatus(request, pk):
    obj = get_object_or_404(T_Status, pk=pk)
    form = TStatusForm(request.POST or None, instance=obj)
    if request.method == 'GET':
        return render(request, 'setting_form.html', {"form": form})
    elif request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('settings:t_status_detail', kwargs={'pk': pk}))


def delete_tstatus(request, pk):
    query = T_Status.objects.get(pk=pk)
    query.delete()
    return redirect(reverse('settings:t_status'))


def t_rank_list(request):
    items = T_Rank.objects.all()
    context = {
        'itemset': 'trank',
        'items': items
    }
    return render(request, 'setting_list.html', context)


def t_rank_detail(request, pk):
    rank = T_Rank.objects.get(pk=pk)
    context = {
        'item': rank,
        'set': 'trank'
    }
    return render(request, 'setting_detail.html', context)


def add_trank(request):
    if request.method == "GET":
        return render(request, "setting_form.html", {"form": TRankForm})
    elif request.method == 'POST':
        form = TRankForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('settings:t_rank'))


def update_trank(request, pk):
    obj = get_object_or_404(T_Rank, pk=pk)
    form = TRankForm(request.POST or None, instance=obj)
    if request.method == 'GET':
        return render(request, 'setting_form.html', {"form": form})
    elif request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('settings:t_tank_detail', kwargs={'pk': pk}))


def delete_trank(request, pk):
    query = T_Rank.objects.get(pk=pk)
    query.delete()
    return redirect(reverse('settings:t_status'))


def kb_type_list(request):
    items = KB_Type.objects.all()
    context = {
        'itemset': 'kbtype',
        'items': items
    }
    return render(request, 'setting_list.html', context)


def kb_type_detail(request, pk):
    type = KB_Type.objects.get(pk=pk)
    context = {
        'item': type,
        'set': 'kbtype'
    }
    return render(request, 'setting_detail.html', context)


def add_kbtype(request):
    if request.method == "GET":
        return render(request, "setting_form.html", {"form": KBTypeForm})
    elif request.method == 'POST':
        form = KBTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('settings:kb_type'))


def update_kbtype(request, pk):
    obj = get_object_or_404(KB_Type, pk=pk)
    form = KBTypeForm(request.POST or None, instance=obj)
    if request.method == 'GET':
        return render(request, 'setting_form.html', {"form": form})
    elif request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('settings:kb_type_detail', kwargs={'pk': pk}))


def delete_kbtype(request, pk):
    query = KB_Type.objects.get(pk=pk)
    query.delete()
    return redirect(reverse('settings:kb_type'))
