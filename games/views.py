from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response

from games.models import Game
from games.serializer import GameSerializer


class GameView(viewsets.ModelViewSet):
    """
      A ViewSet for game model with following functionality
    """

    serializer_class = GameSerializer

    queryset = Game.objects.all()

    def list(self, request):
        queryset = Game.objects.all()
        serializer = GameSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Game added successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Game.objects.all()
        game = get_object_or_404(queryset, pk=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        if len(Game.objects.filter(id=pk)) > 0:
            Game.objects.get(id=pk).delete()
            return Response({'message': 'Game removed successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Game not present'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        queryset = Game.objects.all()
        game = get_object_or_404(queryset, pk=pk)
        serializer = GameSerializer(game, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Game details updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
