from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from model_utils import FieldTracker
from . import jalali
#TODO: Do some improvments on django.admin
#TODO: Add Profile Photo field for users to show it in their panel.

# Create your models here.
class Category(models.Model):
    Title = models.CharField(max_length=250, verbose_name="عنوان")

    def Meta(self):

        verbose_name = "عنوان"
        verbose_name_plural = "عنوان ها"

    def __str__(self):
        return self.Title

class Todo(models.Model):

    last_time_edited = models.DateTimeField(verbose_name='آخرین تغییرات')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="نویسنده", related_name='events')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="دسته", related_name='events')
    Eventname = models.CharField(max_length=500, verbose_name="نام رخداد")
    Description = models.TextField(verbose_name="توضیحات")
    CreateDatetime = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    Attachments = models.FileField(upload_to='media', blank=True, verbose_name="پیوست")
    event_datetime = models.DateTimeField(blank=True, null=True)
    optional = models.BooleanField(blank=True, null=True, verbose_name="اختیاری است؟")
    slug = models.SlugField(unique=True, null=True)
    tracker = FieldTracker()

    def Meta(self):
        ordering = ['CreateDatetime', 'event_datetime']

    def __str__(self):
        return self.Eventname

    def save(self, *args, **kwargs):

        if self.tracker.changed is not None:
            self.last_time_edited = datetime.now()
            super(Todo, self).save(*args, **kwargs)

