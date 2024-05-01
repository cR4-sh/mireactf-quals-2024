FROM golang:1.21.0 as builder

WORKDIR /usr/src/app

COPY ./web/go.mod ./web/go.sum* ./
RUN go mod download && go mod verify


COPY ./web/handlers ./handlers/
COPY ./web/database ./database/
COPY ./web/main.go .
COPY ./web/templates ./templates/
COPY ./web/secret-data ./secret-data/
RUN go build -o /usr/local/bin/app

FROM mongo:latest

WORKDIR /app
EXPOSE 8080
COPY --from=builder /usr/local/bin/app ./
COPY --from=builder /usr/src/app/templates ./templates
COPY --from=builder /usr/src/app/secret-data ./secret-data
COPY ./mongodb_data /data/db 
COPY ./web/resources ./resources
RUN apt-get update && apt-get install -y supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]

