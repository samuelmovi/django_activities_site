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
- In `sevilla/` create folder `templates/sevilla/` and add emplate files

## STATIC FILES
- In `sevilla/` create folder `static/sevilla/`

## TRANSLATION
- In folder `sevilla/`, create `locale/`
- Add `django.middleware.locale.LocaleMiddleware` to MIDDLEWARE in `settings.py`
- Add `LOCALE_PATHS = (os.path.join(BASE_DIR, 'sevilla/locale/'),)` to MIDDLEWARE in `settings.py`
- From `sevilla/` run: `django-admin makemessages -l es` [install gettext if required]
- execute `python manage.py compilemessages`


## MIGRATION to IONOS
- 



