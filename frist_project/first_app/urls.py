from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.vishnu,name='vishnu1212'),
    path('vishnu12a',views.vishnu12a,name='vishnu12a'),
    path('contact',views.contact,name='contact'),
    path('create_superuser_view',views.create_superuser_view,name='create_superuser_view'),
    
]
