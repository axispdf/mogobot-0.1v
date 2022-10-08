from django.shortcuts import render
from .serializers import SerializeUrls
from .models import Urls
from django.utils.safestring import mark_safe
import json
from django.views.decorators.csrf import csrf_exempt,csrf_protect

@csrf_exempt
def urlscreateES(request, ID):
    urls = Urls
    room_name=ID
    urlsid = Urls.objects.get(ID=ID)
    context ={
        "urls": urls,
        "urlsid": urlsid,
        'room_name_json': mark_safe(json.dumps(room_name))
    }
    return render(request, 'polls/italy.html', context )

@csrf_exempt
def urlscreate(request, ID):
    urls = Urls
    room_name=ID
    urlsid = Urls.objects.get(ID=ID)
    context ={
        "urls": urls,
        "urlsid": urlsid,
        'room_name_json': mark_safe(json.dumps(room_name))
    }
    
    return render(request, 'polls/site.html', context)

@csrf_exempt
def urlscreateSLOV(request, ID):
    urls = Urls
    room_name=ID
    urlsid = Urls.objects.get(ID=ID)
    context ={
        "urls": urls,
        "urlsid": urlsid,
        'room_name_json': mark_safe(json.dumps(room_name))
    }
    
    return render(request, 'polls/slovakia.html', context)

@csrf_exempt
def urlscreateAUST(request, ID):
    urls = Urls
    room_name=ID
    urlsid = Urls.objects.get(ID=ID)
    context ={
        "urls": urls,
        "urlsid": urlsid,
        'room_name_json': mark_safe(json.dumps(room_name))
    }
    
    return render(request, 'polls/austria.html', context)


@csrf_exempt
def urlscreateENGLD(request, ID):
    urls = Urls
    room_name=ID
    urlsid = Urls.objects.get(ID=ID)
    context ={
        "urls": urls,
        "urlsid": urlsid,
        'room_name_json': mark_safe(json.dumps(room_name))
    }
    
    return render(request, 'polls/angland.html', context)

@csrf_exempt
def urlscreatefrance(request, ID):
    urls = Urls
    room_name=ID
    urlsid = Urls.objects.get(ID=ID)
    context ={
        "urls": urls,
        "urlsid": urlsid,
        'room_name_json': mark_safe(json.dumps(room_name))
    }
    

    return render(request, 'polls/france.html', context)




