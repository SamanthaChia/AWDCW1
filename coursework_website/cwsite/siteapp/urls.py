from django.urls import include,path
from . import views
from . import api

urlpatterns =[
    path('', views.index, name='index'),
    path('api/protein', api.CreateProtein.as_view()),
    path('api/protein/<str:pk>', api.protein_details.as_view()),

]