"""
URL configuration for proj2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('',views.index),
   path('userreg',views.userreg),
   path('index',views.index),
   path('userview',views.userview),
   path('userlogin',views.userlogin),
   path('uprofile',views.uprofile),
   path('aprofile',views.aprofile),
   path('logout',views.logout),
   path('facreg',views.facreg),
   path('facltylogin',views.facltylogin),
   path('admlogin',views.admlogin),
   path('facltyprofile',views.facltyprofile),
   path('facview',views.facview),
   path('fdelete/<int:id>',views.fdelete,name="fdelete"),
   path('udelete/<int:id>',views.udelete,name="udelete"),
   path('compreg',views.compreg),
   path('viewcomp',views.viewcomp),
   path('updatestatus/<int:id>',views.updatestatus,name="updatestatus"),
   path('acknmesg',views.acknmesg),
   path('acknview',views.acknview,),
   path('admack',views.admack),
   path('adackview',views.adackview),
   path('cupdate/<int:id>',views.cupdate,name="cupdate"),
   path('cupdate/updates/<int:id>',views.updates,name="updates"),
     

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
