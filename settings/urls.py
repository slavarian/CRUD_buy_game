from django.contrib import admin
from django.urls import path


from games.views import GameView

from games.views import GameView 
from user.views import UserView , CommentView


urlpatterns = [
    path('admin/', admin.site.urls),
    *GameView.as_my_view('game'),
    *UserView.as_my_view('user'),
]
