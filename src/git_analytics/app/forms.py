from django import forms


class AnalyticsForm(forms.Form):
    """Forms"""
    repos = forms.CharField(label='repos', required=True, min_length=2, max_length=50)
    users = forms.CharField(label='users', required=True, min_length=2, max_length=50)
    from_date = forms.CharField(label='from_date', required=True, min_length=10, max_length=10)
    to_date = forms.CharField(label='to_date', required=True, min_length=10, max_length=10)
