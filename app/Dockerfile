FROM python:3.9-alpine

RUN apk update && apk add gcc musl-dev linux-headers && \
    pip3 install --upgrade pip
    
WORKDIR /opt/app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY app.py app.py

CMD [ "python3", "app.py" ]