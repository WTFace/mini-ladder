from django.shortcuts import render
from .models import Result
from django.http import JsonResponse,HttpResponse
import datetime
from django.views.decorators.clickjacking import xframe_options_exempt

allowed = ['182.23.209.69', '127.0.0.1', '180.232.154.50', '175.176.41.153', '112.201.171.173','192.241.250.201']


def home(req):
    res = req.META
    return render(req, 'canvas/home.html', {'res':res})


@xframe_options_exempt
def ladder(req):
    res = req.META
    now = datetime.datetime.now().time()
    game_id = int((now.hour*60 + now.minute)/3)
    if game_id == 0: game_id = 480
    history = Result.objects.filter(pk__lte=game_id).order_by('-id')

    return render(req, 'canvas/ladder.html', {
        'res':res, 
        'allowed':allowed,
        'history':history,
        'next_id':game_id + 1,
    })

def get_one(req, id):
    ref = req.META
    if ref['REMOTE_ADDR'] in allowed:
        data = Result.objects.get(pk=id)
        res = {'start':data.start,'bridges':data.bridges}
    else:
        res = {'face': '>_<', 'finger': '_|_'}
    
    return HttpResponse(JsonResponse(res))
    

