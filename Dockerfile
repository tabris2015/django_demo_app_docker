FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
RUN echo build
WORKDIR /app
RUN ls
RUN apt update && apt install nginx -y
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
# run migrations and initial data

