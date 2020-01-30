from django.shortcuts import render
import requests
from requests.compat import quote_plus
from bs4 import BeautifulSoup
from . import models

# Create your views here.
BASE_URL='http://127.0.0.1.:8000/new_search/?query={}'
def volume(request):
    return render(request,'volumecal.html')
def new_search(request):
    rain=request.POST.get('rain')
    area=request.POST.get('area')
    c=0.9
    val=float(rain)
    al=float(area)
    val2=val*c*al

    # print(rain)
    # ans=rain*area*0.9
    # models.Volume.objects.create(Rain=rain)

    # final_url=BASE_URL.format(quote_plus(rain))
    # response=requests.get(final_url)
    # data=response.text

    front={'val2':val2,}

    return render(request,'rwhvolume/new_search.html',front)
