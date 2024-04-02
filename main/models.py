from django.db import models


class Administrator(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)

    def __str__(self):
        return self.username


class Info(models.Model):
    logo = models.ImageField(upload_to='logos/')
    address = models.CharField(max_length=250)
    tw = models.URLField()
    fb = models.URLField()
    insta = models.URLField()
    ln = models.URLField()


class MainBanner(models.Model):
    image = models.ImageField(upload_to='banners/')
    title = models.CharField(max_length=250)
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Service(models.Model):
    icon = models.ImageField(upload_to='icons/')
    title = models.CharField(max_length=250)
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class About(models.Model):
    photo = models.ImageField(upload_to='photos/')
    text1 = models.TextField()
    text2 = models.TextField()


class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')


class Testimonial(models.Model):
    review = models.TextField(max_length=250)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Client(models.Model):
    logo = models.ImageField(upload_to='clients/')


class Message(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.first_name

