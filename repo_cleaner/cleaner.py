import requests
import time
import random

from .urls import UrlBuilder
from .repo import Repo


class ArgumentException(Exception):
    pass


class Cleaner:

    def __init__(self, args, access_key='', do_random_sleep=True, max_sleep_time=2):
        self.access_key = access_key
        self.args = args[1:]
        self.url_builder = UrlBuilder()
        self.do_random_sleep = do_random_sleep
        self.max_sleep_time = max_sleep_time
        self.forked_repo_owner = None

        if len(self.args) < 1:
            raise ArgumentException("This class requires at least one argument!")
        else:
            self.owner_name = args[0]
            if len(self.args) == 2:
                self.forked_repo_owner = args[1]

    def auth(self):
        auth = {}

        if self.access_key != '':
            auth['username'] = self.owner_name
            auth['token'] = self.access_key

        return auth

    def raw_list_repos(self):
        list_url = self.url_builder.list_repos(self.owner_name)

        return requests.get(list_url, auth=self.auth()).json()

    def list_repos(self):
        raw_data = self.raw_list_repos()

        return [Repo(r) for r in raw_data]

    @staticmethod
    def forked_repos(repo_list):
        def filter_func(r: Repo):
            return r.is_fork

        return filter(filter_func, repo_list)

    def forked_from_stored_owner(self, repos):
        if self.forked_repo_owner is None:
            return repos

        def filter_func(r: Repo):
            return r.parent_owner == self.forked_repo_owner

        return filter(filter_func, repos)

    def run(self):
        repos = self.list_repos()

        if len(repos) <= 0:
            print("No forked repos found! Exiting.")
            return

        forked_repos = Cleaner.forked_repos(repos)

        if self.forked_repo_owner:
            forked_repos = self.forked_from_stored_owner(forked_repos)

        if len(forked_repos) <= 0:
            print(f"No Repos forked from user {self.forked_repo_owner}! Exiting.")
            return

        max_sleep = self.max_sleep_time

        if not self.do_random_sleep:
            max_sleep = 0

        for r in forked_repos:
            sleep_time = random.randrange(max_sleep)
            print(f"sleeping for {sleep_time} seconds.")
            time.sleep(sleep_time)
            r.delete(self.access_key)
            print(f"Deleted repo {r.name}")



