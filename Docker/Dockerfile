FROM debian:latest

RUN apt update
RUN apt-get install -y git python3-pip

WORKDIR /usr/src

RUN git clone https://github.com/Goujer/kanojo_server.git

WORKDIR /usr/src/kanojo_server

RUN pip3 install -r /usr/src/kanojo_server/requirements.txt

RUN mv config.py.template config.py

COPY . /usr/bin

ENV PORT_VAL=5000
ENV HTTPS=False
ENV MONGO_CONN_STRING=
ENV MONGO_REAL_STRING=

EXPOSE 5000

ENTRYPOINT KanojoStart
