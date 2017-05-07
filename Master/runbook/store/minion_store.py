#! /usr/bin/env python3
# Persistant storage for minion settings.

import pickle
from collections import namedtuple

from .. import config

STORE_PATH = config.MINION_STORE_PATH

Minions = namedtuple('Minions', ['username', 'hostnames'])

class ConfigurationError(Exception):
    pass

def get_minions():
    try:
        with open(STORE_PATH, 'rb') as fd:
            minions = pickle.load(fd)
    except FileNotFoundError:
        raise ConfigurationError('Username and hostnames have not been set.')
    return minions

def set_minions(username, hostnames):
    minions = Minions(username=username, hostnames=tuple(hostnames))
    with open(STORE_PATH, 'wb') as fd:
        minions = pickle.dump(minions, fd)
