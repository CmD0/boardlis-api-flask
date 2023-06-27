FROM python:latest

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "src/main.py" ]
