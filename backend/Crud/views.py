from django.shortcuts import render
from .serializers import TodoSerializer
from .models import Todo
from rest_framework import viewsets

# Create your views here.
class TodoView(viewsets.ModelViewSet):
    # serializer
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()