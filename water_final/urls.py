"""water_final URL Configuration

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


from water_final.views import (
    LoginView,
    HomeView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.index, name='index'),
    path('knowledge', HomeView.knowledge, name='knowledge'),
    path('device', HomeView.devicecontrol, name='devicecontrol'),
    path('irrigation_area', HomeView.irrigation_area, name='irrigation_area'),
    path('info', HomeView.info, name='info'),
    path('fertilizer', HomeView.fertilizer, name='fertilizer'),
    path('auto', HomeView.auto, name='auto'),
    path('alerts', HomeView.alerts, name='alerts'),
    path('data', HomeView.data, name='data'),
    path('login', LoginView.login_user, name='login'),
    path('logout', LoginView.logout_user, name='logout'),
]

