FROM python:3.11-bullseye as base

USER root

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y default-libmysqlclient-dev libssl-dev libffi-dev build-essential pkg-config gettext

WORKDIR /app/web
COPY --chown=root:root src/ ./

ADD ./entrypoints/* ./

FROM base as dev
ADD ./requirements-dev.txt ./

RUN pip install -r requirements-dev.txt --no-cache-dir 
EXPOSE 80
EXPOSE 3000

ENTRYPOINT [ "bash", "/app/web/dev.sh" ]


FROM base as prod
ADD ./requirements.txt ./

RUN pip install -r requirements.txt --no-cache-dir 

EXPOSE 80

ENTRYPOINT [ "bash", "/app/web/prod.sh" ]