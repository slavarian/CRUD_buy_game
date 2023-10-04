from django.urls import path
from . import views

urlpatterns = [
    path('game/<int:game_id>/buy/', views.buy_game, name='buy_game'),
]
