FROM python:3

WORKDIR /usr/src/app

COPY udpServer.py ./

CMD [ "python", "-u", "./udpServer.py" ]