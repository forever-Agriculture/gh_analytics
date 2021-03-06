valid_mocked_data = {'repos': 'Rv-029.Go', 'users': 'users', 'from_date': '2013-02-01', 'to_date': '2019-01-01'}
invalid_return_dict = {'repos': 'Rv-029.Go', 'users': 'zzell'}
repos = 'Cycling_admin, Rv-029.Go, Rv-025.Python'
users = 'PhilipUa, zzell, yurapa'

mocked_response = {
  "total_count": 2,
  "items": [
    {
      "id": 117976948,
      "node_id": "MDEwOlJlcG9zaXRvcnkxMTc5NzY5NDg=",
      "name": "Rv-029.Go",
      "full_name": "Social-projects-Rivne/Rv-029.Go",
      "owner": {
        "login": "Social-projects-Rivne",
        "id": 13674166,
        "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNjc0MTY2",
        "avatar_url": "https://avatars3.githubusercontent.com/u/13674166?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/Social-projects-Rivne",
        "html_url": "https://github.com/Social-projects-Rivne",
        "followers_url": "https://api.github.com/users/Social-projects-Rivne/followers",
        "following_url": "https://api.github.com/users/Social-projects-Rivne/following{/other_user}",
        "gists_url": "https://api.github.com/users/Social-projects-Rivne/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/Social-projects-Rivne/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/Social-projects-Rivne/subscriptions",
        "organizations_url": "https://api.github.com/users/Social-projects-Rivne/orgs",
        "repos_url": "https://api.github.com/users/Social-projects-Rivne/repos",
        "events_url": "https://api.github.com/users/Social-projects-Rivne/events{/privacy}",
        "received_events_url": "https://api.github.com/users/Social-projects-Rivne/received_events",
        "type": "Organization"
      },
      "html_url": "https://github.com/Social-projects-Rivne/Rv-029.Go",
      "url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go",
      "forks_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/forks",
      "keys_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/keys{/key_id}",
      "collaborators_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/collaborators{/collaborator}",
      "teams_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/teams",
      "hooks_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/hooks",
      "issue_events_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/issues/events{/number}",
      "events_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/events",
      "assignees_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/assignees{/user}",
      "branches_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/branches{/branch}",
      "tags_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/tags",
      "blobs_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/git/blobs{/sha}",
      "git_tags_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/git/tags{/sha}",
      "git_refs_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/git/refs{/sha}",
      "trees_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/git/trees{/sha}",
      "statuses_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/statuses/{sha}",
      "languages_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/languages",
      "stargazers_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/stargazers",
      "contributors_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/contributors",
      "subscribers_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/subscribers",
      "subscription_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/subscription",
      "commits_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/commits{/sha}",
      "git_commits_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/git/commits{/sha}",
      "comments_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/comments{/number}",
      "issue_comment_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/issues/comments{/number}",
      "contents_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/contents/{+path}",
      "compare_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/compare/{base}...{head}",
      "merges_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/merges",
      "archive_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/{archive_format}{/ref}",
      "downloads_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/downloads",
      "issues_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/issues{/number}",
      "pulls_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/pulls{/number}",
      "milestones_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/milestones{/number}",
      "notifications_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/notifications{?since,all,participating}",
      "labels_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/labels{/name}",
      "releases_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/releases{/id}",
      "deployments_url": "https://api.github.com/repos/Social-projects-Rivne/Rv-029.Go/deployments",
      "created_at": "2018-01-18T11:57:16Z",
      "updated_at": "2018-01-18T11:57:16Z",
      "pushed_at": "2018-04-12T10:50:23Z",
      "git_url": "git://github.com/Social-projects-Rivne/Rv-029.Go.git",
      "ssh_url": "git@github.com:Social-projects-Rivne/Rv-029.Go.git",
      "clone_url": "https://github.com/Social-projects-Rivne/Rv-029.Go.git",
      "svn_url": "https://github.com/Social-projects-Rivne/Rv-029.Go",
      "open_issues_count": 1,
      "license": {
        "key": "gpl-3.0",
        "name": "GNU General Public License v3.0",
        "spdx_id": "GPL-3.0",
        "url": "https://api.github.com/licenses/gpl-3.0",
        "node_id": "MDc6TGljZW5zZTk="
      },
      "forks": 0,
      "open_issues": 1,
      "watchers": 0,
      "default_branch": "master",
      "score": 28.202868
    },
    {
      "id": 118752434,
      "node_id": "MDEwOlJlcG9zaXRvcnkxMTg3NTI0MzQ=",
      "name": "rv029go",
      "full_name": "MSennikov/rv029go",
      "owner": {
        "login": "MSennikov",
        "id": 19395072,
        "node_id": "MDQ6VXNlcjE5Mzk1MDcy",
        "avatar_url": "https://avatars2.githubusercontent.com/u/19395072?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/MSennikov",
        "html_url": "https://github.com/MSennikov",
        "followers_url": "https://api.github.com/users/MSennikov/followers",
        "following_url": "https://api.github.com/users/MSennikov/following{/other_user}",
        "gists_url": "https://api.github.com/users/MSennikov/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/MSennikov/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/MSennikov/subscriptions",
        "organizations_url": "https://api.github.com/users/MSennikov/orgs",
        "repos_url": "https://api.github.com/users/MSennikov/repos",
        "events_url": "https://api.github.com/users/MSennikov/events{/privacy}",
        "received_events_url": "https://api.github.com/users/MSennikov/received_events",
        "type": "User"
      },
      "html_url": "https://github.com/MSennikov/rv029go",
      "description": "Docker env",
      "url": "https://api.github.com/repos/MSennikov/rv029go",
      "forks_url": "https://api.github.com/repos/MSennikov/rv029go/forks",
      "keys_url": "https://api.github.com/repos/MSennikov/rv029go/keys{/key_id}",
      "collaborators_url": "https://api.github.com/repos/MSennikov/rv029go/collaborators{/collaborator}",
      "teams_url": "https://api.github.com/repos/MSennikov/rv029go/teams",
      "hooks_url": "https://api.github.com/repos/MSennikov/rv029go/hooks",
      "issue_events_url": "https://api.github.com/repos/MSennikov/rv029go/issues/events{/number}",
      "events_url": "https://api.github.com/repos/MSennikov/rv029go/events",
      "assignees_url": "https://api.github.com/repos/MSennikov/rv029go/assignees{/user}",
      "branches_url": "https://api.github.com/repos/MSennikov/rv029go/branches{/branch}",
      "tags_url": "https://api.github.com/repos/MSennikov/rv029go/tags",
      "blobs_url": "https://api.github.com/repos/MSennikov/rv029go/git/blobs{/sha}",
      "git_tags_url": "https://api.github.com/repos/MSennikov/rv029go/git/tags{/sha}",
      "git_refs_url": "https://api.github.com/repos/MSennikov/rv029go/git/refs{/sha}",
      "trees_url": "https://api.github.com/repos/MSennikov/rv029go/git/trees{/sha}",
      "statuses_url": "https://api.github.com/repos/MSennikov/rv029go/statuses/{sha}",
      "languages_url": "https://api.github.com/repos/MSennikov/rv029go/languages",
      "stargazers_url": "https://api.github.com/repos/MSennikov/rv029go/stargazers",
      "contributors_url": "https://api.github.com/repos/MSennikov/rv029go/contributors",
      "subscribers_url": "https://api.github.com/repos/MSennikov/rv029go/subscribers",
      "subscription_url": "https://api.github.com/repos/MSennikov/rv029go/subscription",
      "commits_url": "https://api.github.com/repos/MSennikov/rv029go/commits{/sha}",
      "git_commits_url": "https://api.github.com/repos/MSennikov/rv029go/git/commits{/sha}",
      "comments_url": "https://api.github.com/repos/MSennikov/rv029go/comments{/number}",
      "issue_comment_url": "https://api.github.com/repos/MSennikov/rv029go/issues/comments{/number}",
      "contents_url": "https://api.github.com/repos/MSennikov/rv029go/contents/{+path}",
      "compare_url": "https://api.github.com/repos/MSennikov/rv029go/compare/{base}...{head}",
      "merges_url": "https://api.github.com/repos/MSennikov/rv029go/merges",
      "archive_url": "https://api.github.com/repos/MSennikov/rv029go/{archive_format}{/ref}",
      "downloads_url": "https://api.github.com/repos/MSennikov/rv029go/downloads",
      "issues_url": "https://api.github.com/repos/MSennikov/rv029go/issues{/number}",
      "pulls_url": "https://api.github.com/repos/MSennikov/rv029go/pulls{/number}",
      "milestones_url": "https://api.github.com/repos/MSennikov/rv029go/milestones{/number}",
      "notifications_url": "https://api.github.com/repos/MSennikov/rv029go/notifications{?since,all,participating}",
      "labels_url": "https://api.github.com/repos/MSennikov/rv029go/labels{/name}",
      "releases_url": "https://api.github.com/repos/MSennikov/rv029go/releases{/id}",
      "deployments_url": "https://api.github.com/repos/MSennikov/rv029go/deployments",
      "created_at": "2018-01-24T10:52:38Z",
      "updated_at": "2018-01-28T12:19:06Z",
      "pushed_at": "2018-01-23T21:00:39Z",
      "git_url": "git://github.com/MSennikov/rv029go.git",
      "ssh_url": "git@github.com:MSennikov/rv029go.git",
      "clone_url": "https://github.com/MSennikov/rv029go.git",
      "svn_url": "https://github.com/MSennikov/rv029go",
      "size": 6,
      "stargazers_count": 0,
      "watchers_count": 0,
      "language": "Go",
      "forks": 0,
      "open_issues": 0,
      "watchers": 0,
      "default_branch": "master",
      "score": 30.851566
    }
  ]
}
