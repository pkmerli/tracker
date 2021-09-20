from django.contrib import admin
from .models import ToDo, Attachment

# Register your models here.
admin.site.register(ToDo)
admin.site.register(Attachment)
