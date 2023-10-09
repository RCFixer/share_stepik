"""
URL configuration for share_stepik project.

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
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("select2/", include("django_select2.urls")),
    path('add', views.create_page, name='add'),
    path('<int:id>', views.page_view, name='page'),
    path('', views.page_list, name='home'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('edit/<int:id>', views.update_page, name='update'),
    path('delete/<int:id>', views.delete_page, name='delete'),
    path('specialization/add', views.create_specialization, name='create_specialization'),
    path('specialization/', views.specialization_page_list, name='specialization_list'),
    path('specialization/<int:id>', views.specialization_view, name='specialization'),
    path('specialization/<int:id>/add', views.create_specialization_page, name='specialization_add_sp'),
    path('specialization/<int:id>/edit', views.update_specialization_page, name='specialization_edit'),
    path('specialization/<int:id>/delete', views.delete_specialization_page, name='delete_specialization_page'),
]
