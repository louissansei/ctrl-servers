FROM ubuntu:16.04

RUN apt-get update && \
    apt-get -y install \
            libffi-dev \
	    libssl-dev \
	    python3 \
	    python3-pip && \
    pip3 install flask-restful \
                 fabric3

ARG username=ubuntu
ARG homedir=/home/${username}/

RUN useradd -d $homedir -m $username -p fds#657kJ

COPY id_rsa /home/${username}/.ssh/id_rsa

COPY start_server.py $homedir
COPY runbook ${homedir}runbook/

RUN chown -R ${username}:${username} ${homedir}/.ssh && \
    chown -R ${username}:${username} ${homedir}/runbook && \
    chown ${username}:${username} ${homedir}/start_server.py && \
    chmod 700 ${homedir}/.ssh  && \
    chmod 600 ${homedir}/.ssh/id_rsa && \
    chmod 700 ${homedir}/start_server.py


EXPOSE 5000

USER $username
CMD $HOME/start_server.py
