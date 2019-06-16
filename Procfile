release: python manage.py makemigrations pdfmerge --noinput && python manage.py migrate --noinput
web: gunicorn pdfmerge.wsgi
