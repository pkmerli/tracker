from django.contrib import admin
from .models import LinkedTasks, Task, Entry, Attachment

# Register your models here.
admin.site.register(LinkedTasks)
admin.site.register(Task)
admin.site.register(Entry)
admin.site.register(Attachment)
