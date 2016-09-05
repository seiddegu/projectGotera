from django.http import HttpResponse
from django.shortcuts import render
from .models import Shops, ShopsDetail
import ethiotel.settings


# Create your views here.

def index(request):
    shops_list = Shops.objects.all()
    banks_list = ['awash', 'dashen', 'abyssinia', 'Commercial']
    banks_list = map(lambda banks_li: str.capitalize(banks_li), banks_list)
    return render(request, 'index.html',
                  dict(shops_list=shops_list, static_url=ethiotel.settings.STATIC_URL, banks_list=banks_list))

def list_of_allshops(request):
    return HttpResponse("We will give all the details <br> Shops Name <br> Shops ID <br> Shops LAT and long ")


def shop_details_view(request, shop_name):
    shop_details = ShopsDetail.objects.get(shop_id__shop_name=shop_name)

    return render(request, 'ShopDetails.html', {'shopDetails': shop_details})
