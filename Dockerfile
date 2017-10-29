FROM debian:stretch-slim
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    				apache2 \
                    python3 \
                    libapache2-mod-wsgi-py3 \
                    wget \
                    gnupg2 \
                    python3-pip \
                    gcc \
                    python3-dev \
                    libssl-dev \
                    vim \
    && wget http://repo.percona.com/apt/percona-release_0.1-5.stretch_all.deb \
    && dpkg -i percona-release_0.1-5.stretch_all.deb \
    && apt-get update \
    && apt-get install -y --no-install-recommends percona-server-server-5.7 libperconaserverclient20-dev \
    && mkdir -p /var/www/mgsv_server/wsgi-scripts/mgsv_emulator \
    && mkdir -p /var/www/mgsv_server/logs \
    && mkdir -p /var/www/mgsv_server/www/tppstmweb/eula \
    && touch /var/log/app.log /var/www/mgsv_server/logs/access.log /var/log/error.log \
    && pip3 install requests setuptools wheel \
    && pip3 install mysqlclient \
    && chown www-data:www-data /var/log/app.log /var/log/error.log
COPY [ "src/mgsv_emulator", "/var/www/mgsv_server/wsgi-scripts/mgsv_emulator" ]
COPY files/myapp.wsgi /var/www/mgsv_server/wsgi-scripts
COPY files/mgs_server.conf /etc/apache2/sites-available/
COPY files/static_key.bin /var/www/mgsv_server/
COPY files/eula.var /var/www/mgsv_server/www/tppstmweb/eula
COPY files/database.sql /database.sql
COPY files/entrypoint.sh /entrypoint.sh
RUN a2ensite mgs_server \
	&& a2dissite 000-default \
	&& chmod +x /entrypoint.sh \
	&& rm /percona-release_0.1-5.stretch_all.deb \
	&& chown -R www-data:www-data /var/www/mgsv_server
EXPOSE 80
CMD ["/entrypoint.sh"]
