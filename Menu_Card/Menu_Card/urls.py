"""
URL configuration for Menu_Card project.

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
from django.contrib.auth import views as auth_views
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('add_menu',views.add_menu),
    path('admin_login', auth_views.LoginView.as_view(template_name='adminlogin.html', success_url='admin_home'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('sample',views.sample,name='sample'),
         
] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
