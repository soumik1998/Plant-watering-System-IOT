from django.db import models
from datetime import datetime

'''This is a user model. It stores detail of user.'''


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=255, blank=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

'''This is a Plant model. It stores details of a plant.'''


class Plants(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    plant_name = models.CharField(max_length=100, blank=True)
    lat = models.FloatField(default=0.0)
    lon = models.FloatField(default=0.0)
    dt = models.DateTimeField(default=datetime.now(),)

    def __str__(self):
        return str(self.plant_name)

'''This is a temperature model. It stores temperature values of temperature sensor.'''


class Temp(models.Model):
    pid = models.ForeignKey(Plants, on_delete=models.CASCADE)
    temp = models.CharField(max_length=20)
    dt = models.DateTimeField(default=datetime.now(),)

    def __str__(self):
        return str(self.temp)

'''This is a water model. It stores water level values in water tank'''


class Water(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.CharField(max_length=5)
    dt = models.DateTimeField(default=datetime.now(),)

    def __str__(self):
        return str(self.level)

'''This is a soil model. It stores soil moisture values of soil moisture sensor.'''


class Soil(models.Model):
    pid = models.ForeignKey(Plants, on_delete=models.CASCADE)
    m_level = models.CharField(max_length=5)
    dt = models.DateTimeField(default=datetime.now(),)

    def __str__(self):
        return str(self.m_level)

'''This is Rain model. It stores values of rain gauge.'''


class Rain(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    r_level = models.CharField(max_length=5)
    dt = models.DateTimeField(default=datetime.now(),)

    def __str__(self):
        return str(self.r_level)

'''This is an actuator model. It stores status of actuator whether it is on or off.'''


class Actuator(models.Model):
    pid = models.ForeignKey(Plants, on_delete=models.CASCADE)
    dt = models.DateTimeField(default=datetime.now(),)
    status = models.CharField(max_length=10)

    def __str__(self):
        return str(self.status)
