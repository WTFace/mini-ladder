from django.shortcuts import render


def home(req):
    res = req.META
    return render(req, 'canvas/home.html', {'res':res})

def ladder(req):
    res = req.META
    return render(req, 'canvas/ladder.html', {'res':res, 'allowed':['112.201.174.116', '127.0.0.1', '180.232.154.50']})
