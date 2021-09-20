from django.db import models


class KBQuerySet(models.query.QuerySet):
    def get_by_name(self, name):
        return self.filter(name=name)

    def get_by_type(self, type):
        return self.filter(type=type)

    def order_by_created(self):
        return self.order_by('created_at')

    def order_by_updated(self):
        return self.order_by('updated_at')


class KBManger(models.Manager):
    def get_queryset(self):
        return KBQuerySet(self.model, using=self._db)

    def get_by_name(self, name):
        return self.get_queryset().get_by_name(name)

    def get_by_type(self, type):
        return self.get_queryset().get_by_type(type)

    def order_by_created(self):
        return self.get_queryset().order_by_created()

    def order_by_updated(self):
        return self.get_queryset().order_by_updated()


class AttachmentQuerySets(models.query.QuerySet):
    def get_by_name(self, file_name):
        return self.filter(file_name=file_name)

    def get_by_attached_to(self, attached_to):
        return self.filter(attached_to=attached_to)

    def get_by_attached_pk(self, pk):
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

    def get_by_attached_id(self, pk):
        return self.get_queryset().get_by_attached_pk(pk)

    def order_by_upload(self):
        return self.get_queryset().order_by_upload()

