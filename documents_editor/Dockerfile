FROM ubuntu:20.04 as building

RUN apt update && apt upgrade -y

RUN apt install python3 python3-pip -y

COPY  . /app

WORKDIR /app

# после запуска контейнера необходимо запустить
# init.sh в интерактивном режиме для поддержки сетевого принтера

FROM building as application

RUN pip install -r requirements.txt

CMD uvicorn main:app --host 0.0.0.0 --reload --workers 2
