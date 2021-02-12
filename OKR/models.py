from django.contrib.auth.models import User
from django.db import models


class Objective(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    objective = models.CharField(max_length=40)

    def __str__(self):
        return self.objective

    class Meta:
        verbose_name = "Objective"
        verbose_name_plural = "Objectives"


class KR(models.Model):
    objective = models.ForeignKey(Objective, on_delete=models.CASCADE)
    key_result = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.objective}'

    class Meta:
        verbose_name = "Key Result"
        verbose_name_plural = "Key Results"


class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    objective = models.ForeignKey(Objective, on_delete=models.SET_NULL, blank=True, null=True)
    key_result = models.ForeignKey(KR, on_delete=models.SET_NULL, blank=True, null=True)
    percentage = models.IntegerField(help_text="What is the completion percentage",default=0)
    update = models.TextField(help_text="Brief description on the progress")
    time_spent = models.TimeField(help_text="Time spent on the task")

    def __str__(self):
        return f'{self.user}-{self.date_time}'

    class Meta:
        verbose_name = "Entry"
        verbose_name_plural = "Entries"