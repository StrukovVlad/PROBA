
from dgango.db import models
from django.contrib.auth.models import User

"""Create your models here"""

class Common(models.Model):
    created_ad = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Contest(Common):
    name = models.CharField(max_lenght=200)
    description = models.CharField(max_lenght=500)
    image = models.ImageField(upload_to='/media/contest')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    vote_price = models.FloatField(default=100.00)
    is_open = models.BooleanField(default=True)

