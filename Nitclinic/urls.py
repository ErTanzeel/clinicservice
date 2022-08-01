from django.urls import path
from . import views
urlpatterns=[
    path("home",views.home),
    path("sig",views.sig),
    path("inscode",views.inscode),
    path("insert",views.insert),
    path("inpcode",views.inpcode),
    path("login",views.login),
    path("log",views.log),
    path("about",views.about),

]