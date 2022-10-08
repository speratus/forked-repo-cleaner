class UrlBuilder:

    def __init__(self, alternate_options={}):
        if not alternate_options == {}:
            self.scheme = alternate_options['scheme']
            self.host = alternate_options['host']
            self.base_path = alternate_options['base_path']
        else:
            self.scheme = 'https'
            self.host = 'api.github.com'
            self.base_path = ''

    def base_url(self):
        return f"{self.scheme}://{self.host}{self.base_path}"

    def get_repo(self, owner: str, repo: str):
        return f"{self.base_url()}/repos/{owner}/{repo}"

    def delete_repo(self, owner: str, repo: str):
        return f"{self.base_url()}/repos/{owner}/{repo}"

    def list_repos(self, username):
        return f"{self.base_url()}/users/{username}/repos"

