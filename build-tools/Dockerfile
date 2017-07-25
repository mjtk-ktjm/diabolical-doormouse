FROM alpine:3.6 

MAINTAINER Mathew J Kelly <mjtk.ktjm@gmail.com>

RUN apk update && \
    apk add vim && \ 
    apk add python3 python3-dev uwsgi-python3 py3-lxml tzdata dcron
 
RUN /usr/bin/pip3 install --upgrade pip && \
    /usr/bin/pip3 install argparse jinja2 

ADD python3 /toolbox

WORKDIR /toolbox

RUN ln -s /share

CMD ["/bin/sh"]
