################# Builder ###############
FROM fampay:base AS base

COPY ./requirements.txt .

RUN pip install -r requirements.txt

################# Release ###############
FROM python:3.7-alpine AS release

RUN apk add --update --no-cache bash libpq

COPY --from=base /usr/local/lib/python3.7/site-packages/ /usr/local/lib/python3.7/site-packages/
COPY --from=base /usr/local/bin/ /usr/local/bin/

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ENV PATH=/root/local/bin:$PATH

WORKDIR /src
RUN mkdir /src/staticfiles

COPY . /src/

