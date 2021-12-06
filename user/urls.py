from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user', views.user),
    path('user/<int:pk>', views.clientDetailView),
    # path('userdata/<int:pk>', views.clientDetailView, name='login'),
    # path('login', views.login, name='login'),
    # path('register', views.register, name='register'),
    #     path('logout', views.logout, name='logout'),
    #     path('dashboard', views.dashboard, name='dashboard'),
]
