from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
import logging
from django.utils.translation import ugettext_lazy as _

from .models import *
from .forms import ContactForm

# Create your views here

logger = logging.getLogger(__name__)


def base(request):
    try:
        if request.method == 'GET':
            if request.META['HTTP_ACCEPT_LANGUAGE'].startswith('es'):
                return redirect('/inicio/')
            else:
                return redirect('/home/')
        else:
            return redirect('/')
    except Exception as e:
        logger.exception(e)
        return redirect('/error/')


class PageView(View):
    all_contacts = Contact.objects.all()
    # loading EN info
    all_pages_EN = Page.objects.filter(lang='en')
    all_activities_EN = Activity.objects.filter(lang='en')
    activity_types_EN = all_activities_EN.values('type').distinct()
    # loading ES info
    all_pages_ES = Page.objects.filter(lang='es')
    all_activities_ES = Activity.objects.filter(lang='es')
    activity_types_ES = all_activities_ES.values('type').distinct()
    
    cards_ES = [
        'Flamenco en Grupo para Principiantes',
        "Lección Privada de Flamenco",
        "Espectáculo Flamenco Privado",
        "Tour de Tapas Privado",
        "Tour Privado de Triana",
        "Experiencia Hecha a Medida",
    ]
    cards_EN = [
        'Group Lessons For Beginners',
        "Private Flamenco Lesson",
        "Private Show",
        "Tapas Tour",
        "Local Tour",
        "Custom Tour",
    ]
    cards = []
    
    def get(self, request, name):
        print("[#] Loading requested page: {}".format(name))
        try:
            if request.META['HTTP_ACCEPT_LANGUAGE'].startswith('es'):
                # print("[#] All activities ES: {}".format(len(self.all_activities_ES)))
                page = self.all_pages_ES.get(name=name)
                all_photos = CarouselPhoto.objects.filter(activity=page.id)
                context = {
                    'page_title': page.title,
                    'all_contacts': self.all_contacts,
                    'all_photos': all_photos,
                    'activity_types': self.activity_types_ES,
                    'all_activities': self.all_activities_ES,
                    'all_pages': self.all_pages_ES,
                    'page': page,
                }
                self.cards = self.cards_ES
            else:
                # print("[#] All activities EN: {}".format(len(self.all_activities_EN)))
                page = self.all_pages_EN.get(name=name)
                all_photos = CarouselPhoto.objects.filter(activity=page.id)
                context = {
                    'page_title': page.title,
                    'all_contacts': self.all_contacts,
                    'all_photos': all_photos,
                    'activity_types': self.activity_types_EN,
                    'all_activities': self.all_activities_EN,
                    'all_pages': self.all_pages_EN,
                    'page': page,
                }
                self.cards = self.cards_EN
            context['footer_form'] = ContactForm()
            context['home'] = False
            if name in ('home', 'inicio'):
                context['home'] = True
                excerpts = Excerpt.objects.filter(name__in=self.cards)
                print("\t> Excerpts: {}".format(len(excerpts)))
                context['excerpts'] = excerpts
            # print("[#] Activities: {}".format(len(context['all_activities'])))
            # print("[#] Pages: {}".format(len(context['all_pages'])))
            return render(request, 'my_site/page.html', context)
        except Exception as e:
            logger.exception(e)
            return redirect('/error/')


class ActivityView(View):
    global logger
    all_contacts = Contact.objects.all()
    # loading EN info
    all_pages_EN = Page.objects.filter(lang='en')
    all_activities_EN = Activity.objects.filter(lang='en')
    activity_types_EN = all_activities_EN.values('type').distinct()
    # loading ES info
    all_pages_ES = Page.objects.filter(lang='es')
    all_activities_ES = Activity.objects.filter(lang='es')
    activity_types_ES = all_activities_ES.values('type').distinct()
    
    def get(self, request, lang, type, name):
        try:
            if lang == 'es':
                logger.info("[#] Loading: {}/{}/{}".format(lang, type, name))
                print("[#] Loading: {}/{}/{}".format(lang, type, name))
                activity = self.all_activities_ES.get(type=type, name=name)
                all_photos = CarouselPhoto.objects.filter(activity=activity.id)
                context = {
                    'page_title': activity.title,
                    'all_contacts': self.all_contacts,
                    'all_photos': all_photos,
                    'activity_types': self.activity_types_ES,
                    'all_activities': self.all_activities_ES,
                    'activity': activity,
                    'all_pages': self.all_pages_ES,
                }
            else:
                logger.info("[#] Loading: {}/{}/{}".format(lang, type, name))
                print("[#] Loading: {}/{}/{}".format(lang, type, name))
                activity = self.all_activities_EN.get(type=type, name=name)
                all_photos = CarouselPhoto.objects.filter(activity=activity.id)
                context = {
                    'page_title': activity.title,
                    'all_contacts': self.all_contacts,
                    'all_photos': all_photos,
                    'activity_types': self.activity_types_EN,
                    'all_activities': self.all_activities_EN,
                    'activity': activity,
                    'all_pages': self.all_pages_EN,
                }
            context['footer_form'] = ContactForm()
            return render(request, 'my_site/activity.html', context)
        except Exception as e:
            logger.exception(e)
            return redirect('/error/')


class ContactFormView(View):
    all_contacts = Contact.objects.all()
    # loading EN info
    all_pages_EN = Page.objects.filter(lang='en')
    all_activities_EN = Activity.objects.filter(lang='en')
    activity_types_EN = all_activities_EN.values('type').distinct()
    # loading ES info
    all_pages_ES = Page.objects.filter(lang='es')
    all_activities_ES = Activity.objects.filter(lang='es')
    activity_types_ES = all_activities_ES.values('type').distinct()
    
    def get(self, request):
        try:
            if request.META['HTTP_ACCEPT_LANGUAGE'].startswith('es'):
                context = {
                    'all_contacts': self.all_contacts,
                    # 'all_photos': self.all_photos,
                    'activity_types': self.activity_types_ES,
                    'all_activities': self.all_activities_ES,
                    'all_pages': self.all_pages_ES,
                }
            else:
                context = {
                    'all_contacts': self.all_contacts,
                    # 'all_photos': self.all_photos,
                    'activity_types': self.activity_types_EN,
                    'all_activities': self.all_activities_EN,
                    'all_pages': self.all_pages_EN,
                }
            form = ContactForm()
            context['form'] = form
            return render(request, 'my_site/contact.html', context)
        except Exception as e:
            logger.exception(e)
            return redirect('/error/')
    
    def post(self, request):
        try:
            form = ContactForm(request.POST)
            if form.is_valid():
                fields = ['name', 'email', 'arrival_date', 'party_size', 'reference']
                # print("[1] {}: {}".format(type(form.cleaned_data), form.cleaned_data))
                email_template = "<ul>"
                for field in fields:
                    email_template += "\n<li> {}: {}</li>".format(field, form.cleaned_data[field])
                    # print("> {}: {}".format(field, form.cleaned_data[field]))
                email_template += "\n</ul>"
                print(email_template)
                # send email here
                return redirect('/')
            else:
                return redirect('/contact/')
        except Exception as e:
            logger.exception(e)
            return redirect('/error/')


def error(request):
    if request.method == 'GET':
        return render(request, 'my_site/error.html')
    else:
        return redirect('/error/')
