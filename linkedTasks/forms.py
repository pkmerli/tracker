from django import forms
from .models import LinkedTasks, Entry, Attachment, Task
from settings.models import LT_Status, LT_Category, T_Status, T_Rank


class LinkedTaskForm(forms.ModelForm):
    title = forms.CharField(label='Task List', help_text='Name your Task ToDo',
                            widget=forms.TextInput(attrs={'class': 'text'}))
    summary = forms.CharField(label='Details', widget=forms.Textarea)
    category = forms.ModelChoiceField(queryset=LT_Category.objects.all(), label='Category',
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    status = forms.ModelChoiceField(queryset=LT_Status.objects.all(), label='Status',
                                    widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = LinkedTasks
        fields = ['title', 'summary', 'category', 'status', 'active']


TYPES_CHOICE = (
    ("1", "To Do"),
    ("2", "Issue"),
    ("3", "Standard"),
    ("4", "Other")
)


class TaskForm(forms.ModelForm):
    name = forms.CharField(label='Task', widget=forms.TextInput(attrs={'class': 'form-control'}))
    linked_to = forms.ModelChoiceField(queryset=LinkedTasks.objects.all(), label='Linked Task List',
                                       widget=forms.Select(attrs={'class': 'form-control'}))
    type = forms.ChoiceField(choices=TYPES_CHOICE, label='Task Type',
                             widget=forms.Select(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Details', widget=forms.Textarea)
    rank = forms.ModelChoiceField(queryset=T_Rank.objects.all(), label='Task Rank',
                                  widget=forms.Select(attrs={'class': 'form-control'}))
    status = forms.ModelChoiceField(queryset=T_Status.objects.all(), label='Task Rank',
                                    widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Task
        fields = ['name', 'linked_to', 'type', 'description', 'rank', 'status', 'active']


class EntryForm(forms.ModelForm):
    notes = forms.CharField(label='Details', widget=forms.Textarea)
    entry_on = forms.ModelChoiceField(queryset=Task.objects.all(), label='Task',
                                      widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Entry
        fields = ['notes', 'entry_on']


class AttachmentForm(forms.ModelForm):

    class Meta:
        model = Attachment
        fields = ['file_name', 'file']


