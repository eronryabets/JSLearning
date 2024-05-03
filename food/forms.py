from django import forms


class PromoDayForm(forms.Form):
    # name = forms.CharField(label='Input your Name', max_length=100)
    # phone = forms.CharField(label='Input your phone', max_length=15)
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Enter username'}))
    phone = forms.CharField(label='Input your phone', max_length=15)
