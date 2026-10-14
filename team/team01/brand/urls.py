from django.urls import path,include
from . import views

app_name='brand'
urlpatterns = [
    path('coffee/', views.coffee, name='coffee'),
    path('chicken/', views.chicken, name='chicken'),
    path('hair/', views.hair, name='hair'),
    path('convenience/', views.convenience , name='convenience'),
]