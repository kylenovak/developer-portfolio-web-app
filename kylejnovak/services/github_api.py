from kylejnovak import app

import requests
import json


def get_github_username():
    return app.config['GITHUB_USERNAME']


def get_github_starred_repos():
    starred_repos = []

    uri = 'https://api.github.com/user/starred?access_token={}'
    secret_token = app.config['GITHUB_API_TOKEN']

    # attach the secret token to the uri
    uri = uri.format(secret_token)

    try:
        uri_response = requests.get(uri)
    except requests.ConnectionError:
        app.logger.error('Github API connection error.')
        return None

    json_response = uri_response.text
    repos = json.loads(json_response)
    for repo in repos:
        starred_repo = dict()
        starred_repo['name'] = repo['name']
        starred_repo['html_url'] = repo['html_url']
        starred_repo['stargazers_count'] = repo['stargazers_count']
        starred_repo['forks_count'] = repo['forks_count']
        starred_repo['description'] = repo['description']
        starred_repo['updated_at'] = repo['updated_at']
        starred_repos.append(starred_repo)

    return starred_repos
