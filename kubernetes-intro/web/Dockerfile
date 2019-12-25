FROM python:3.7-alpine

RUN addgroup -S user && adduser -S user -G user -u 1001
USER user

WORKDIR /app

ADD homework.html /app/

EXPOSE 8000/tcp

ENTRYPOINT ["python3", "-m", "http.server", "8000", "--directory", "/app"]