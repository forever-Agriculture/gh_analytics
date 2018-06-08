import requests
import json
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from .forms import AnalyticsForm


class HomePageView(TemplateView):
    template_name = "base.html"
    form_class = AnalyticsForm

    def get(self, request, *args, **kwargs):
        super(HomePageView, self).get(self, request, *args, **kwargs)
        form = self.form_class(request.GET)

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        super(HomePageView, self).get(self, request, *args, **kwargs)
        form = self.form_class(request.POST)
        if form.is_valid():
            owner = form.cleaned_data['owner']
            repo = form.cleaned_data['repo']
            users = form.cleaned_data['users']
            from_date = form.cleaned_data['from_date']
            to_date = form.cleaned_data['to_date']

            s = requests.Session()
            params = {'state': 'all', 'sort': 'created',
                      'created': '{from_date}..{to_date}'.format(from_date=from_date, to_date=to_date),
                      'per_page': '100'}
            r = s.get('https://api.github.com/repos/{owner}/{repo}/pulls'.format(owner=owner, repo=repo),
                      params=params)
            r.encoding = 'utf-8'
            data = r.json()
            user_counter, user_set = self.count_users(data, users)

            args = {'form': form, 'owner': owner, 'repo': repo, 'users': users,
                    'from_date': from_date, 'to_date': to_date, 'user_counter': user_counter}

            return render(request, self.template_name, args)

    @staticmethod
    def count_users(data, users):
        count_list = []
        for pull_req in data:
            if pull_req['user']['login'] in users:
                count_list.append(pull_req['user']['login'])
        return len(count_list), set(count_list)
