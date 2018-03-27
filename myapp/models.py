from adminsortable.models import SortableMixin
from django.db import models


class Test(models.Model):
    test_name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.test_name


class Page(SortableMixin, models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    position = models.PositiveIntegerField(default=0, db_index=True, editable=False)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return '-'


class Question(models.Model):
    question = models.CharField(max_length=50)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    choice_score = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text