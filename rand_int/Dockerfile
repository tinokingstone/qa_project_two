FROM python:3.7
#RUN apt-get update -y
WORKDIR /app
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
ENTRYPOINT ["/usr/local/bin/python","app,py"]
