from django.urls import path

from . import views

urlpatterns = [
    path('', views.rapid_prospect_ai_index, name='home'),
    path('', views.rapid_prospect_ai_index, name='index'),
    path('business-os/', views.business_os, name='business_os'),
    path('education/', views.education, name='education'),
    path('enterprise/', views.enterprise, name='enterprise'),
    path('ikonik/', views.ikonik, name='ikonik'),
]
