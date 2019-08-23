from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Page)
admin.site.register(Activity)
admin.site.register(Contact)
admin.site.register(CarouselPhoto)
admin.site.register(Excerpt)
