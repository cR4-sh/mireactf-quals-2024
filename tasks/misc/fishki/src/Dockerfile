FROM golang:1.21.0 as builder

WORKDIR /usr/src/app

COPY go.mod go.sum* ./
RUN go mod download && go mod verify
COPY ./handlers ./handlers/
COPY ./models ./models/
COPY ./main.go .
RUN go build -o /usr/local/bin/app


FROM alpine:latest


EXPOSE 8080
RUN apk add libc6-compat
RUN addgroup -g 2000 fishki && adduser -u 2000 -G fishki -s /bin/sh -D fishki --home /app
USER fishki
WORKDIR /app

COPY --from=builder /usr/local/bin/app ./
COPY ./resources ./resources
COPY ./templates ./templates


CMD ["./app"]

