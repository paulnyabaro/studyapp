from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' # Will create form based on the model content (Rendering all)
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio'] # The fields you want to be output