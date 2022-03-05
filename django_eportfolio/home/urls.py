from django.contrib import admin
from django.urls import path , include
from home import views
urlpatterns = [
    # path('desale', views.home , name='home'),
    # path('home/', include('home.urls')),
    # path('admin/' , admin.site.urls),
    path('' , views.home , name = 'home'),
    path('about' , views.about , name = 'about'),
    path('projects' , views.projects , name = 'projects'),
    path('contact' , views.contact , name = 'contact'),

]
