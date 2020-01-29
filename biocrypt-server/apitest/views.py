from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json, requests
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .models import Share
import requests, json

def index(request):
    return HttpResponse("Hello Buddy");

@csrf_exempt
def testing(request):
    username = request.POST.get('username', None)
    share_data = request.POST.get('share_data', None)
    #print(data)
    context = {
        'username': username
    }
    address = "http://192.168.43.216:8080/registration/getUserId/"
    response = requests.post(address, data=context)
    response = json.loads(response.content)
    user_id = response['user_id']
    print(user_id)
    shareId = "1"
    share = Share()
    share.createNewShare(user_id, shareId, share_data)
    share.save()
    return HttpResponse("Share Received")


@csrf_exempt
def returnShares(request):
    username = request.POST.get('username', None)
    context = {
        'username': username
    }
    address = "http://192.168.43.216:8080/registration/getUserId/"
    response = requests.post(address, data=context)
    response = json.loads(response.content)
    user_id = response['user_id']
    share = Share.objects.filter(user_id=user_id)[0]
    return HttpResponse(share.share_data)

@csrf_exempt
def tp(request):
    #share = Share.objects.filter(user_id="abc")[0]
    #Share.objects.all().delete()
    context = {
        'data': "123"
    }

    return HttpResponse(json.dumps(context))
