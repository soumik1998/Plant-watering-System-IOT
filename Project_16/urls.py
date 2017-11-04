from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'Plant'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Plant/', include('Plant.urls')),
    url(r'^$', views.home, name='home'),
]
