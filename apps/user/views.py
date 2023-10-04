from abstracts.views import CRUDView
from user.models import MyUser , Commets
from user.forms import CreateUser , CreateComment


class UserView(CRUDView):
    model = MyUser
    form = CreateUser
    template_create = 'create_user.html'
    template_list = 'list_user.html'


class CommentView(CRUDView):
    model = Commets
    form = CreateComment
    template_create = 'create_comment.html'




