#!/bin/sh

: << 'END'
until nc -z "${DB_HOST}" "${DB_PORT}";do
  echo "Ждём пока БД подымается"
  sleep 1
done
echo "✅ PostgreSQL доступен!"
END

set -e

echo "🧱 Applying database migrations..."
python manage.py migrate --noinput

echo "🎨 Collecting static files..."
python manage.py collectstatic --noinput

echo "Create SuperUser..."
python manage.py createsuperuser  --noinput || echo "Superuser already exists or could not be created"

echo "🚀 Starting server..."
exec "$@"
