from django import forms
from .models import ToDo, Attachment
from settings.models import TD_Status, TD_Priority


class TDForm(forms.ModelForm):
    name = forms.CharField(label='To Do', help_text='Name your Task ToDo',
                           widget=forms.TextInput(attrs={'class': 'text'}))
    priority = forms.ModelChoiceField(queryset=TD_Priority.objects.all(), label='Priority',
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Details', widget=forms.Textarea)
    status = forms.ModelChoiceField(queryset=TD_Status.objects.all(), label='Status',
                                    widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = ToDo
        fields = ['name', 'priority', 'description', 'status', 'active']


class AttachmentForm(forms.ModelForm):

    class Meta:
        model = Attachment
        fields = ['file_name', 'file']
