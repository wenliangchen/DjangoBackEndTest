from django.shortcuts import render
from pymongo import MongoClient
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    client = MongoClient('192.168.0.196', 27017, username='admin', password='password')
    db = client['test']
    collection = db['id']
    timestamp = datetime.now()
    # get client ip
    ip = request.META.get('REMOTE_ADDR')
    newdata = {
        'name': 'test',
        'id': timestamp,
        'ip': ip
    }
    collection.insert_one(newdata)
    data = collection.find_one({'name': 'test'})

    return HttpResponse(data.get('id'))
    # return HttpResponse("Hello, world. You're at the polls index.")