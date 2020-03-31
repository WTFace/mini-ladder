from django.shortcuts import render
from .models import Result
from django.http import JsonResponse,HttpResponse
from datetime import datetime, timedelta
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt

allowed = ['127.0.0.1', '148.72.213.133', '180.232.154.50', '175.176.10.158', '112.201.171.173','192.241.250.201']


def home(req):
    res = req.META
    return render(req, 'canvas/home.html', {'res':res})


@xframe_options_exempt
def ladder(req):
    res = req.META
    now = datetime.now() - timedelta(seconds=9)
    now = now.time()
    game_id = int((now.hour*60 + now.minute)/3)
    if game_id == 0: game_id = 480
    history = Result.objects.filter(pk__lte=game_id).order_by('-id')

    return render(req, 'canvas/ladder.html', {
        'res':res, 
        'allowed':allowed,
        'history':history,
        'next_id':game_id + 1,
        'sec':now.second,
        'min':now.minute
    })

def get_one(req, id):
    ref = req.META
    data = Result.objects.get(pk=id)
    res = {'start':data.start,'bridges':data.bridges}
    
    return HttpResponse(JsonResponse(res))


@csrf_exempt
def api(req, id):
    ref = req.META
    now = datetime.now() - timedelta(seconds=9)
    nowDate = now.strftime('%Y-%m-%d')
    game_id = int((now.hour*60 + now.minute)/3)
    if game_id == 0: game_id = 480

    if  req.POST.get('secret') == 'h33x41e@+=$q_!i+#uko%lh+t1@=+k' and id <= game_id:
        data = Result.objects.get(pk=id)
        ##res = {'start':data.start,'bridges':data.bridges}
        res = {'date':nowDate, 'start':data.start,'bridges':data.bridges, 'game_id':game_id}
    else:
        res = {'face': '>_<', 'finger': '_|_'}
    
    return HttpResponse(JsonResponse(res))

def base(req):
    res = req.META
    return render(req, 'canvas/base.html', {'res':res})

def get_time(req):
    now = datetime.now() - timedelta(seconds=9)
    res = {'min':now.minute, 'sec':now.second}
    return HttpResponse(JsonResponse(res))
