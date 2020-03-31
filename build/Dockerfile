#### Base OS ####
FROM phusion/baseimage:0.10.0

#### Build ####
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y update
RUN apt-get -y install build-essential && \
    apt-get -y install python-dev python-pip python-tk && \
    apt-get -y install git
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools wheel
RUN pip install --upgrade twine

#### Python Libs ####
RUN pip install pandas numpy pyarrow
RUN pip install matplotlib seaborn
RUN pip install pycryptodome
RUN pip install pathlib
RUN pip install minio

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#### Files ####
RUN mkdir -p /build/
COPY scripts/envvars.sh /build/
COPY scripts/run.sh /
RUN chmod +x /run.sh

#### Networking ####

#### Start ####
CMD ["/bin/bash", "/run.sh"]
