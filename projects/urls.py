from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.project),
    path('details/<int:pk>', views.ProjectDetailView),
    path('details/', views.prjct)
]
