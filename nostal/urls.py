from django.urls import path
from . import views

urlpatterns = [
    path('', views.decade_get, name='decade_get'),
    path('fads', views.fad_get, name='fad_get'),
    path('decade/<int:pk>', views.decade_detail, name='decade_detail'),
    path('fads/<int:pk>', views.fad_detail, name='fad_detail'),
    path('decade/add', views.decade_create, name='decade_create'),
    path('fads/add', views.fad_create, name='fad_create'),
    path('decade/<int:pk>/edit', views.decade_edit, name='decade_edit'),
    path('fad/<int:pk>/edit', views.fad_edit, name='fad_edit'),
    path('decade/<int:pk>/delete', views.decade_delete, name='decade_delete'),
    path('fad/<int:pk>/delete', views.fad_delete, name='fad_delete'),
]