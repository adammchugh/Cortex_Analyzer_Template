LABEL maintainer=adam.mchugh@mchughsecurity.com

FROM python:3.13-slim
WORKDIR /worker
COPY . .
RUN test ! -e /worker/requirements.txt || pip install --no-cache-dir -r /worker/requirements.txt
ENTRYPOINT ["/bin/sh","-c","/worker/{command}}"]