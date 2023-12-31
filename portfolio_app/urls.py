from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('musicians/', views.MusicianListView.as_view(), name= 'musicians'),
    path('musicians/<int:pk>', views.MusicianDetailView.as_view(), name='musician-detail'),
    path("musicians/<int:musician_id>/update/", views.updateMusician, name="update-musician"),
    path('', views.index, name= 'index'),
    path('pieces/<int:pk>', views.PieceDetailView.as_view(), name='piece-detail'),
    path("pieces/<int:piece_id>/update/", views.updatePiece, name="update-piece"),
    path('musician/<int:musician_id>/create_piece/', views.createPiece, name='create-piece'),
    path("pieces/<int:piece_id>/delete_piece/", views.deletePiece, name="delete-piece"),
    path('accounts/register/', views.registerPage, name = 'register_page'),
    path('user/', views.userPage, name='user_page'),

]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)