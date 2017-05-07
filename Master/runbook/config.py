#! /usr/bin/env python3

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

MINION_STORE_PATH = os.path.join(BASE_DIR, 'store', 'minions.pkl')

#Server settings.
LISTEN_ON = '0.0.0.0'
PORT = 5000

SSH_PORT = 22
