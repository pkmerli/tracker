from django.db import models
from settings.models import KB_Type


class KB_Entry(models.Model):
    name = models.CharField(max_length=50, null=False)
    type = models.ForeignKey(KB_Type, on_delete=models.CASCADE)
    notes = models.TextField(max_length=575, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.name


class Attachment(models.Model):
    file_name = models.CharField(max_length=125, null=False)
    file = models.FileField(upload_to='attachments', max_length=500, null=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    attached_to = models.ForeignKey(KB_Entry, related_name='entity', on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return self.file_name

