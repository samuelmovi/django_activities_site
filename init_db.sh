echo '[#] Starting MySQL database container: django-db...'
sudo docker run --rm --name django-db -e MYSQL_ROOT_PASSWORD=mysecretpassword -v $PWD/db:/var/lib/mysql -d mariadb

echo '[#] Waiting 6 seconds for DB initialization...'
sleep 6

echo '[#] Starting virtual environment...'
source ~/py3venv/bin/activate

echo '[#] Starting Django development server...'
python manage.py runserver 0.0.0.0:8000
