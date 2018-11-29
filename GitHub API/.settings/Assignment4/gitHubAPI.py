import re
from github import Github

def getRepoCommits(user):

    if user is None:
        return None

    userDetails = {
        'UserName' : user.get_user().login,
        'Name' : user.get_user().name,
        'Repos' : []
    }

    for repo in user.get_user().get_repos():
        repoCommits = {
            'Name' : repo.name,
            'Commits' : list(repo.get_commits()),
            
        }
        userDetails['Repos'].append(repoDetails)

    return userDetails

    if __name__ == '__main__':
    #Create github account using personal access token
    login = input('Enter: <userName> <password>\t')
    uName, passW = login.split(' ')
    g = Github(uName, passW)
    print(getRepoDetails(g))