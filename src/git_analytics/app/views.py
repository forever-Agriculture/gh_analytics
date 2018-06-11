import requests
from django.shortcuts import render
from django.views.generic.base import TemplateView
from .forms import AnalyticsForm


class HomePageView(TemplateView):
    """GH analytics class"""
    template_name = "base.html"
    form_class = AnalyticsForm

    def get(self, request, *args, **kwargs):
        super(HomePageView, self).get(self, request, *args, **kwargs)
        form = self.form_class(request.GET)

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        """ getting requested repos, calling count_pr method and then
         returning computed data with a plot"""
        super(HomePageView, self).get(self, request, *args, **kwargs)
        form = self.form_class(request.POST)

        if form.is_valid():
            repos = form.cleaned_data['repos']
            users = form.cleaned_data['users']
            from_date = form.cleaned_data['from_date']
            to_date = form.cleaned_data['to_date']

            rep_list = self.get_repos(repos)
            global_pr_counter = 0

            for repo in rep_list:
                repo_params = {'q': repo, 'repo': repo, 'order': 'desc', 'sort': 'updated'}
                repo_resp = requests.get('https://api.github.com/search/repositories', params=repo_params)
                repo_resp.encoding = 'utf-8'
                json_repo = repo_resp.json()['items']
                owner_list = self.get_owner(json_repo, from_date, to_date)

                user_counter = self.count_pr(repo, owner_list, users, from_date, to_date)
                global_pr_counter += user_counter

            args = {'form': form, 'repos': repos, 'users': users,
                    'from_date': from_date, 'to_date': to_date, 'global_pr_counter': global_pr_counter}
        return render(request, self.template_name, args)

    def count_pr(self, repo, owner_list, users, from_date, to_date):
        """ counting pull requests of users in requested repos """
        global_user_counter = 0
        for owner in owner_list:
            pr_params = {'state': 'all', 'sort': 'created',
                         'created': '{from_date}..{to_date}'.format(from_date=from_date, to_date=to_date),
                         'per_page': '100'}

            pr_resp = requests.get('https://api.github.com/repos/{owner}/{repo}/pulls'.format(owner=owner, repo=repo),
                                   params=pr_params)
            pr_resp.encoding = 'utf-8'
            json_pr_resp = pr_resp.json()
            user_counter = self.count_users(json_pr_resp, users)
            global_user_counter += user_counter
        return global_user_counter

    @staticmethod
    def get_repos(repos):
        """ splitting repos and adding into a list"""
        rep_list = []
        repos = repos.split(", ")
        for repo in repos:
            rep_list.append(repo)
        return rep_list

    @staticmethod
    def get_owner(repo, from_data, to_date):
        """searching for owners and adding them into a list"""
        owner_list = []
        for item in repo:
            if item['owner']['login']:
                if item['created_at'] >= from_data and item['created_at'] <= to_date:
                    owner_list.append(item['owner']['login'])
        return owner_list

    @staticmethod
    def count_users(json_pr_resp, users):
        """ count created pull requests of required users """
        count_list = []
        for pull_req in json_pr_resp:
            try:
                if pull_req['user']['login'] in users:
                    count_list.append(pull_req['user']['login'])
            except TypeError:
                pass
        return len(count_list)
