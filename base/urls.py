from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.loginPage),
    path('registro/', views.registerPage),
    path('logout/', views.logoutPage),
    path('manteneragendas/', views.manteneragendas),
    path('agenda/', views.agenda),
    path('agenda/<int:id>', views.agenda),
    path('mantenersocios/', views.mantenersocios),
    path('socio/', views.socio),
    path('socio/<int:id>', views.socio),
    path('mantenerservicios/', views.mantenerservicios),
    path('servicio/', views.servicio),
    path('servicio/<int:id>', views.servicio),
    path('mantenerempleados/', views.mantenerempleados),
    path('empleado/', views.empleado),
    path('empleado/<int:id>', views.empleado),
    path('mantenerlocales/', views.mantenerlocales),
    path('local/', views.local),
    path('local/<int:id>', views.local),
    path('mantenerocupaciones/', views.mantenerocupaciones),
    path('ocupacion/', views.ocupacion),
    path('ocupacion/<int:id>', views.ocupacion)
]