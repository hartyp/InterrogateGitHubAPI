import re
from github import Github

def getRepoCommits(user):

    if user is None:
        return None

    userRepos = {
        'UserName' : user.get_user().login,
        'Repos' : []
    }

    for repo in user.get_user().get_repos():
        repoCommits = {
            'Name' : repo.name,
            'Commits' : (repo.get_commits().totalCount),
            
        }
        userRepos['Repos'].append(repoCommits)

    return userRepos

if __name__ == '__main__':
    login = input('Enter username and password separated by a space\t')
    username, password = login.split(' ')
    account = Github(username, password)
    print(getRepoCommits(account))