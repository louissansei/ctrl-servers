FROM ubuntu:16.04 

ARG username=ubuntu
ARG homedir=/home/${username}/

RUN apt-get update && \
    apt-get install -y openssh-server && \
    useradd -d $homedir -m $username -p fds#657kJ && \
    mkdir /var/run/sshd && \
    mkdir /home/${username}/.ssh

COPY id_rsa.pub /home/${username}/.ssh/authorized_keys

RUN chown -R ${username}:${username} /home/${username}/.ssh && \
    chmod 700 /home/${username}/.ssh  && \
    chmod 600 /home/${username}/.ssh/authorized_keys

EXPOSE 22

CMD ["/usr/sbin/sshd","-D"]
