FROM python:3.8-slim-buster
ENV FLASK_APP app.py
ENV FLASK_ENV development
ENV FLASK_DEBUG: 'true'
RUN apt-get update -y && apt-get install \
    -y python-pip python-dev build-essential
RUN mkdir /usr/src/gh-url-shortener
WORKDIR /usr/src/gh-url-shortener
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
ENTRYPOINT ["flask"]
CMD ["run", "--host=0.0.0.0"]