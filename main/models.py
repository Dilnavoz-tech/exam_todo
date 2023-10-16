from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()

class Todo(models.Model):
    ID = models.IntegerField()
    text = models.TextField()
    expires_at = models.DateTimeField()
    owner =  models.ForeignKey(User, on_delete=models.CASCADE)


    def create(self, validated_data):
        print(validated_data)
        return super().save(**validated_data)

    class Meta:
        verbose_name = _('Todo')
        verbose_name_plural = _('Todos')


class List(models.Model):
    work = models.TextField()
    work2 = models.ForeignKey(Todo, on_delete=models.CASCADE)
