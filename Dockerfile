FROM znly/protoc

RUN apk add --no-cache --update python py-pip git
RUN pip install --upgrade pip

WORKDIR /app
ADD ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ADD . /app

ENTRYPOINT ["python", "curate/curate.py"]
