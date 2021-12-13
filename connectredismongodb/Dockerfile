# 1. ubuntu 설치 ( 패키지 업데이트 + 만든 사람 표시 )
FROM python:3.7.9
RUN python3 -m pip install pip --upgrade
RUN pip install wheel
COPY . /usr/src/app
WORKDIR /usr/src/app
EXPOSE 8000
EXPOSE 6379