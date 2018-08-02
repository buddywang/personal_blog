from django import forms

class SearchForm(forms.Form):
    search_key = forms.CharField(max_length=20,widget=forms.TextInput(attrs={ 'class': \
    'form-control','type': 'text','placeholder':'搜一搜',}))