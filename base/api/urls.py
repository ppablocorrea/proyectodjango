from django.urls import path
from . import views


urlpatterns = [
    path('', views.routes),
    path('locales/', views.locales),
    path('local/<int:id>', views.local),
    path('servicios/', views.servicios),
    path('servicio/<int:id>', views.servicio),
    path('ocupaciones/', views.ocupaciones),
    path('ocupacion/<int:id>', views.ocupacion)
]