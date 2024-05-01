FROM gcc:4.9 as builder
COPY src /usr/src/
WORKDIR /usr/src/
RUN gcc -std=c++14 --no-pie -o chall main.cpp

FROM debian:12-slim
RUN apt update && apt install socat -yyy
WORKDIR /app
COPY --from=builder /usr/src/chall .
RUN adduser user && \
        chmod 555 chall

USER user
CMD ["socat", "tcp-l:9002,reuseaddr,fork", "EXEC:'/app/chall'"]

EXPOSE 9002/tcp