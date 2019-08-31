# DJANGO ACTIVITIES SITE

## PROJECT SETUP
- Create project: `django-admin startproject django_activities_site`
- Create database foder `db/` and execute:
```bash
docker run --rm --name django-db -e POSTGRES_PASSWORD=mysecretpassword -v $PWD/db:/var/lib/postgresql/data -d postgres:alpine
sudo apt install postgresql-client
psql -h 172.17.0.2 -U postgres
create database activities_site;
exit
```
- Set up postgres database in `settings.py`:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'activities_site',
        'HOST': '172.17.0.2',
        'USER': 'postgres',
        'PASSWORD': 'mysecretpassword',
    }
}
```
- Update database to accommodate changes made: `python manage.py migrate`
- Create admin user: `python manage.py createsuperuser`

## APP SETUP
- Create app: `python manage.py startapp my_site`
- Add `'my_site.apps.MySiteConfig',` to `INSTALLED_APPS` in settings.py
- Create file `my_site/urls.py`
- In `django_activities_site/urls.py` add `path('', include('my_site.urls')),` to urlpatterns

## MODELS
- Populate models in `my_site/models.py`

- Make models available to admin user, edit `my_site/admin.py`
```pythonstub
from .models import *

admin.site.register(Page)
admin.site.register(Activity)
admin.site.register(Contact)
admin.site.register(CarouselPhoto)
admin.site.register(Excerpt)

```

## FORMS
Create and populate `my_site/forms.py`


## VIEWS
- Populate `my_site/views.py`
- Populate `my_site/urls.py`

## MIGRATION
Now that models views, and urls are populated:
```bash
python manage.py makemigrations my_site
python manage.py migrate

```

## TEMPLATES
- In `my_site/` create folder `templates/my_site/` and add emplate files

## STATIC FILES
- In `my_site/` create folder `static/my_site/`

## MEDIA FILES
- create folder for media files `media/`
- Add to `settings.py`:
```
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```
- Append  to the end of urlpatterns in `project_name/urls.py`:
```
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [ ... ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## INITIALIZE
Stop the database container if still running (`sudo docker stop django-db`), and execute `./init.sh`

## TRANSLATION
- In folder `my_site/`, create `locale/`
- Add `django.middleware.locale.LocaleMiddleware` to MIDDLEWARE in `settings.py`
- Add `LOCALE_PATHS = (os.path.join(BASE_DIR, 'my_site/locale/'),)` to MIDDLEWARE in `settings.py`
- From `my_site/` run: `django-admin makemessages -l es` [install gettext if required]
- execute `python manage.py compilemessages`

## FEEDER
The way the app is set up, you will be redirected to an error page on first run. To avoid this you need home pages (`/home/` and `/inicio/`).
Instead of using the admin interface, feel free to use my feeder script. It has custom dictionaries to automatically 
add entries to the database.

To use it:
```
python manage.py shell

import feeder

```

This should execute the code in it, and populate the fields. Feel free to modify it for your own use.



