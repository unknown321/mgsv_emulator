FROM debian:stretch-slim
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get install -y --no-install-recommends apache2 \
                    python3 \
                    libapache2-mod-wsgi-py3 \
                    wget \
                    gnupg2 \
    && wget http://repo.percona.com/apt/percona-release_0.1-5.stretch_all.deb \
    && dpkg -i percona-release_0.1-5.stretch_all.deb \
    && apt-get update \
    && apt-get install -y --no-install-recommends percona-server-server-5.7
COPY emulator /var/www/