"""
Definition of urls for OrbSight.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from rest_framework import routers
from app import forms, views
from core import views as core_views
from todo import views as todo_views


router = routers.DefaultRouter()
router.register(r'families', core_views.FamilyView, 'core')
router.register(r'individuals', core_views.IndividualView, 'core')
router.register(r'members', core_views.MemberView, 'core')
router.register(r'networks', core_views.NetworkView, 'core')
router.register(r'orbs', core_views.OrbView, 'core')
router.register(r'todos', todo_views.TodoView, 'todo')


urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
    # path('platform/', include('core.urls', namespace='core')),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
