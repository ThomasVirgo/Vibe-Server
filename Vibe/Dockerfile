FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
# Add back in for deployment
# CMD gunicorn DockerDjango.wsgi:application --bind 0.0.0.0:$PORT