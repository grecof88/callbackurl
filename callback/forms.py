from django import forms


class LogForm(forms.Form):
    api_url = forms.CharField(label='URL', max_length=300)
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=32, widget=forms.PasswordInput)
