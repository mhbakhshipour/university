FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /univercity
WORKDIR /univercity
COPY requirements.txt /univercity/
RUN pip install -r requirements.txt
COPY . /univercity/