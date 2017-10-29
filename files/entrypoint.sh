#!/bin/bash
service mysql start && sleep 3; mysql -h localhost -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123'; FLUSH PRIVILEGES;" && mysql -u root -h localhost -p123 < /database.sql && rm /database.sql
apachectl -DFOREGROUND
