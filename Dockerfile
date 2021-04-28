FROM python:3.8.3-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

RUN apk update
RUN pip install --upgrade pip
RUN pip install django_rest_framework
RUN pip install django-bootstrap-modal-forms
RUN apk add python3-dev
RUN apk add gpgme-dev
RUN apk add libc-dev
RUN apk add gcc jpeg-dev zlib-dev libffi-dev freetype-dev musl-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev cairo-dev pango-dev gdk-pixbuf-dev
RUN apk add mariadb-dev
RUN pip install mysqlclient

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
