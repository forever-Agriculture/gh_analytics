from django import forms


class AnalyticsForm(forms.Form):
    """ Forms """
    repos = forms.CharField(label='repos', required=True, min_length=3, max_length=50)
    users = forms.CharField(label='users', required=True, min_length=3, max_length=50)
    from_date = forms.CharField(label='from_date', required=True)
    to_date = forms.CharField(label='to_date', required=True)
