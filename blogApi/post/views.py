from django.shortcuts import render
from django.views.generic.list import ListView
from .models import PostModel
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = PostModel.objects.prefetch_related('comments')
    serializer_class = PostSerializer
    http_method_names = ['get', 'post', 'patch', 'put', 'delete'] 

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)  # Handle PUT (partial=False) or PATCH (partial=True) requests
        post = self.get_object()
        serializer = self.get_serializer(post, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    


