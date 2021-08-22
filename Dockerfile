FROM python:3.8-slim-buster

ENV PYTHONPATH /
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./app /app
WORKDIR /app
EXPOSE 8000
USER 1000
CMD ["uvicorn", "main:app_", "--host", "0.0.0.0", "--port", "8000"]