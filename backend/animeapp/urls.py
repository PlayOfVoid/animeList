from django.urls import path
from .import views as anime

app_name = 'anime'

urlpatterns = [
    path('',anime.index,name='index'),
    path('animes/',anime.animes,name='animes'),
    path('add_anime/',anime.add_anime,name='add_anime'),
    #
    path('register/', anime.register, name='register'),
    path('login/', anime.user_login, name='login'),
]