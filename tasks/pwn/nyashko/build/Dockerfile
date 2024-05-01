FROM gcc:4.9 as builder
COPY src /usr/src/
WORKDIR /usr/src/
RUN gcc -std=c++14 --no-pie -o chall main.cpp

FROM alpine:3.19.1
RUN apk update && apk add socat libc6-compat
ENV PASSPHRASE S5p3rNy4sh00!!
WORKDIR /app
COPY --from=builder /usr/src/chall .
COPY startup.sh .
RUN adduser -D user && \
        chmod 555 chall startup.sh

CMD ["./startup.sh"]

EXPOSE 9000/tcp