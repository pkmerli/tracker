from django.contrib import admin
from .models import Bug, Attachment, Entry


admin.site.register(Bug)
admin.site.register(Entry)
admin.site.register(Attachment)

