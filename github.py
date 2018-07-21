"""Retrieve some info using GitHib API."""

import requests

user = "AlexSkrn"

response = requests.get('https://api.github.com/users/{}/events'.format(user))

event = response.json()[0]['type']

creation_date = response.json()[0]['created_at']

print("The user {}'s latest event was {} on {}".format(user,
                                                       event,
                                                       creation_date))
