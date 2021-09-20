from django import forms
from .models import KB_Entry, Attachment
from settings.models import KB_Type


class KBForm(forms.ModelForm):
    name = forms.CharField(label='KB Title', widget=forms.TextInput(attrs={'class': 'text'}))
    type = forms.ModelChoiceField(queryset=KB_Type.objects.all(), label='KB Type',
                                  widget=forms.Select(attrs={'class': 'form-control'}))
    notes = forms.CharField(label='Notes', widget=forms.Textarea)

    class Meta:
        model = KB_Entry
        fields = ['name', 'type', 'notes']


class AttachmentForm(forms.ModelForm):

    class Meta:
        model = Attachment
        fields = ['file_name', 'file']
