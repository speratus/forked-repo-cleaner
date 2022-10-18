import os
import sys

from .cleaner import Cleaner


GHUB_TOKEN_VAR = 'GITHUB_TOKEN'


def load_github_token():
    token_result = os.environ.get(GHUB_TOKEN_VAR)
    if token_result is not None:
        return token_result
    else:
        return ''


if __name__ == '__main__':
    cleaner = Cleaner(sys.argv, load_github_token())
    cleaner.run()

