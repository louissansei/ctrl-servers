#! /usr/bin/env python3

from ..store import minion_store

def configure(payload):
    try:
        username = payload['username']
    except KeyError:
        return "Username not specified.", 400

    try:
        hostnames = payload['hostnames']
    except KeyError:
        return "Hostnames not specified.", 400

    minion_store.set_minions(username, hostnames)
    return "Configured.", 200
