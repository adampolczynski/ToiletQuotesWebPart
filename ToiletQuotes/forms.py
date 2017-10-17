from django import forms

class ToiletQuotes(forms.Form):
    user=forms.CharField(max_length=20)
    lang=forms.CharField(max_length=5)
    quote=forms.CharField(max_length=300)
    author=forms.CharField(max_length=24)
    category=forms.IntegerField()
    confirmed=forms.IntegerField(required=False)
