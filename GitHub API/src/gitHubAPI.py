import re
from github import Github
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 10})

def getRepoCommits(user):
    names = []
    commits = []

    for repo in user.get_user().get_repos():
        names.append(repo.name)
        commits.append(repo.get_commits().totalCount)

    plt.bar(names,commits)
    plt.xticks(fontsize=7)
    plt.legend()
    plt.xlabel('Repo Name')
    plt.ylabel('Number of Commits')

    plt.title('Bar Chart For the\nNumber of Commits to a Given Repository.')

    plt.show()

if __name__ == '__main__':
    login = input('Enter username and password separated by a space\t')
    username, password = login.split(' ')
    account = Github(username, password)
    getRepoCommits(account)

    
    