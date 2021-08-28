FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app

COPY ./scripts/ /scripts/

RUN chmod +x /scripts/*

RUN apk update

RUN pip install --upgrade pip

RUN apk add --update --no-cache postgresql-client jpeg-dev

RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev libffi-dev linux-headers postgresql-dev musl-dev \
      zlib zlib-dev openssl-dev rust 

RUN apk add --update \
  build-base \
  cairo \
  cairo-dev \
  cargo \
  freetype-dev \
  gcc \
  gdk-pixbuf-dev \
  gettext \
  jpeg-dev \
  lcms2-dev \
  libffi-dev \
  musl-dev \
  openjpeg-dev \
  openssl-dev \
  pango-dev \
  poppler-utils \
  postgresql-client \
  postgresql-dev \
  py-cffi \
  python3-dev \
  rust \
  tcl-dev \
  tiff-dev \
  tk-dev \
  zlib-dev \
  linux-headers

RUN pip install cryptography

RUN pip install -r requirements.txt

RUN apk del .tmp-build-deps

COPY ./app /app

RUN adduser --disabled-password --no-create-home app && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R app:app /vol && \
    chmod -R 755 /vol

ENV PATH="/scripts:/py/bin:$PATH"

USER app

CMD ["run.sh"]


CMD python manage.py runserver 0.0.0.0:$PORT