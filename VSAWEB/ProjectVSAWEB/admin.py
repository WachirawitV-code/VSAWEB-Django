from django.contrib import admin
from .models import Images,MarkImages,SavedEmbeds

# Register your models here.

admin.site.register(Images)
admin.site.register(MarkImages)
admin.site.register(SavedEmbeds)
