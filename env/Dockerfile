FROM ubuntu:jammy
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get -y --no-install-recommends install \
        python3 python3-pip python3-tk git ca-certificates fontconfig

RUN pip install mechanicalsoup
RUN git clone https://github.com/Enthalpy-AC/catalysis /app
RUN mkdir /root/.fonts && cp /app/PWExtended.ttf /root/.fonts/ && fc-cache -fv

WORKDIR /app
ENTRYPOINT [ "python3", "/app/catalysis.py" ]
