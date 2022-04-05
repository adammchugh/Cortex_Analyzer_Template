FROM python:3.9-alpine3.15
LABEL maintainer=adam.mchugh@mchughsecurity.com

ENV LANG=C.UTF-8

WORKDIR /analyzer

COPY template.py template.json requirements.txt ./

RUN pip install --no-cache-dir --requirement requirements.txt

ENTRYPOINT ["/bin/sh","-c","/analyzer/template.py"]
