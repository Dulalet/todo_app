FROM python

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

RUN apt-get update -yqq && apt-get upgrade -yqq && apt-get install -y --no-install-recommends

COPY requirements.txt /usr/src/app

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8000

#RUN adduser --disabled-password --gecos '' myuser
#CMD ["python3", "-u", "manage.py", "runserver", "[::]:8000"]
