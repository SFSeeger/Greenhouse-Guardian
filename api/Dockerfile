FROM python:3.11-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apt-get update
RUN apt-get install -y default-libmysqlclient-dev libssl-dev libffi-dev build-essential pkg-config gettext

WORKDIR /app/web
COPY --chown=root:root src/ ./src/

WORKDIR /app
ADD ./requirements-dev.txt ./
ADD ./entrypoint.sh ./

RUN pip install -r requirements-dev.txt --no-cache-dir 
EXPOSE 80
EXPOSE 3000

WORKDIR /app/web
ENTRYPOINT [ "bash", "/app/entrypoint.sh" ]