from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class Location(models.Model):
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    voivodeship = models.CharField(max_length=50)


class Realtor(models.Model):
    surname = models.CharField(max_length=20, verbose_name='Nazwisko')
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=90)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?4?8?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    avatar = models.ImageField(blank=True, null=True, verbose_name='Zdjecie', upload_to='avatars/')


class Estate(models.Model):
    person = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    type = models.CharField(max_length=40)

    text = models.TextField(verbose_name='Содержание')
    date_till = models.DateField(verbose_name='Срок')
