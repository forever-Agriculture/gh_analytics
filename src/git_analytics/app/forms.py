from django import forms


class AnalyticsForm(forms.Form):
    # owner = forms.CharField(label='owner', max_length=30, required=True)
    repo = forms.CharField(label='repo', max_length=30, required=True)
    users = forms.CharField(label='users', max_length=30, required=True)
    from_date = forms.CharField(label='from_date', max_length=10, required=True)
    to_date = forms.CharField(label='to_date', max_length=10, required=True)
