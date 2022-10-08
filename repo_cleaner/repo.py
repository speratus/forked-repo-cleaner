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
