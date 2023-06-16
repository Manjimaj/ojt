"""
URL configuration for Cargomanagement project.

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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf.urls.static import static

urlpatterns = [
    path('',views.homepage),
    path('bb/',views.branchmaster),
    path('bb/b/',views.branchpage),
    path('lm/',views.locationmaster),
    path('lm/ud/',views.userdetails),
    path('cm/',views.customermanager),
    path('cm/c/',views.customer),
    path('bm/',views.bookingmanager),
    path('bm/bo/',views.booking), 
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('admin/', admin.site.urls),
    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
