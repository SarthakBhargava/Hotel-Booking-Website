from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/', views.rooms, name='rooms'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.log_out, name='logout'),
    path('booking/', views.booking, name='booking'),
    path('book/', views.book, name='book'),
    path('account/', views.account, name='account'),
    path('profile/', views.profile, name='profile'),
    path('<str:type>/', views.detail, name='detail'),
]