from django.urls import path

from games.views import GameView

urlpatterns = [
    path('games/', GameView.as_view({'get': 'list', 'post': 'create'})),
    path('games/<pk>', GameView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]
