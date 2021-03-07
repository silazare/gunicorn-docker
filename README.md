## Gunicorn app example

Gunicorn app example for JSON logging tests.
Forked from original article repo - https://sebest.github.io/post/protips-using-gunicorn-inside-a-docker-image/

### Installation

1) Build Docker image:
```shell
docker build -t gunicorn-docker .
```

2) Run app:
```shell
docker run -d -e GUNICORN_WORKERS=4 -e GUNICORN_ACCESSLOG=- -p 8000:8000 gunicorn-docker
```

3) Test endpoints and check the logs in JSON format:
```shell
curl localhost:8000/path
curl localhost:8000/exception

docker logs <container_id> 
```
