FROM debian:stretch-slim
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    				apache2 \
                    python3 \
                    libapache2-mod-wsgi-py3 \
                    wget \
                    gnupg2 \
                    python-mysqldb \
                    vim \
    && wget http://repo.percona.com/apt/percona-release_0.1-5.stretch_all.deb \
    && dpkg -i percona-release_0.1-5.stretch_all.deb \
    && apt-get update \
    && apt-get install -y --no-install-recommends percona-server-server-5.7 \
    && mkdir -p /var/www/mgsv_server/wsgi-scripts/mgsv_emulator \
    && mkdir -p /var/www/mgsv_server/logs \
    && mkdir -p /var/www/mgsv_server/www/tppstmweb/eula \
    && touch /var/www/mgsv_server/logs/app.log /var/www/mgsv_server/logs/access.log /var/www/mgsv_server/logs/error.log
COPY [ "emulator", "/var/www/mgsv_server/wsgi-scripts/mgsv_emulator/emulator" ]
COPY myapp.wsgi /var/www/mgsv_server/wsgi-scripts
COPY mgs_server.conf /etc/apache2/sites-available/
COPY static_key.bin /var/www/mgsv_server/
COPY eula.var /var/www/mgsv_server/www/tppstmweb/eula
COPY database.py /var/www/mgsv_server/wsgi-scripts
COPY entrypoint.sh /entrypoint.sh
RUN a2ensite mgs_server \
	&& a2dissite 000-default \
	&& chmod +x /entrypoint.sh \
	&& rm /percona-release_0.1-5.stretch_all.deb
EXPOSE 80
CMD ["/entrypoint.sh"]