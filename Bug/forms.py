from django import forms
from .models import Bug, Attachment, Entry
from settings.models import Bug_Category, Bug_Status, Bug_Priority


class BugForm(forms.ModelForm):
    name = forms.CharField(label='Summary', help_text='short description')
    priority = forms.ModelChoiceField(queryset=Bug_Priority.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Description', help_text='long description',
                                  widget=forms.Textarea)
    status = forms.ModelChoiceField(queryset=Bug_Status.objects.all(),
                                    widget=forms.Select(attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(queryset=Bug_Category.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Bug
        fields = ['name', 'priority', 'description', 'status', 'category', 'active']


class AttachmentForm(forms.ModelForm):

    class Meta:
        model = Attachment
        fields = ['file_name', 'file']


class EntryForm(forms.ModelForm):
    notes = forms.CharField(label='Notes', widget=forms.Textarea(attrs={'class': 'form-control'}))
    entry_for = forms.ModelChoiceField(queryset=Bug.objects.all(), label='Bug',
                                       widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Entry
        fields = ['notes', 'entry_for']
