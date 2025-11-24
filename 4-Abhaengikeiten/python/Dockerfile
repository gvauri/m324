FROM python:latest

WORKDIR /usr/src/app

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY main.py .

CMD ["python", "main.py"]