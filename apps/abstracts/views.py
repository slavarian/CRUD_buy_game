from django.shortcuts import render, redirect
from django.views import View
from django.db import models
from django.forms import ModelForm
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.urls import path
from django.shortcuts import get_object_or_404, redirect
from games.models import Game

class CRUDView(View):
    model: models.Model
    form: ModelForm
    template_create: str
    template_delete: str
    template_list: str
    template_current: str

    @classmethod
    def create(
        cls,
        request: HttpRequest,
        *args: tuple,
        **kwargs: dict
    ) -> HttpResponse:
        if request.method == 'GET':
            return render(
                request=request,
                template_name=cls.template_create,
                context={
                    'form': cls.form
                }
            )
        if request.FILES:
            form: ModelForm = cls.form(request.POST , request.FILES)
        else:
            form: ModelForm = cls.form(request.POST)
        message: str = None
        if form.is_valid():
            form.save()
            message = "ok"
            return render(
                request=request,
                template_name=cls.template_create,
                context={
                    'form': cls.form,
                    'message': message
                }
            )
        return render(
            request=request,
            template_name=cls.template_create,
            context={
                'form': cls.form
            }
        )

    @classmethod
    def read(
        cls,
        request: HttpRequest,
        *args: tuple,
        **kwargs: dict
    ) -> HttpResponse:
        queryset: list[cls.model] = \
            cls.model.objects.all()
        return render(
            request=request,
            template_name=cls.template_list,
            context={
                'models': queryset
            }
        )
    
    @classmethod
    def buy(
        cls,
        request: HttpRequest,
        game_id: int,
        *args: tuple,
        **kwargs: dict
    ) -> HttpResponse:
        game = get_object_or_404(Game, id=game_id)

        if request.method == 'GET':
            if game.quantity > 0:
                return render(
                    request=request,
                    template_name='buy_game.html',
                    context={'game': game}
                )
            else:
                return render(
                    request=request,
                    template_name='game_sold_out.html',
                    context={'game': game}
                )
        elif request.method == 'POST':
            if game.quantity > 0:
                game.quantity -= 1
                game.save()
            return render(
                    request=request,
                    template_name='game_sold_out.html',
                    context={'game': game}
                )


    @classmethod
    def as_my_view(cls, enpoint: str):
        return [
            path(enpoint, cls.read,  name='read'),
            path(f'{enpoint}/create/', cls.create),
            path(f'{enpoint}/buy/<int:game_id>/', cls.buy, name='buy_game')
        ]
