from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={
        'name': 'search', 'placeholder': 'Search...', 'class': 'searchfield'}),
        label='')


class FilterForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(
        attrs={'placeholder': 'Arrival Date', 'class': 'filterfield'}),
        label='')
    end_date = forms.DateField(widget=forms.DateInput(
        attrs={'placeholder': 'Departure Date', 'class': 'filterfield'}),
        label='')
    capacity = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': 'Person(s)', 'class': 'filterfield'}), label='')
