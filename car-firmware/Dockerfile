ARG IMAGE_ARCH=arm64v8
FROM torizon/$IMAGE_ARCH-debian-base:3-bookworm
WORKDIR /home/torizon

RUN apt-get -y update && apt-get install -y \ 
    nano \ 
    python3 \ 
    python3-pip \ 
    python3-setuptools \ 
    git \ 
    iproute2 \ 
    can-utils \ 
    python3-can \ 
    libopencv-dev \
    python3-opencv\
    && apt-get clean && apt-get autoremove && rm -rf /var/lib/apt/lists/*  

# COPY requirements.txt /app/

# RUN pip install -r requirements.txt

COPY /src /app

