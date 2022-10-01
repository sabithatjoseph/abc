from . import views
from django.urls import path

app_name = 'limousineapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('about/',views.about,name='about'),
    path('bahrain/',views.bahrain,name='bahrain'),
    path('saudi/',views.saudi,name='saudi'),
    path('gallery/',views.gallery,name='gallery'),
    path('review/',views.review,name='review'),
    path('contact/',views.contact,name='contact'),
]
