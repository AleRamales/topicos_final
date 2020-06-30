from django.shortcuts import render
#from django.http import HttpResponse
from datetime import datetime

now = datetime.now().strftime("%b %dth, %Y - %H:%M hrs ")

posts = [
    
    {
       'title': 'Mont Black',
       'user': {
          'name': 'Yesica Cortés',
      'picture' : 'https://picsum.photos/60/60/?image=1027'
    },

    'timestamp'  : datetime.now().strftime("%b %dth, %Y - %H:%M hrs "),
       'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
       'title': 'Via lactea',
       'user':{
          'name': 'Christian Van der Henst',
          'picture' : 'https://picsum.photos/60/60/?image=1005'   
       },
       'timestamp'  : datetime.now().strftime("%b %dth, %Y - %H:%M hrs "),
       'photo': 'https://picsum.photos/800/800/?image=903',
       
    },
    {
       'title': 'Nuevo Auditorio',
       'user': {
          'name': 'Uriel H (thepianartist)',
          'picture': 'https://picsum.photos/60/60/?image=883'
        },
       'timestamp'  : datetime.now().strftime("%b %dth, %Y - %H:%M hrs "),
       'photo' : 'https://picsum.photos/500/700/?image=1076',
    },
    {
       'title': 'Lluvia',
       'user': {
          'name': 'Ariana notanGrande',
      'picture' : 'https://picsum.photos/60/60/?image=1011'
    },
    'timestamp'  : datetime.now().strftime("%b %dth, %Y - %H:%M hrs "),
    'photo' : 'https://picsum.photos/500/700/?image=1004',
    },
    {
       'title': 'En la lista',
       'user': {
          'name': 'Emma Taiyari',
      'picture' : 'https://picsum.photos/60/60/?image=1006'
    },
    'timestamp'  : datetime.now().strftime("%b %dth, %Y - %H:%M hrs "),
    'photo' : 'https://picsum.photos/500/700/?image=1018',
    }

]
# Create your views here.

def list_posts(request):
    return render(request, 'feed.html', {'posts':posts})