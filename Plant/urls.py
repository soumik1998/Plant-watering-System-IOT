from django.conf.urls import url
from . import views

app_name = 'Plant'

urlpatterns = [url(r'^send/$', views.getdata, name='getdata'),
               url(r'^makeUser/$', views.makeUser, name='makeUser'),
               url(r'^userProfile/$', views.userprofile, name='userProfile'),
               url(r'home/$', views.home, name='home'),
               url(r'^home/(?P<name>\w+)/$', views.home, name='home'),
               url(r'^addplant/(?P<name>\w+)/$', views.addplant, name='addplant'),
               url(r'^userPlants/(?P<name>\w+)/(?P<plant_name>\w+)/$', views.userPlants, name='userPlants'),
               url(r'^editUser/(?P<name>\w+)/$', views.editUser, name='editUser'),
               url(r'^signup/$', views.signup, name='signup'),
               url(r'^login/$', views.login, name='login'),
               url(r'^logout/$', views.logout, name='logout'),
               ]
