from logging import raiseExceptions
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Song
from .serializer import SongsSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST'])
def song_list(request):
   
   if request.method == 'GET':
       songs = Song.objects.all()
       serializer = SongsSerializer(songs, many = True)
       return Response(serializer.data, status=status.HTTP_200_OK)
    
   elif request.method == 'POST':
       serializer = SongsSerializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def song_by_id(request,pk):
    song = get_object_or_404(Song,pk=pk)
    if request.method == 'GET':
        serializer = SongsSerializer(song)
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = SongsSerializer(song, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        serializer = SongsSerializer(song, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
