from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    Title = models.CharField(max_length=250, verbose_name="عنوان")

    def Meta(self):

        verbose_name = "عنوان"
        verbose_name_plural = "عنوان ها"

    def __str__(self):
        return self.Title


class Todo(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="نویسنده")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="دسته")
    Eventname = models.CharField(max_length=500 , verbose_name="نام رخداد")
    Description = models.TextField(verbose_name="توضیحات")
    CreateDatetime = models.DateTimeField(default=datetime.now(), verbose_name="تاریخ ایجاد")
    Attachments = models.FileField(upload_to='media', blank=True, verbose_name="پیوست")
    event_datetime = models.DateTimeField(blank=True, null=True)
    optional = models.BooleanField(blank=True, null=True, verbose_name="اختیاری است؟")
    slug = models.SlugField(unique=True, null=True)

    def Meta(self):
        ordering = ['CreateDatetime', 'event_datetime']

    def __str__(self):
        return self.Eventname
