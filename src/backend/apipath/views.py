from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient
# Create your views here.
def index(request):
    request.encoding = 'utf-8'
    client = MongoClient('192.168.0.105', 27017, username='admin', password='password')
    db = client['test']
    collection = db['id']
    
    if request.method == 'GET':
        data = collection.find_one({'name': 'test'})
        return HttpResponse(data.get('id'))
    elif request.method == 'POST':
        return HttpResponse("Hello, world. You're at the polls index.")
