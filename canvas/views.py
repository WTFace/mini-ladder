from django.shortcuts import render
from .models import Result
from django.http import JsonResponse,HttpResponse


def home(req):
    res = req.META
    return render(req, 'canvas/home.html', {'res':res})

def ladder(req):
    res = req.META
    return render(req, 'canvas/ladder.html', {'res':res, 'allowed':['112.201.162.146', '127.0.0.1', '180.232.154.50']})

def get_one(req, id):
    data = Result.objects.get(pk=id)
    res = {'start':data.start,'bridges':data.bridges}
    
    return HttpResponse(JsonResponse(res))
