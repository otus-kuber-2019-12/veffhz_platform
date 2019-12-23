FROM python:3.6.0-alpine

RUN addgroup -S user && adduser -S user -G user -u 1001
USER user

WORKDIR /server

ADD server.py /server

RUN pip install flask==1.1.1 --user

ADD homework.html /app/

EXPOSE 8000

ENTRYPOINT ["python3", "server.py"]