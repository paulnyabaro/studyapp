from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' # Will create form based on the model content (Rendering all)
        exclude = ['host', 'participants']