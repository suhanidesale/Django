from django.contrib import admin
from django.urls import path , include
from home import views
urlpatterns = [
    path('desale', views.home , name='home'),
    # path('home/', include('home.urls'))
]
