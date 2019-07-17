FROM python:3.7-alpine3.10 as base
FROM base as builder

RUN apk update
RUN apk add build-base

RUN mkdir /usr/src/secretsharing
WORKDIR /usr/src/secretsharing
COPY . .

RUN python -m venv /usr/src/venv

RUN source /usr/src/venv/bin/activate

RUN python setup.py install

ENV VIRTUAL_ENV=/usr/src/venv

ENTRYPOINT [ "python" ]
CMD ["-m", "secretsharing"]