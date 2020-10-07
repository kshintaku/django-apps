from django import forms


class SearchLocForm(forms.Form):
    loc_info = forms.CharField(label="City", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Search City'}))


class UnitToggleForm(forms.Form):
    CHOICES = [("metric", "metric"), ("imperial", "imperial"),]
    unit_info = forms.CharField(label="Units", widget=forms.RadioSelect(choices=CHOICES), required=False)