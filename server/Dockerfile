FROM python:3.10

WORKDIR /server

COPY requirements.txt /server/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /server/requirements.txt

COPY . /server/

EXPOSE 5000

CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]