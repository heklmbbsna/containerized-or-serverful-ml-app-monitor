FROM python:3.10-slim

WORKDIR /cmpt756-g15-serverful-ml-app

COPY . /cmpt756-g15-serverful-ml-app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]