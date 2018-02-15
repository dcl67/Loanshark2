from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.db.models import Q

import re

from inventory.models import Device

@login_required
def index(request):
    return render(request, 'home/index.html', context=None)

# search?
def normalize_query(query_string,
    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
    normspace=re.compile(r'\s{2,}').sub):

    return [normspace(' ',(t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):

    '''
    Returns a query, that is a combination of Q objects. 
    That combination aims to search keywords within a model by testing the given search fields.
    '''

    query = None # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query
"""
#search view
def search_for_something(request):
    print('made it here')
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        entry_query = get_query(query_string, ['name', 'serial_number', 'owner', 'issued_to'])
        found_entries = Model.objects.filter(entry_query).order_by('-something')
    print(found_entries)
    return render_to_response('inventory/search_results.html',
            { 'query_string': query_string, 'found_entries': found_entries }
            #context_instance=RequestContext(request)
        )
"""
def search_for_something(request, searchtext):
    results = Device.objects.filter(Q(name__icontains=searchtext) | Q(serial_number__icontains=searchtext) | Q(issued_to__icontains=searchtext))
    context = {
        results:results
    }
    return render(request, 'home/searchresults.html', context)


"""
def search_results(request, search_term): #-w
    devices  = Device.objects.all()
    for term in search_term.split():
        devices = devices.filter(Q(name__icontains=term)| Q(serial_number__icontains= term)| Q(owner__icontains=term)| Q(issued_to__icontains=term))
        
#    return devices

def search(request):
    query_string = ''
    found_entries = None
    if 'q' in request.GET and request.GET['q'].strip():
        query_string = request.GET['q']
        
    
    context = {
        'devices': devices,
    }

    return render(request, 'inventory/search_results.html', {'context': context})
"""