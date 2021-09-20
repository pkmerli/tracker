from django.db import models
from settings.models import TD_Priority, TD_Status


class ToDo(models.Model):
    name = models.CharField(max_length=55, null=False)
    priority = models.ForeignKey(TD_Priority, on_delete=models.CASCADE)
    description = models.TextField(max_length=275, null=True, blank=True)
    status = models.ForeignKey(TD_Status, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    objects = models.Manager()

    def __str__(self):
        return self.name


class Attachment(models.Model):
    file_name = models.CharField(max_length=125, null=False)
    file = models.FileField(upload_to='attachments/', max_length=500, null=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    attached_to = models.ForeignKey(ToDo, related_name='entity', on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return self.file_name

