#! /usr/bin/env python3


from ..ssh import remote_ctrl

def run(payload):
    try:
        command = payload['command']
    except KeyError:
        return "Command not specified.", 400

    try:
        output = remote_ctrl.run(command)
        return output, 200
    except Exception as e:
        return str(e), 500
