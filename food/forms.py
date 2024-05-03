from django import forms


class PromoDayForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'order__input',
        'placeholder': 'Enter name'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'order__input',
        'placeholder': 'Enter phone'}))
