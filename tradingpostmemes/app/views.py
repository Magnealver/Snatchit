"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
import json
import requests

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    api_url_base = 'https://api.guildwars2.com/v2/'
    response  = requests.get('https://api.guildwars2.com/v2/commerce/listings/19684')
    listingdata = response.json()



    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'id':listingdata['id'],
            'lowest sell':listingdata['sells'],
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
