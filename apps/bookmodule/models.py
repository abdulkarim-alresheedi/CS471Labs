from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1)


class Address(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city



class Card(models.Model):
    card_number = models.IntegerField()


class Department(models.Model):
    name = models.CharField(max_length=100)



class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.IntegerField()


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    card = models.OneToOneField(Card, on_delete=models.PROTECT,null = True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null = True)
    course = models.ManyToManyField('Course')


class Address2(models.Model):
    city = models.CharField(max_length=100)
    def __str__(self):
        return self.city

class Student2(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    addresses = models.ManyToManyField(Address2)


class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.title
