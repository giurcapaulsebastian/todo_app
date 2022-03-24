from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from todolist.models import TodoItem
from .serializers import TodoItemSerializer
from rest_framework import serializers, status

# Create your views here.

@api_view(['POST'])
def create_item(request):
    item = TodoItemSerializer(data=request.data)

    if TodoItem.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
  
    if item.is_valid():
        item.save()
        return Response(item.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_items(request):
    items = TodoItem.objects.all()
  
    if items:
        serializer = TodoItemSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_item(request, pk):
    item = TodoItem.objects.get(pk=pk)
    serializer = TodoItemSerializer(instance=item, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_item(request,pk):
    item = get_object_or_404(TodoItem, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)