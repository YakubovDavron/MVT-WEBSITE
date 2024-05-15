from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=212)
    email = models.EmailField()
    subject = models.CharField(max_length=212)
    message = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=212)
    content = models.TextField()
    image = models.ImageField(upload_to="team")

    def __str__(self):
        return self.title


class Clients(models.Model):
    name = models.CharField(max_length=212)
    image = models.ImageField(upload_to="Clients")
    profession = models.CharField(max_length=212)
    content = models.TextField()

    def __str__(self):
        return self.name
