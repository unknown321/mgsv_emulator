#!/bin/bash
service mysql start
mysql < /var/www/mgsv_server/wsgi-scripts/mgsv_emulator/emulator/database.sql
apachectl -DFOREGROUND