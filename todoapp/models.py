from django.db import models

# Create your models here.
class User(models.Model):

    Fullname = models.CharField(max_length = 255)
    Nickname = models.CharField(max_length = 255,primary_key = True)
    Birthdate = models.DateField()

    def __str__(self):
        return self.Fullname

class Todo(models.Model):
    EventOwner = models.ForeignKey(User, on_delete = models.CASCADE)
    #Piority = models.CharField(max_length = 20,blank = True)
    Title = models.CharField(max_length = 500)
    Description = models.TextField()
    Datetime = models.DateTimeField(auto_now_add = True)
    Attachments = models.FileField(blank = True)

    def __str__(self):
        return self.Title