FROM nvidia/cuda:10.0-base AS builder

ENV LANG=C.UTF-8
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    python3-venv \
&& rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /venv
ENV PATH=/venv/bin:$PATH

COPY requirements.txt /requirements.txt
RUN pip install --requirement=/requirements.txt


FROM nvidia/cuda:10.0-base

LABEL maintainer="hyeon0145@gmail.com"
ENV LANG=C.UTF-8

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-venv \
&& rm -rf /var/lib/apt/lists/*

COPY --from=builder /venv /venv

COPY . /app
WORKDIR /app

ENV PATH=/venv/bin:$PATH
CMD python3 -m gpugpu
