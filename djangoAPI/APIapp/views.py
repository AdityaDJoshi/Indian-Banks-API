# from http.client import HTTPResponse
from django.http import HttpResponse, Http404
from django.core.cache import cache
from django.http import JsonResponse
import requests
from django.shortcuts import render
import requests
import json
# Create your views here.

from APIapp.functions import isValidIFSCode


def ifsc_search(request):
    ifsc = request.GET.get('ifsc')
    validIFSC = isValidIFSCode(ifsc)
    if ifsc == "" or (not validIFSC):
        raise Http404("Incorrect ifsc code")

    cache_key = ifsc
    cache_time = 86400
    data = cache.get(cache_key)
    if not data:
        print("Not in cache, retrieving")
        data = requests.get(
            "http://localhost:8008/search?ifsc="+ifsc).json()

    cache.set(cache_key, data, cache_time)

    return JsonResponse({'response': data})


def bank_leaderboard(request):
    DESC = request.GET.get('DESC', "True")
    fetchcount = request.GET.get('fetchcount', "10")
    print(DESC, fetchcount)

    fetchcount = eval(fetchcount)
    DESC = eval(DESC)
    print("After typecasted", DESC, fetchcount)
