import re
from github import Github
import csv
'''
## input into a csv

with open('commits.csv', mode='w') as csv_file:
    fieldnames = ['Repo', 'Commits']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for repo in g.get_user().get_repos():
        print(repo.get_commits().totalCount)
        writer.writerow({'Repo': repo.name , 'Commits': repo.get_commits().totalCount})
'''
def repoCommitsToCSV(user):

    if user is None:
        return None

    with open('data.csv', mode='w') as csv_file:
        fieldnames = ['Name', 'Commits']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for repo in user.get_user().get_repos():
            repoCommits = {
                'Name' : repo.name,
                'Commits' : (repo.get_commits().totalCount),
            
            }
            writer.writerow(repoCommits)
    

if __name__ == '__main__':
    login = input('Enter username and password separated by a space\t')
    username, password = login.split(' ')
    account = Github(username, password)
    repoCommitsToCSV(account)
    
    