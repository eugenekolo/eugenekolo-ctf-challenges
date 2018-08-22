FROM ubuntu:xenial
MAINTAINER Eugene Kolodenker <eugene@kolobyte.com>

RUN apt-get update
RUN apt-get -y install openssh-server gcc gdb g++-multilib python ruby nodejs

WORKDIR /opt/challenge

COPY sshd_config /etc/ssh/sshd_config
COPY rop101.c .
COPY flag1.txt .
COPY flag2.txt .
COPY flag3.txt .

RUN gcc -o rop101 rop101.c -m32 -fno-stack-protector -static
RUN rm rop101.c /usr/bin/top /bin/ps
RUN chmod +x /opt/challenge/

RUN useradd chalowner
RUN chown chalowner:chalowner rop101
RUN chmod g+s rop101
RUN chown chalowner:chalowner flag1.txt
RUN chown chalowner:chalowner flag2.txt
RUN chown chalowner:chalowner flag3.txt
RUN chmod 440 flag1.txt
RUN chmod 440 flag2.txt
RUN chmod 440 flag3.txt

RUN useradd -ms /bin/bash  -d /opt/challenge challenge
RUN passwd -d challenge

RUN mkdir /var/run/sshd

CMD ["/usr/sbin/sshd", "-D"]
