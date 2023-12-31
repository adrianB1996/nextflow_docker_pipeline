FROM python:3

WORKDIR .

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt


COPY /bin/. /bin

COPY /data/. /data


COPY main.nf ./

COPY nextflow.config ./