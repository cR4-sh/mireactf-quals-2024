FROM gcc:4.9 as builder
COPY src /usr/src/
WORKDIR /usr/src/
RUN gcc -o chall main.c

FROM alpine:3.19.1
RUN apk update && apk add socat libc6-compat
WORKDIR /app
COPY --from=builder /usr/src/chall .
RUN adduser -D user && \
        chmod 555 chall

USER user
CMD ["socat", "tcp-l:9003,reuseaddr,fork", "EXEC:'/app/chall'"]

EXPOSE 9003/tcp