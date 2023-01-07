from django.shortcuts import render
from .models import Room
from .forms import RoomForm

def home(request):
    rooms = Room.objects.all()
    context =  {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/rooms.html', context)


def create_room(request):
    form = RoomForm()
    context = {'form': form}
    return render(request, 'base/room_form.html', context)
