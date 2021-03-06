from django.urls import path

from users.views import login, registration, logout, profile, verify

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),

    path('verify/<str:email>/<str:activate_key>/', verify, name='verify')
]
