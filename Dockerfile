FROM python:3.9-slim
WORKDIR /app
COPY ./40131401 /app
CMD ["echo", "Docker is running"]