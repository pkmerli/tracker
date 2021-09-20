from django import forms
from .models import Bug_Category, Bug_Status, Bug_Priority, TD_Priority, TD_Status, \
    LT_Category, LT_Status, T_Status, T_Rank, KB_Type


class BugPriorityForm(forms.ModelForm):
    class Meta:
        model = Bug_Priority
        fields = ['priority', 'sort_order']


class BugStatusForm(forms.ModelForm):
    class Meta:
        model = Bug_Status
        fields = ['status', 'sort_order']


class BugCategoryForm(forms.ModelForm):
    class Meta:
        model = Bug_Category
        fields = ['category']


class PriorityForm(forms.ModelForm):
    priority = forms.CharField(label='Priority', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sort_order = forms.IntegerField(label='Sort Order', widget=forms.NumberInput)

    class Meta:
        model = TD_Priority
        fields = ['priority', 'sort_order']


class StatusForm(forms.ModelForm):
    status = forms.CharField(label='Status', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sort_order = forms.IntegerField(label='Sort Order', widget=forms.NumberInput)

    class Meta:
        model = TD_Status
        fields = ['status', 'sort_order']


class LTCategoryForm(forms.ModelForm):
    class Meta:
        model = LT_Category
        fields = ['category']


class LTStatusForm(forms.ModelForm):
    status = forms.CharField(label='Status', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sort_order = forms.IntegerField(label='Sort Order', widget=forms.NumberInput)

    class Meta:
        model = LT_Status
        fields = ['status', 'sort_order']


class TStatusForm(forms.ModelForm):
    status = forms.CharField(label='Status', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sort_order = forms.IntegerField(label='Sort Order', widget=forms.NumberInput)

    class Meta:
        model = T_Status
        fields = ['status', 'sort_order']


class TRankForm(forms.ModelForm):
    rank = forms.CharField(label='Rank', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sort_order = forms.IntegerField(label='Sort Order', widget=forms.NumberInput)

    class Meta:
        model = T_Rank
        fields = ['rank', 'sort_order']


class KBTypeForm(forms.ModelForm):
    type = forms.CharField(label='Type', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = KB_Type
        fields = ['type']


