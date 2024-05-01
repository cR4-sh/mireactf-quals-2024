#!/bin/bash
/usr/lib/postgresql/13/bin/postgres -D /var/lib/postgresql/13/main -c config_file=/etc/postgresql/13/main/postgresql.conf &
PGPASSWORD=root createuser --username=postgres --superuser root
psql -X --file=/docker-entrypoint-initdb.d/database.sql
