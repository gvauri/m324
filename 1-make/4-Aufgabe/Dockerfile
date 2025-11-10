FROM debian:stable-slim

WORKDIR /app

RUN apt-get update && apt-get install -y g++

COPY main.cpp /app/main.cpp

RUN g++ main.cpp -o a.out

CMD ["./a.out"]
