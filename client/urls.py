from django.urls import path
from . import views
urlpatterns = [
    path('client/<int:pk>', views.clientDetailView),
    path('client/', views.client)
]
