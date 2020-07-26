FROM python:3.7
MAINTAINER Mayuri Lahane "mayurilahane1998@gmail.com"
WORKDIR /var
COPY ./* .
RUN python3 setup.py install
ENTRYPOINT [ "/bin/bash" ]
