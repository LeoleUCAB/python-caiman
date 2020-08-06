from django.conf.urls import url
from . import views

app_name = "pythonCaiman"

urlpatterns = [
    url(r'^$', views.get_pizza, name='index'),
    url(r'^your-pizza/', views.ready, name='pizza')
]