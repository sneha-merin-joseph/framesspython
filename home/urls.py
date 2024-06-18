from django.urls import path
from . import views as v

app_name = 'home'
urlpatterns = [
    path('',v.homepage,name="index"),
    # path('search/', v.Search, name='search'),   
]