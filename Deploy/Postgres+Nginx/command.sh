docker image build -f ./Nginx/Dockerfile .
docker network create pg
docker container run --name pg --network pg -v pgdata:/var/lib/postgresql/data -d --env-file ./Postgres/db.env postgres:latest
docker container run --name webapp --network pg -d --env-file ./Nginx/app.env jfahrer/demo_web_app:latest
docker container run --name lb --network pg -d -p 80:80 -e PROXY_UPSTREAM=webapp:9292 --env-file ./Nginx/app.env vbelousov/nginx_lb:latest

#####################

USE WORKDIR in DOCKERFILE INSTEAD FULL PATH!!!

#########################