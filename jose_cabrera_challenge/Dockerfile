
FROM alpine:3.7

ADD requirements.txt /home/app/
WORKDIR /home/app/

RUN apk add --no-cache postgresql-dev gcc python3 python3-dev musl-dev \
    py-pip portaudio-dev && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache && \
    pip3 install -r requirements.txt && \
    pip install flask-expects-json && \
    pip install SpeechRecognition && \
    pip install -U pip && \
    pip install paho-mqtt pyaudio

# ADD ./app /home/app/
# WORKDIR /home/app/

EXPOSE 5000

ENTRYPOINT ["python3", "run.py"]
