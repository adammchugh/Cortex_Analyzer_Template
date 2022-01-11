FROM python:3.9-alpine3.15
LABEL maintainer=adam.mchugh@mchughsecurity.com

WORKDIR /analyzer

COPY template template
RUN pip install --no-cache-dir --requirement template/requirements.txt

ENTRYPOINT ["template/template.py"]
