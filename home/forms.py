from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(
        attrs={'name': 'search', 'placeholder': 'Search...'}), label='')


class FilterForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(
        attrs={'placeholder': 'Arrival Date'}), label='')
    end_date = forms.DateField(widget=forms.DateInput(
        attrs={'placeholder': 'Departure Date'}), label='')
    capacity = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': 'Person(s)'}), label='')
