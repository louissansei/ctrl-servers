#! /usr/bin/env python3

from fabric import api
from fabric.api import env

from fabric import tasks
from fabric import network
from fabric.context_managers import hide

from ..store import minion_store
from .. import config


class ExecutionException(Exception):
    pass

env.port = config.SSH_PORT
env.warn_only = True
env.abort_exception = ExecutionException
env.abort_on_prompts = True


def host_type(command):
    output = api.run(command)
    return output

def run(command):
    minions = minion_store.get_minions()
    env.user = minions.username
    env.hosts = minions.hostnames

    with hide('everything'):
        output = tasks.execute(host_type, command=command)

    network.disconnect_all()

    return output

