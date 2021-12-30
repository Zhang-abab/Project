# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
COPY testdb.py /
COPY docker-entrypoint.sh /
RUN chmod +x /testdb.py /docker-entrypoint.sh
#RUN pip install -r requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /code/
ENTRYPOINT ["/docker-entrypoint.sh"]
EXPOSE 8000