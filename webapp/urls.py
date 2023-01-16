from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('add-tubes/', views.add_tubes, name='add-tubes'),
    path('solution', views.solution, name = 'solution')
]