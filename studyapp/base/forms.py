from django.forms import ModelForm
from .models import Room, User

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' # Will create form based on the model content (Rendering all)
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email'] # The fields you want to be output