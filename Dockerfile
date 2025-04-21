FROM ubuntu:latest
MAINTAINER Druzhinin Vasily 'web_dev_drizhinin@mail.com'
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip python-dev-is-python3 build-essential python3-venv
RUN adduser --disabled-password admin
RUN mkdir /home/altair/ && chown -R admin:admin /home/altair
RUN mkdir -p /var/log/altair && touch /var/log/altair/altair.err.log && touch /var/log/altair/altair.out.log
RUN chown -R admin:admin /var/log/altair

WORKDIR /home/altair
USER admin
# copy all the files to the container
COPY --chown=admin:admin . .

# venv
ENV VIRTUAL_ENV=/home/altair/venv

RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# upgrade pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# define the port number the container should expose
EXPOSE 8000


#CMD ["gunicorn", "--workers", "4", "--timeout", "6000",  "--bind", ":8000", "wsgi:app"]

