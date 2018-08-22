FROM ubuntu:xenial
MAINTAINER Robert Clark <rbclark@mitre.org>

RUN apt-get update

RUN apt-get -y install netcat openssh-server python tmux

COPY flag.txt /opt/challenge/flag.txt
COPY tinyworld.py /opt/challenge/tinyworld.py
COPY sshd_config /etc/ssh/sshd_config
COPY tmux.conf /etc/tmux.conf

RUN chmod +x /opt/challenge/tinyworld.py
RUN useradd -ms /opt/challenge/tinyworld.py challenge
RUN passwd -d challenge
RUN mkdir /var/run/sshd

EXPOSE 22
EXPOSE 2000-2100
CMD ["/usr/sbin/sshd", "-D"]