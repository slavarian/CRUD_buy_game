from django.forms import ModelForm

from user.models import MyUser , Commets



class CreateUser(ModelForm):
    class Meta:
        model = MyUser
        fields = (
            'nickname',
            'email',
            'password',
        )
        
class CreateComment(ModelForm):
    class Meta:
        model = Commets
        fields = (
            'game_comments',
            'comment',

        )

