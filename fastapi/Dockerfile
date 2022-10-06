FROM python:latest
RUN mkdir -p /opt/api
WORKDIR /opt/api
RUN pip install fastapi[all]
#RUN pip install "uvicorn[standard]"
#RUN pip install pydantic
RUN pip install jupyter
COPY main.py /opt/api/main.py

RUN apt-get update && \
    apt-get install -y curl sudo procps net-tools dnsutils vim wget

RUN curl -s https://raw.githubusercontent.com/dapr/cli/master/install/install.sh --insecure | /bin/bash
#RUN wget -q https://raw.githubusercontent.com/dapr/cli/master/install/install.sh -O - | /bin/bash
RUN dapr -v

RUN dapr init --slim

COPY requirements.txt /api/requirements.txt

COPY dapr /dapr

EXPOSE 8000

COPY start.sh /opt/api/

#CMD uvicorn main:app --host 0.0.0.0 --reload
CMD /bin/bash ./start.sh
