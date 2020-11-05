from django import forms


class URLForm(forms.Form):
    url_input = forms.CharField(label="URL", max_length=500, widget=forms.TextInput(attrs={'placeholder': 'URL to Shorten'}))