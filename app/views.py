from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hai(request,mouni):
    return HttpResponse(f'mounika reddy {mouni}')
