FROM python:3.10

WORKDIR /client

COPY requirements.txt /client/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /client/requirements.txt

COPY . /client/

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "localhost", "--port", "8000", "--reload"]