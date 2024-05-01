FROM ubuntu:jammy as builder
RUN apt update && apt install build-essential gcc-multilib g++-multilib -yyy
COPY src /usr/src
WORKDIR /usr/src
RUN gcc main.cpp -o chall

# FROM gcc:4.9 as builder
# COPY src /usr/src/
# WORKDIR /usr/src/
# RUN gcc -std=c++14 -o chall main.cpp

FROM debian:12-slim
RUN apt update && apt install socat -yyy
WORKDIR /app
COPY --from=builder /usr/src/chall .
# COPY chall .
RUN adduser user && \
        chmod 555 chall

USER user
CMD ["socat", "tcp-l:9001,reuseaddr,fork", "EXEC:'/app/chall'"]

EXPOSE 9001/tcp