ARG FROM=trophime/salome:9.11.0-debian11

FROM ${FROM}

ARG DEBUG=1

ARG NUMTHREADS=1
ARG TERM=linux
ARG DEBIAN_FRONTEND=noninteractive
ARG DESTDIR=/opt
ARG VERSION=9.11.0
ARG PLATFORM=DB11

USER root

# Setup demo environment variables
ENV LANG=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    LC_ALL=C.UTF-8 \
    PATH=${DESTDIR}/SALOME-${VERSION}-${PLATFORM}:${DESTDIR}/SALOME-${VERSION}-${PLATFORM}/sat:$PATH


CMD ["salome","-w1"]

