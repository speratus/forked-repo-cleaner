import os


GHUB_TOKEN_VAR = 'GITHUB_TOKEN'


def load_github_token():
    return os.environ.get(GHUB_TOKEN_VAR)
