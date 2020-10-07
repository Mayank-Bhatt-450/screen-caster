from django.urls import path
from.import views
urlpatterns = [
    path("",views.home,name='home'),
    path("h/",views.homes,name='homes'),
    path("q/",views.home1,name='homes1')

]
