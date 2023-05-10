from django.urls import path
from . import views


urlpatterns = [
    path('', views.routes),
    path('socios/', views.socios),
    path('socio/<int:id>', views.socio)
]