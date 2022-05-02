FROM python:3.10

COPY . /server

WORKDIR /server

RUN pip install -r requirements.txt

CMD uvicorn main:app --host 0.0.0.0 --reload --workers 2
