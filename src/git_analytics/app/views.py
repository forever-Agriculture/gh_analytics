import requests
from django.shortcuts import render
from django.views.generic.base import TemplateView
from .forms import AnalyticsForm


class HomePageView(TemplateView):
    """ GH analytics class """
    template_name = "base.html"
    form_class = AnalyticsForm

    def post(self, request, *args, **kwargs):
        """ Getting requested repos, calling count_pr method and then
         returning computed data with a plot """
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
                try:
                    json_repo = repo_resp.json()['items']
                    owner_list = self.get_owner(json_repo)
                    pr_counter = self.count_pr(repo, owner_list, users, from_date, to_date)
                    global_pr_counter += pr_counter
                except KeyError:
                    pass

            args = {'form': form, 'repos': repos, 'users': users,
                    'from_date': from_date, 'to_date': to_date, 'global_pr_counter': global_pr_counter}
        return render(request, self.template_name, args)

    def count_pr(self, repo, owner_list, users, from_date, to_date):
        """ Counting pull requests of users in requested repos """
        pr_counter = 0
        user_list = self.get_users(users)
        for owner in owner_list:
            for user in user_list:
                pr_resp = requests.get('https://api.github.com/search/issues?q=is:pr+author:{user}+user:{owner}+'
                                       'repo:{repo}+created:{from_date}..{to_date}'.format(user=user, repo=repo,
                                                                                           owner=owner,
                                                                                           from_date=from_date,
                                                                                           to_date=to_date))
                pr_resp.encoding = 'utf-8'
                json_pr_resp = pr_resp.json()
                try:
                    pr_counter += json_pr_resp['total_count']
                except KeyError:
                    pass

        return pr_counter

    @staticmethod
    def get_users(users) -> list:
        """ Splitting users and adding into a list """
        user_list = []
        repos = users.split(", ")
        for repo in repos:
            user_list.append(repo)
        return user_list

    @staticmethod
    def get_repos(repos) -> list:
        """ Splitting repos and adding into a list """
        rep_list = []
        repos = repos.split(", ")
        for repo in repos:
            rep_list.append(repo)
        return rep_list

    @staticmethod
    def get_owner(repo) ->list:
        """ Searching for owners and adding them into a list """
        owner_list = []
        for item in repo:
            if item['owner']['login']:
                owner_list.append(item['owner']['login'])
        return owner_list
