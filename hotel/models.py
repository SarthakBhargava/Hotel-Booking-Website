from django.conf import settings
from django.db import models

# Create your models here.

class roomtype(models.Model):
    typename = models.CharField(max_length=30, null=False)
    roomprice = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField(default="")
    available = models.IntegerField( null=True)
    image = models.ImageField(upload_to='thumbnails', null=True)

    def __str__(self):
        return self.typename


class room(models.Model):
    type = models.ForeignKey(roomtype, on_delete=models.SET_NULL, blank=True, null=True)
    details = models.TextField(default="")
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.type.typename

class reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    room_type = models.CharField(max_length=100, null=True)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    guest = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.user.get_username()


