from django.db import models


class BugPriorityQuerySet(models.query.QuerySet):
    def get_by_priority(self, priority):
        return self.filter(priority=priority)

    def list_priority(self):
        return self.all()

    def get_by_pk(self, pk):
        return self.filter(pk=pk)

    def order_by_created(self):
        return self.order_by('created_at')

    def order_by_update(self):
        return self.order_by('updated_at')


class BugPriorityManager(models.Manager):
    def get_queryset(self):
        return BugPriorityQuerySet(self.model, using=self._db)

    def get_by_priority(self, priority):
        return self.get_queryset().get_by_priority(priority)

    def list(self):
        return self.get_queryset().list_priority()

    def pk(self, pk):
        return self.get_queryset().get_by_pk(pk)

    def order_by_created(self):
        return self.get_queryset().order_by_created()

    def order_by_update(self):
        return self.get_queryset().order_by_update()


class BugStatusQuerySet(models.query.QuerySet):
    def get_by_status(self, status):
        return self.filter(status=status)

    def list_status(self):
        return self.all()

    def get_by_pk(self, pk):
        return self.filter(pk=pk)

    def get_completed(self):
        return self.filter(is_completed=True)

    def get_noncompleted(self):
        return self.filter(is_completed=False)

    def order_by_created(self):
        return self.order_by('created_at')

    def order_by_update(self):
        return self.order_by('updated_at')


class BugStatusManager(models.Manager):
    def get_queryset(self):
        return BugStatusQuerySet(self.model, using=self._db)

    def get_by_status(self, status):
        return self.get_queryset().get_by_status(status)

    def list(self):
        return self.get_queryset().list_status()

    def pk(self, pk):
        return self.get_queryset().get_by_pk(pk)

    def completed(self):
        return self.get_queryset().get_completed()

    def open(self):
        return self.get_queryset().get_noncompleted()

    def order_by_created(self):
        return self.get_queryset().order_by_created()

    def order_by_update(self):
        return self.get_queryset().order_by_update()


class BugCategoryQuerySet(models.query.QuerySet):
    def get_by_category(self, category):
        return self.filter(category=category)

    def list_categories(self):
        return self.all()

    def get_by_pk(self, pk):
        return self.filter(pk=pk)

    def order_by_category(self):
        return self.order_by('category')

    def order_by_created(self):
        return self.order_by('created_at')

    def order_by_update(self):
        return self.order_by('updated_at')


class BugCategoryManager(models.Manager):
    def get_queryset(self):
        return BugCategoryQuerySet(self.model, using=self._db)

    def get_category(self, category):
        return self.get_queryset().get_by_category(category)

    def list(self):
        return self.get_queryset().list_categories()

    def pk(self, pk):
        return self.get_queryset().get_by_pk(pk)

    def order_alpabetically(self):
        return self.get_queryset().order_by_category()

    def order_by_created(self):
        return self.get_queryset().order_by_created()

    def order_by_update(self):
        return self.get_queryset().order_by_update()

