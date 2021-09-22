from django.db import models
from settings.models import T_Rank, T_Status, LT_Status, LT_Category


class LinkedTasks(models.Model):
    title = models.CharField(max_length=50, null=False)
    summary = models.TextField(max_length=500, null=True, blank=True)
    category = models.ForeignKey(LT_Category, on_delete=models.CASCADE)
    status = models.ForeignKey(LT_Status, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    objects = models.Manager()

    def __str__(self):
        return self.title


class Task(models.Model):
    name = models.CharField(max_length=50, null=False)
    linked_to = models.ForeignKey(LinkedTasks, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, null=False)
    description = models.TextField(max_length=275, null=True, blank=True)
    rank = models.ForeignKey(T_Rank, on_delete=models.CASCADE)
    status = models.ForeignKey(T_Status, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['rank']


class Entry(models.Model):
    notes = models.TextField(max_length=550, null=True, blank=True)
    entry_for = models.ForeignKey(Task, related_name="noted_on", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.notes


class Attachment(models.Model):
    file_name = models.CharField(max_length=125, null=False)
    file = models.FileField(upload_to='attachments', max_length=500, null=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    attached_to = models.ForeignKey(LinkedTasks, related_name='entity', on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return self.file_name
