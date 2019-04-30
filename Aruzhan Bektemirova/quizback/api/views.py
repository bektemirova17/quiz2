# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Post
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostListSerializer, PostSerializer
from datetime import datetime

@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':

        api = Post.objects.all()[:10]
        serializer = PostListSerializer(api, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostListSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    return render(request, 'index.html', context)

@api_view(['GET', 'PUT', 'DELETE'])
def get_list(request, pk):
    try:
        list = PostList.objects.get(id=pk)
    except PostList.DoesNotExist as e:
        return Response({
            'error': str(e)
        })

    if request.method == 'GET':
        serializer = PostListSerializer(list)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostListSerializer(instance = list, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        list.delete()
        return Response({
            'list': 'deleted'
        })

@api_view(['GET', 'POST'])
def get_task_list_tasks(request, pk):
    try:
        tasks = Post.objects.filter(list = pk)
    except Post.DoesNotExist as e:
        return Response({
            'error': str(e)
        })

    if request.method == 'GET':
        serializer = PostSerializer(tasks, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        task_list = PostList.objects.get(id = pk)
        serializer = PostSerializer(data = request.data)
        print(request.data)

        if serializer.is_valid():
            print("de")
            serializer.save(list = list)
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def get_task(request, pk):
    try:
        task = Post.objects.get(id = pk)
    except Post.DoesNotExist as e:
        return Response({
            'error': str(e)
        })
    print(task)

    if request.method == 'GET':
        serializer = PostSerializer(task)
        return Response(serializer.data)
    elif request.method == 'PUT':
        print(request.data)
        serializer = PostSerializer(instance = task, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        task.delete()
        return Response({
            'task': 'deleted'
        })







# Create your views here.
