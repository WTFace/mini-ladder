from django.shortcuts import render
from .models import Result
from django.http import JsonResponse,HttpResponse
import datetime
from django.views.decorators.clickjacking import xframe_options_exempt


def home(req):
    res = req.META
    return render(req, 'canvas/home.html', {'res':res})


@xframe_options_exempt
def ladder(req):
    res = req.META
    now = datetime.datetime.now().time()
    game_id = int((now.hour*60 + now.minute)/3)+1
    history = Result.objects.filter(pk__lte=game_id).order_by('-id')
    return render(req, 'canvas/ladder.html', {
        'res':res, 
        'allowed':['182.23.209.69', '127.0.0.1', '180.232.154.50'],
        'history':history
    })

def get_one(req, id):
    data = Result.objects.get(pk=id)
    res = {'start':data.start,'bridges':data.bridges}
    
    return HttpResponse(JsonResponse(res))

