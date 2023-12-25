web: gunicorn --bind :8000 --workers 3 --threads 5 myproject.wsgi:application
websocket: daphne -b 0.0.0.0 -p 5000 myproject.asgi:application