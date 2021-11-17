"""md URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from myapp import views
from loginapp import views as auth_views
urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', views.indexFunc),  
    path('search/', views.mainFunc),
    path('searchlist/', views.MSearchFunc), 
    
    path('compare', views.compareFunc),
    path('compare/choice', views.comparechoiceFunc),
    path('compare/choice2', views.comparechoice2Func),
    
    path('cardshow', views.showFunc), 
    path('more', views.moreFunc),
     
    path('mypage', views.mypageFunc), 
    path('gologin',auth_views.LoginView),
    path('login', auth_views.LoginFunc), 
    path('signup', views.signupFunc),
    path('calldb', views.IdDbFunc),
    path('loginprocess',auth_views.login),
    path('logout', auth_views.logout),
    
    path('writesignup', views.writesingupFunc),
    path('findID', views.findIDFunc),
    path('findIDprocess', views.findID), 
    path('findPW', views.findPWFunc),
    path('findPWprocess', views.findPW),
    path('oklogin', views.okloginFunc), 
    path('deleteCard', views.DeleteFunc),  

]