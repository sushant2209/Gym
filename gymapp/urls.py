from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.home),
    path('addMember', views.addMember,name='addMember'),
    path('success',views.success),
    path('members',views.members,name='members'),
    path('addFees/<int:member_id>/', views.addFees,name='addFees'),
    path('pendingFees',views.pendingFees,name='pendingFees'),
    path('user_profile/<int:user_id>/', views.user_profile, name='user_profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
