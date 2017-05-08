# CtrlServers

This project is primarily a web app which exposes a REST interface that forwards commands to multiple machines over ssh, and returns the command output from each. It is implemented in python3 (tested with python 3.5). A simple client is also included.
The api is available at the following url:
<pre>http://hostname/api/</pre>
It has a 'run' resource and a 'configure' resource. Both these resources only acccept a POST request with a json payload.

See the client application for details.
 
## Setting up and running the master server locally

$ pip install flask-restful

$ pip install fabric3

$ cd Master

$ ./start_server


## Setting up and running the client

$pip install requests

$ cd Client

Edit client.py - make sure that the hostname in BASE_URL is correct for your set up.

Edit configuration.json - this file contains the minion-servers IP addresses (or hostnames) and username (assumes all minions have the same username).

Public keys (with no password on the private key) must have been shared with the minion-servers for successful connections.

Optionally edit payload.json - this file contains the command to be run on the minions.

The webserver persists the minion-server settings, so it is only necessary to send the configuration initially and when it is changed. However, client.py currently sends the configuration each time it is run. 

## Using the Docker images

Alternatively, docker images are available from Docker Hub:

$ docker pull louissansei/master

$ docker pull louissansei/minion

Run the containers in separate termninals.

$ docker -t run louissansei/master:latest

$ docker -t run louissansei/minion:latest

The minion exposes port 22, and the master exposes port 5000.

