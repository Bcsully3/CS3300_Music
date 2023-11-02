from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('musicians/', views.MusicianListView.as_view(), name= 'students'),
    path('musicians/<int:pk>', views.MusicianDetailView.as_view(), name='student-detail'),


]   