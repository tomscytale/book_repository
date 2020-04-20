FROM python:3.8-slim-buster
COPY requirements.txt /code/requirements.txt
WORKDIR /code
RUN pip install -r requirements.txt
ADD . /code
CMD python -m book_request
