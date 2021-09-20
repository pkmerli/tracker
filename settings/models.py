from django.db import models
from .managers import BugPriorityManager, BugStatusManager, BugCategoryManager


class Bug_Priority(models.Model):
    priority = models.CharField(max_length=25, null=False)
    sort_order = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BugPriorityManager()

    def __str__(self):
        return self.priority

    class Meta:
        ordering = ['sort_order']


class Bug_Status(models.Model):
    status = models.CharField(max_length=40, null=False)
    is_completed = models.BooleanField(default=False)
    sort_order = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BugStatusManager()

    def __str__(self):
        return self.status

    class Meta:
        ordering = ['sort_order']


class Bug_Category(models.Model):
    category = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BugCategoryManager()

    def __str__(self):
        return self.category


class TD_Priority(models.Model):
    priority = models.CharField(max_length=25, null=False)
    sort_order = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.priority

    class Meta:
        ordering = ['sort_order']


class TD_Status(models.Model):
    status = models.CharField(max_length=40, null=False)
    is_completed = models.BooleanField(default=False)
    sort_order = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.status

    class Meta:
        ordering = ['sort_order']


class LT_Category(models.Model):
    category = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.category


class LT_Status(models.Model):
    status = models.CharField(max_length=40, null=False)
    is_completed = models.BooleanField(default=False)
    sort_order = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.status

    class Meta:
        ordering = ['sort_order']


class T_Rank(models.Model):
    rank = models.CharField(max_length=40, null=False)
    sort_order = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.rank

    class Meta:
        ordering = ['sort_order']


class T_Status(models.Model):
    status = models.CharField(max_length=40, null=False)
    is_completed = models.BooleanField(default=False)
    sort_order = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.status

    class Meta:
        ordering = ['sort_order']


class KB_Type(models.Model):
    type = models.CharField(max_length=75, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.type

    class Meta:
        ordering = ['created_at']
