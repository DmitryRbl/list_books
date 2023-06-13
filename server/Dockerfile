FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

ADD . /code

WORKDIR /code

RUN pip install -r server/requirements.txt

CMD ["python", "app.py"]