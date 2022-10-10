import requests


class Repo:

    def __init__(self, raw_data):
        self.owner = raw_data['owner']['login']
        self.name = raw_data['name']
        self.is_fork = 'fork' in raw_data and raw_data['fork']
        self.parent_set = False
        self.url = raw_data['url']

        if self.is_fork and 'parent' in raw_data:
            self.parent_set = True
            self.parent_owner = raw_data['parent']['owner']['login']
            self.parent_data = raw_data['parent']

    def delete(self, access_key):
        return requests.delete(self.url, auth={'username': self.owner, 'token': access_key})

    def get_full_repo(self, access_key=''):
        args = {}
        if len(access_key) > 0:
            auth = {'username': self.owner, 'token': access_key}
            args['auth'] = auth

        return requests.get(self.url, **args).json()

    def load_repo_details(self, access_key=''):
        repo_details = self.get_full_repo(access_key)

        if repo_details['fork'] and 'parent' in repo_details:
            self.parent_set = True
            self.parent_owner = repo_details['parent']['owner']['login']
            self.parent_data = repo_details['parent']

        return repo_details
