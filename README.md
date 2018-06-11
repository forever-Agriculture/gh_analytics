# gh_analytics

_A simple petproject, check a number of pull requests added by users into certain repositories, 
during certain period of time. Using GitHub API._


## test data:

* repo = Cycling_admin, Rv-029.Go, Rv-025.Python
* users = PhilipUa, zzell, mosketrem, yurapa
* from_date = 2017-02-01
* to_date = 2019-01-01

## API examples:

* https://api.github.com/search/repositories?q=Rv-029.Go&order=desc&sort=updated
* https://api.github.com/search/issues?q=is:pr+author:forever-Agriculture+repo:Social-projects-Rivne/rv-027py+created:2017-12-29..2017-12-29