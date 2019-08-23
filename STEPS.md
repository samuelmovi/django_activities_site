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
- Create app: `python manage.py startapp site`
- Add `'sevilla.apps.SiteConfig',` to `INSTALLED_APPS` in settings.py
- Kill the db container if still running: `sudo docker stop django-db`
- Start web app with `./init.sh` (make executable with `chmod +x init.sh`)
- In `django_activities_site/urls.py` add `path('', include('site.urls')),` to urlpatterns

## MODELS
- Populate models in `site/models.py`

- Make migrations:
```bash
python manage.py makemigrations sevilla
python manage.py migrate

```
- Make models available to admin user, edit sevilla/admin.py
```pythonstub
from .models import *

admin.site.register(Page)
admin.site.register(Experience)
admin.site.register(Contact)

```

## VIEWS
- Create views:
```pythonstub
from django.views import View

def home(request):
	pass

class PageView(View):
    def get(self, request):
        pass


class ExperienceView(View):
    def get(self, request):
        pass

```
- Create file `sevilla/urls.py`:
```pythonstub
from django.urls import path
from . import views

app_name = 'sevilla'
urlpatterns = [
	path('', views.home, name='home'),
    path('experience/<path:experience.name>/', views.ExperienceView.as_view(), name='experience'),
    path('<path:page.name>/', views.PageView.as_view(), name='page'),
]

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



