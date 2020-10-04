from django import forms


class SearchLocForm(forms.Form):
    loc_info = forms.CharField(label="City", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Search City'}))
