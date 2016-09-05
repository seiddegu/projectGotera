from django.contrib import admin

# Register your models here.
from shops.models import Shops,ShopsDetail
    
admin.site.register(Shops)
admin.site.register(ShopsDetail)