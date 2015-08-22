from django.db import models

# Cars

class CarsType(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name



class Cars(models.Model):
    name = models.ForeignKey(CarsType)
    model = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.FileField(upload_to='cars_images')
    description = models.TextField()

    def __unicode__(self):
        return self.model


class Type_for_car(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Form_car(models.Model):
    type = models.ForeignKey(Type_for_car)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.FileField(upload_to='for_car')
    description = models.TextField()

    def __unicode__(self):
        return self.name


# Electronic

class ElectronicType(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Electronic(models.Model):
    name = models.ForeignKey(ElectronicType)
    model = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.FileField(upload_to='Electronic_images')
    description = models.TextField()

    def __unicode__(self):
        return self.model


# ForHome

class ForHomeType(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class ForHome(models.Model):
    name = models.ForeignKey(ForHomeType)
    model = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.FileField(upload_to='forHome_images')
    description = models.TextField()

    def __unicode__(self):
        return self.model

# Clothes

class ClothesType(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Clothes(models.Model):
    name = models.ForeignKey(ClothesType)
    model = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.FileField(upload_to='Clothes_images')
    description = models.TextField()

    def __unicode__(self):
        return self.model
