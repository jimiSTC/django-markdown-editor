from django.shortcuts import render

from .sqlPluginDev import Dashi2, Donation
#from .live import Dashi2
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from tabulate import tabulate
from .forms import NameForm

from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page



#import os
#os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

@cache_page(CACHE_TTL)
def index(request):
    return HttpResponse("Welcome the new Dashi page")


def Cust(request, customer_id):
    row = CustDet(customer_id)
    template2 = loader.get_template('DashiKombu/cust.html')

    context = {
        'row': row,
    }
    #return HttpResponse(row[0][4])
    return HttpResponse(template2.render(context, request))

def EmailReqLog(request):
    results = EmailLog()
    
    return HttpResponse(tabulate(results, tablefmt='html'))

@cache_page(CACHE_TTL)
def DashiBoard(request):
    print("test.....................dashi...view")
    SalesResults = Dashi2()
    DonationResults = Donation()
    template = loader.get_template('DashiKombu/Dashi.html')
    context = {
        'SalesResults': SalesResults,
        'DonationResults': DonationResults
    }
    print(context)
    return HttpResponse(template.render(context, request))

def glow(request):
    template3 = loader.get_template('DashiKombu/glow.html')
    context = {}
    return HttpResponse(template3.render(context,request))


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print(request.POST.get('your_name'))
            print('Test')
            return HttpResponseRedirect('your_name/' + request.POST.get('your_name') + ' ' + request.POST.get('your_surname'))
            #return testFunction( request.POST.get('your_name'), request.POST.get('your_surname'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        print(request.POST)

    return render(request, 'DashiKombu/name.html', {'form': form})


def your_name(request, cust_name):
    return HttpResponse('Hi there ' + cust_name) 


#def testFunction(fname, sname):
#    return HttpResponse ('Good day there' + fname + ' and surname' +sname)


#Need to import global settings for the cache to work

#import os
#os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'