from django.urls import path
from . import views

urlpatterns = [
    path('musicians/', views.MusicianListView.as_view(), name= 'musicians'),
    path('musicians/<int:pk>', views.MusicianDetailView.as_view(), name='musician-detail'),
    path("musicians/<int:musician_id>/update/", views.updateMusician, name="update-musician"),
    path('', views.index, name= 'index'),
    path('pieces/<int:pk>', views.PieceDetailView.as_view(), name='piece-detail'),
    path("pieces/<int:piece_id>/update/", views.updatePiece, name="update-piece"),
    path('pieces/<int:piece_id>/create_piece/', views.createPiece, name='create-piece'),
    path("pieces/<int:piece_id>/delete_piece/", views.deletePiece, name="delete-piece"),


]   