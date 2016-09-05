from django.db import models


# Create your models here.

class Shops(models.Model):
    shop_name = models.CharField(max_length=100)
    shop_id = models.IntegerField(unique=True)

    def __unicode__(self):
        return self.shop_name


class ShopsDetail(models.Model):
    shop_id = models.ForeignKey(Shops)
    shop_lat = models.FloatField()
    shop_log = models.FloatField()
    shop_address = models.CharField(max_length=150)
    shop_type = models.CharField(max_length=150)
    shop_status = models.CharField(max_length=150)
    shop_numOfSales = models.IntegerField()

    def __unicode__(self):
        return self.shop_id.shop_name + ' Shop Details \n'
