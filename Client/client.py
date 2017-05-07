#! /usr/bin/env python3

import requests

from urllib.parse import urljoin

PAYLOAD_PATH = 'payload.json'
CONFIG_PATH = 'configuration.json'
BASE_URL = 'http://localhost:5000/api/'

HEADERS = {'Content-Type': 'application/json'}

def run():
    post('run', PAYLOAD_PATH)

def configure():
    post('configure', CONFIG_PATH)

def post(relative_url, json_path):
    url = urljoin(BASE_URL, relative_url)
    payload = get_json(json_path)

    response = requests.post(url, headers=HEADERS, data=payload)
    print("Status code: %d: %s" % (response.status_code, response.content))

def get_json(path):
    with open(path) as fd:
        return fd.read()

if __name__ == '__main__':
    configure()
    run()
