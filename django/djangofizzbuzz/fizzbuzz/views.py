from django.shortcuts import render

from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponse
from djangofizzbuzz.settings import BASE_DIR
import os
moduledir = os.path.dirname(os.path.dirname(BASE_DIR))
os.sys.path.insert(0, moduledir) 
from fizzbuzzMod.fizzbuzz import FizzBuzz

def index(request, t0=1, t1=100):
    fizzbuzz = FizzBuzz(t0, t1).fizzbuzz
    context = {
        'fizzbuzz': fizzbuzz,
        't0': t0,
        't1': t1,
    }
    return render(request, 'fizzbuzz/index.html', context)

def modify(request):
    t0 = request.POST['t0']
    t1 = request.POST['t1']
    return HttpResponseRedirect(reverse('index', args=(t0, t1, )))
