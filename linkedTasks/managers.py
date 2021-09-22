from django.db import models
from django.apps import apps


class LinkedTaskQuerySet(models.query.QuerySet):
    def get_by_title(self, title):
        return self.filter(title=title)

    def get_by_category(self, category):
        return self.filter(category=category)

    def get_by_status(self, status):
        return self.filter(status=status)

    def active(self):
        return self.filter(active=True)

    def order_by_status(self):
        return self.order_by('status')

    def order_by_created_at(self):
        return self.order_by('created_at')


class LinkedTaskManager(models.Manager):
    def get_queryset(self):
        return LinkedTaskQuerySet(self.model, using=self._db)

    def get_by_title(self, title):
        return self.get_queryset().get_by_title(title)

    def get_by_category(self, category):
        return self.get_queryset().get_by_category(category)

    def get_by_status(self, status):
        return self.get_queryset().get_by_status(status)

    def active(self):
        return self.get_queryset().active()

    def order_by_status(self):
        return self.get_queryset().order_by_status()

    def order_by_created_at(self):
        return self.get_queryset().order_by_created_at()


class TaskQuerySet(models.query.QuerySet):
    def get_by_name(self, name):
        return self.filter(name=name)

    def get_by_linked_to(self, linked_to):
        return self.filter(linked_to=linked_to)

    def get_related_by_pk(self, pk):
        return self.filter(linked_to__pk=pk)

    def active(self):
        return self.filter(active=True)

    def order_by_rank(self):
        return self.order_by('rank')

    def order_by_status(self):
        return self.order_by('status')


class TaskManager(models.Manager):
    def get_queryset(self):
        return TaskQuerySet(self.model, using=self._db)

    def get_by_name(self, name):
        return self.get_queryset().get_by_name(name)

    def get_by_linked_to(self, linked_to):
        return self.get_queryset().get_by_linked_to(linked_to)

    def get_by_related_pk(self, pk):
        return self.get_queryset().get_related_by_pk(pk)

    def active(self):
        return self.get_queryset().active()

    def order_by_rank(self):
        return self.get_queryset().order_by_rank()

    def order_by_status(self):
        return self.get_queryset().order_by_status()


class EntryQuerySet(models.query.QuerySet):
    def get_by_entry_for(self, entry_for):
        return self.filter(entry_for=entry_for)

    def get_related_by_pk(self, pk):
        return self.filter(entry_for__pk=pk)

    def order_by_created_at(self):
        return self.order_by('created_at')


class EntryManager(models.Manager):
    def get_queryset(self):
        return EntryQuerySet(self.model, using=self._db)

    def get_by_entry_for(self, entry_for):
        return self.get_queryset().get_by_entry_for(entry_for)

    def get_related_by_pk(self, pk):
        return self.get_queryset().get_related_by_pk(pk)

    def order_by_created_at(self):
        return self.get_queryset().order_by_created_at()


class AttachmentQuerySet(models.query.QuerySet):
    def get_by_name(self, file_name):
        return self.filter(file_name=file_name)

    def get_by_attached(self, attached_to):
        return self.filter(attached_to=attached_to)

    def get_related_by_pk(self, pk):
        return self.filter(attached_to__pk=pk)

    def order_by_upload(self):
        return self.order_by('uploaded_at')


class AttachmentManager(models.Manager):
    def get_queryset(self):
        return AttachmentQuerySet(self.model, using=self._db)

    def get_by_name(self, file_name):
        return self.get_queryset().get_by_name(file_name)

    def get_by_attached(self, attached_to):
        return self.get_queryset().get_by_attached(attached_to)

    def get_by_related_pk(self, pk):
        return self.get_queryset().get_related_by_pk(pk)

    def order_by_upload(self):
        return self.get_queryset().order_by_upload()
