FROM alpine:latest

RUN apk update && \
    apk add build-base wget git

WORKDIR /usr/src/app

RUN git clone https://github.com/ggerganov/llama.cpp .

RUN make server

EXPOSE 8000

ENTRYPOINT wget -nc -O ${MODEL_FILE} ${MODEL_URL} && ./server --port 8000
