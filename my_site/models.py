from django.db import models


# Create your models here.


class Page(models.Model):
    ENGLISH = 'en'
    SPANISH = 'es'
    
    LANGUAGES = (
        (ENGLISH, 'en'),
        (SPANISH, 'es'),
    )
    
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1500)
    lang = models.CharField(max_length=10, choices=LANGUAGES)
    
    def __str__(self):
        return "[{}] {}".format(self.lang, self.name)


class Activity(models.Model):
    FLAMENCO = 'Flamenco'
    TRIANA = 'Triana'
    CRAFTS = 'Crafts'
    ARTESANIA = 'Artesania'
    SPECIALTIES = 'Specialties'
    ESPECIALIDADES = 'Especialidades'
    
    CHOICES = (
        (FLAMENCO, 'Flamenco'),
        (TRIANA, 'Triana'),
        (CRAFTS, 'Cratfs'),
        (ARTESANIA, 'Artesania'),
        (SPECIALTIES, 'Specialties'),
        (ESPECIALIDADES, 'Especialidades'),
    )
    
    ENGLISH = 'en'
    SPANISH = 'es'
    
    LANGUAGES = (
        (ENGLISH, 'en'),
        (SPANISH, 'es'),
    )
    
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=CHOICES)
    summary = models.TextField(max_length=1500)
    details = models.TextField(max_length=500)
    lang = models.CharField(max_length=10, choices=LANGUAGES)
    
    def __str__(self):
        return '[{}] {}/{}'.format(self.lang, self.type, self.name)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class CarouselPhoto(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    activity = models.ForeignKey(Activity, on_delete=models.DO_NOTHING, null=True, blank=True)
    page = models.ForeignKey(Page, on_delete=models.DO_NOTHING, null=True, blank=True)
    
    def __str__(self):
        if self.activity is None:
            return '{}/{}'.format(self.page, self.name)
        else:
            return '{}/{}'.format(self.activity, self.name)


class Excerpt(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    image = models.ImageField(null=True, blank=True)
    link = models.CharField(max_length=100)
    
    ENGLISH = 'en'
    SPANISH = 'es'
    
    LANGUAGES = (
        (ENGLISH, 'en'),
        (SPANISH, 'es'),
    )
    lang = models.CharField(max_length=10, choices=LANGUAGES)
    
    def __str__(self):
        return "[{}] {}".format(self.lang, self.name)
