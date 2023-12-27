from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Todo, Comment, Post
from .serializers import UserSerializer, TodoSerializer, CommentSerializer, PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados de Users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TodoViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados de Albuns
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class CommentViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados de Músicas
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados de Músicas
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer