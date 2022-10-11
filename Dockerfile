FROM python:3.9
ENV PYTHONUNBUFFERED 1

RUN mkdir /vps_app

WORKDIR /vps_app

ADD . /vps_app/

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt