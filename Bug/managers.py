from django.db import models


class BugQuerySet(models.query.QuerySet):
    def get_by_name(self, name):
        return self.filter(name=name)

    def get_by_pk(self, pk):
        return self.filter(pk=pk)

    def get_by_priority(self, priority):
        return self.filter(priority=priority)

    def get_by_status(self, status):
        return self.filter(status=status)

    def get_by_category(self, category):
        return self.filter(category=category)

    def order_by_priority(self):
        return self.order_by('priority')

    def order_by_status(self):
        return self.order_by('status')

    def active(self):
        return self.filter(active=True)


class BugManager(models.Manager):

    def get_queryset(self):
        return BugQuerySet(self.model, using=self._db)

    def get_by_name(self, name):
        return self.get_queryset().get_by_name(name)

    def get_by_pk(self, pk):
        return self.get_queryset().get_by_pk(pk)

    def get_by_priority(self, priority):
        return self.get_queryset().get_by_priority(priority)

    def get_by_status(self, status):
        return self.get_queryset().get_by_status(status)

    def get_by_category(self, category):
        return self.get_queryset().get_by_category(category)

    def active(self):
        return self.get_queryset().active()

    def order_by_priority(self):
        return self.get_queryset().order_by_priority()

    def order_by_status(self):
        return self.get_queryset().order_by_status()


class EntryQuerySets(models.query.QuerySet):

    def get_by_entry_for(self, entry_for):
        return self.filter(entry_for=entry_for)

    def get_by_relatedpk(self, pk):
        return self.filter(entry_for__pk=pk)

    def order_by_created_at(self):
        return self.order_by('created_at')


class EntryManager(models.Manager):
    def get_queryset(self):
        return EntryQuerySets(self.model, using=self._db)

    def get_by_entry_for(self, entry_for):
        return self.get_queryset().get_by_entry_for(entry_for)

    def get_by_related_pk(self, pk):
        return self.get_queryset().get_by_relatedpk(pk)

    def order_by_created_at(self):
        return self.get_queryset().order_by_created_at()


class AttachmentQuerySets(models.query.QuerySet):
    def get_by_name(self, file_name):
        return self.filter(file_name=file_name)

    def get_by_attached_to(self, attached_to):
        return self.filter(attached_to=attached_to)

    def get_by_relatedpk(self, pk):
        return self.filter(attached_to__pk=pk)

    def order_by_upload(self):
        return self.order_by('uploaded_at')


class AttachmentManager(models.Manager):
    def get_queryset(self):
        return AttachmentQuerySets(self.model, using=self._db)

    def get_by_name(self, file_name):
        return self.get_queryset().get_by_name(file_name)

    def get_by_attached_to(self, attached_to):
        return self.get_queryset().get_by_attached_to(attached_to)

    def get_by_related_pk(self, pk):
        return self.get_queryset().get_by_relatedpk(pk)

    def order_by_upload(self):
        return self.get_queryset().order_by_upload()







