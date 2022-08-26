from django import forms


class MassUploadForm(forms.Form):
    all_quotes = forms.CharField(widget=forms.Textarea(
        attrs={'rows': '20', 'cols': '80'}))
