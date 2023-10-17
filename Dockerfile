FROM python:3.8-slim

WORKDIR /app

COPY app.py /app
COPY /templates/ /app/templates
COPY /static/ /app/static

RUN pip install flask

EXPOSE 5000

CMD ["python", "app.py"]
