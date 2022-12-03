from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import TaskSerializer
from .models import *

@api_view(['GET'])
def index(request):
    urls_dic = {}
    context = {}
    return Response(urls_dic)

@api_view(['GET'])
def list(request):
    task = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(task , many = True)

    return Response(serializer.data)


@api_view(['GET'])
def item(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task , many = False)
    return Response(serializer.data)    


@api_view(['POST'])
def create(request):
    # task = Task.objects.get()
    serializer = TaskSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)    

@api_view(['POST'])
def update(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance = task , data= request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)    
    

@api_view(['DELETE'])
def delete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Task deleted!")

    