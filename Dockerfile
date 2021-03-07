FROM python:3.7-slim-buster

WORKDIR /app
ADD requirements.txt /app

RUN set -ex && \
    pip install -r requirements.txt

ADD myapp.py *.conf /app/

EXPOSE 8000

ENTRYPOINT ["/usr/local/bin/gunicorn", "--config", "/app/gunicorn.conf", "--log-config", "/app/logging.conf", "-b", ":8000", "myapp:app"]
