from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Boat(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    displacement = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000)])
    data_create = models.DateField()

class Positions(models.Model):
    name = models.CharField(max_length=50)

class Person(models.Model):
    name = models.CharField(max_length=40)
    addres = models.CharField(max_length=50)
    position = models.ForeignKey(Positions, on_delete=models.CASCADE)

class PlaceFishing(models.Model):
    name = models.CharField(max_length=50)
    discriptions = models.TextField()

class Ban(models.Model):
    exit_date = models.DateTimeField()
    return_date = models.DateTimeField()
    place = models.ForeignKey(PlaceFishing, on_delete=models.CASCADE)
    quality = models.CharField(max_length=10)

class Catch(models.Model):
    name_fish = models.CharField(max_length=40)
    weight = models.IntegerField()

class Flight(models.Model):
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE)
    crew = models.ManyToManyField(Person, through='FlightHasPerson')
    bans = models.ManyToManyField(Ban, through='FlightHasBan')
    catch = models.ManyToManyField(Catch, through='FlightHasCatch')
    exit_date = models.DateTimeField()
    return_date = models.DateTimeField()

class FlightHasPerson(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

class FlightHasBan(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    ban = models.ForeignKey(Ban, on_delete=models.CASCADE)

class FlightHasCatch(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    catch = models.ForeignKey(Catch, on_delete=models.CASCADE)