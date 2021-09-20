from django.db import models
from .managers import BugManager, EntryManager, AttachmentManager
from settings.models import Bug_Status, Bug_Category, Bug_Priority


class Bug(models.Model):
    name = models.CharField(max_length=50, null=False)
    priority = models.ForeignKey(Bug_Priority, on_delete=models.CASCADE)
    description = models.TextField(max_length=275, null=True, blank=True)
    status = models.ForeignKey(Bug_Status, on_delete=models.CASCADE)
    category = models.ForeignKey(Bug_Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    objects = BugManager()

    def __str__(self):
        return self.name


class Entry(models.Model):
    notes = models.TextField(max_length=550, null=True, blank=True)
    entry_for = models.ForeignKey(Bug, related_name="noted_on", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = EntryManager()

    def __str__(self):
        return self.notes


class Attachment(models.Model):
    file_name = models.CharField(max_length=125, null=False)
    file = models.FileField(upload_to='attachments', max_length=500, null=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    attached_to = models.ForeignKey(Bug, related_name='entity', on_delete=models.CASCADE)

    objects = AttachmentManager()

    def __str__(self):
        return self.file_name
