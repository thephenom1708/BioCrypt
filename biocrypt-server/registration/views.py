from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json, requests
import hashlib
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from apitest.models import Share
from .models import User

@csrf_exempt
def register(request):
    name = request.POST.get('name', None)
    username = request.POST.get('username', None)
    pin = request.POST.get('pin', None)
    new_user = User()
    new_user.createNewUser(name, username, pin)
    new_user.save()
    user = User.objects.filter(username=username)[0]
    if user is not None:
        return HttpResponse("1")
    else:
        return HttpResponse("0")

@csrf_exempt
def getUserId(request):
    username = request.POST.get('username', None)
    user = User.objects.filter(username=username)[0]
    context = {
        'user_id': user.user_id
    }
    return HttpResponse(json.dumps(context))

@csrf_exempt
def verifyPin(request):
    username = request.POST.get('username', None)
    pin = request.POST.get('pin', None)

    sha = hashlib.sha256()
    sha.update(pin.encode('utf-8'))
    curr_pin_hash = sha.hexdigest()

    user = User.objects.filter(username=username)[0]
    if(curr_pin_hash == user.pin_hash):
        return HttpResponse("1")
    else:
        return HttpResponse("0")


@csrf_exempt
def uploadFingerprint(request):
    username = request.POST.get('username', None)
    fingerprint = request.POST.get('fingerprint', None)
    coordinates = request.POST.get('coordinates', None)
    User.objects.filter(username=username).update(fingerprint=fingerprint, coordinates=coordinates)
    return HttpResponse("Uploaded")

@csrf_exempt
def getCoordinates(request):
    username = request.POST.get('username', None)
    user = User.objects.filter(username=username)[0]
    return HttpResponse(user.coordinates)

@csrf_exempt
def tpsend(request):
    username = request.POST.get('name', None)
    print(username)
    context = {
        'data': "Hello"
    }
    return HttpResponse(json.dumps(context))
