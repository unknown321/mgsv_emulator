FROM debian:stretch-slim
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get install -y --no-install-recommends apache2 \
                    python3 \
                    libapache2-mod-wsgi-py3 \
                    wget \
                    gnupg2 \
                    vim \
    && wget http://repo.percona.com/apt/percona-release_0.1-5.stretch_all.deb \
    && dpkg -i percona-release_0.1-5.stretch_all.deb \
    && apt-get update \
    && apt-get install -y --no-install-recommends percona-server-server-5.7 \
    && mkdir -p /var/www/mgsv_server/wsgi-scripts/mgsv_emulator 
COPY [ "emulator", "/var/www/mgsv_server/wsgi-scripts/mgsv_emulator" ]
COPY myapp.wsgi /var/www/mgsv_server/wsgi-scripts
COPY mgs_server.conf /etc/apache2/sites-available/
COPY static_key.bin /var/www/mgsv_server/
RUN mkdir -p /var/www/mgsv_server/www \
	&& a2ensite mgs_server \
	&& a2dissite 000-default \
	&& service mysql start \
	&& service apache2 start

EXPOSE 80