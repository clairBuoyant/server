#! /usr/bin/env sh

echo "Running inside /server/prestart.sh, you could add migrations to this file"

echo "
#!/bin/sh
# Let the DB start
sleep 10;
# Run migrations
alembic upgrade head
"
