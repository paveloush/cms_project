from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
from django.urls import reverse


class Location(models.Model):
    district = models.CharField(blank=True, max_length=50)
    city = models.CharField(blank=True, max_length=30)
    voivodeship = models.CharField(blank=True, max_length=50)

    def __str__(self):  # Python 3: def __unicode__(self):
        if self.district and self.city and self.voivodeship:
            return self.district + ', ' + self.city + ', ' + self.voivodeship
        elif self.city and self.voivodeship:
            return self.city + ', ' + self.voivodeship
        elif self.voivodeship:
            return self.voivodeship


class Realtor(models.Model):
    surname = models.CharField(max_length=20, verbose_name='Nazwisko')
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=90)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?4?8?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    avatar = models.ImageField(blank=True, null=True, verbose_name='Zdjecie', upload_to='avatars/')

    def __str__(self):
        return self.name + ' ' + self.surname


class Estate(models.Model):
    person = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    title = models.TextField(verbose_name='Заголовок')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'id': self.id})
