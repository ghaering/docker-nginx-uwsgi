FROM debian
RUN apt-get update -y
RUN apt-get install -y uwsgi-plugin-python python python-virtualenv
RUN virtualenv /venv
RUN /venv/bin/pip install flask
RUN mkdir /app/
ADD *.py /app/
ADD uwsgi.ini /app/
EXPOSE 5555
ENTRYPOINT ["/usr/bin/uwsgi", "--plugin", "python", "--ini", "/app/uwsgi.ini", "-s", "0.0.0.0:5555"]
