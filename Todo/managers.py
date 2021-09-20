from django.db import models
from django.apps import apps


class ToDoQuerySet(models.query.QuerySet):
    def get_by_name(self, name):
        return self.filter(name=name)

    def get_by_priority(self, priority):
        return self.filter(priority=priority)

    def get_by_status(self, status):
        return self.filter(status=status)

    def active(self):
        return self.filter(active=True)

    def order_by_created(self):
        return self.order_by('created_at')

    def order_by_updated(self):
        return self.order_by('updated_at')


class ToDoManager(models.Manager):
    def get_queryset(self):
        return ToDoQuerySet(self.model, using=self._db)

    def get_by_name(self, name):
        return self.get_queryset().get_by_name(name)

    def get_by_priority(self, priority):
        return self.get_queryset().get_by_priority(priority)

    def get_by_status(self, status):
        return self.get_queryset().get_by_status(status)

    def active(self):
        return self.get_queryset().active()

    def order_by_created(self):
        return self.get_queryset().order_by_created()

    def order_by_upload(self):
        return self.get_queryset().order_by_updated()
