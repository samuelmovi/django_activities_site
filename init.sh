echo '[#] Starting PostgreSQL database container: django-db...'
sudo docker run --rm --name django-db -e POSTGRES_PASSWORD=mysecretpassword -v $PWD/db:/var/lib/postgresql/data -d postgres:alpine

echo '[#] Waiting 5 seconds for DB initialization...'
sleep 5

echo '[#] Starting virtual environment...'
source ~/py3venv/bin/activate

echo '[#] Starting Django development server...'
python manage.py runserver 0.0.0.0:8000
