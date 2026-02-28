from django.urls import include, path


from produition.views.view_porfolioMedia import PortfolioMediaCreateView, PortfolioMediaDeleteView, PortfolioMediaListView
from produition.views.view_portfolio import PortfolioCreateView, PortfolioDeleteView, PortfolioDetailView, PortfolioListView, PortfolioUpdateView
from produition.views.views_contact import ContactFormView
from produition.views.views_Message import (
    MessagesView,
    MessageMarkReadView,
    MessageDeleteView,
    MessageArchiveView,
    MessageReplyView,
)
from produition.views.views_Tableaux_Bord import AdminView
from produition.views.views_connexion import CustomLoginView, InscriptionView, CustomLogoutView
from produition.views.views_Video import (
    VideoListView,
    VideoCreateView,
    VideoUpdateView,
    VideoDeleteView,
    VideoDetailView,
    HeroVideoView,
    VideoToggleStatusView,
    VideoToggleFeaturedView,
)

urlpatterns = [
    path('tableau_de_bord/', AdminView.as_view(), name='tableau_de_bord'),
    path('messages/', MessagesView.as_view(), name='messages'),
    path('messages/<int:pk>/read/', MessageMarkReadView.as_view(), name='message_read'),
    path('messages/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),
    path('messages/<int:pk>/archive/', MessageArchiveView.as_view(), name='message_archive'),
    path('messages/<int:pk>/reply/', MessageReplyView.as_view(), name='message_reply'),
    
    # URLs pour les vidéos
    path('videos/', VideoListView.as_view(), name='video_list'),
    path('videos/ajouter/', VideoCreateView.as_view(), name='video_create'),
    path('videos/<int:pk>/', VideoDetailView.as_view(), name='video_detail'),
    path('videos/<int:pk>/modifier/', VideoUpdateView.as_view(), name='video_update'),
    path('videos/<int:pk>/toggle-status/', VideoToggleStatusView.as_view(), name='video_toggle_status'),
    path('videos/<int:pk>/toggle-featured/', VideoToggleFeaturedView.as_view(), name='video_toggle_featured'),
    path('videos/<int:pk>/supprimer/', VideoDeleteView.as_view(), name='video_delete'),
    path('videos/hero/', HeroVideoView.as_view(), name='hero_video'),
    
    path('connexion/', CustomLoginView.as_view(), name='connexion'),
    path('inscription/', InscriptionView.as_view(), name='inscription'),
    path('deconnexion/', CustomLogoutView.as_view(), name='deconnexion'),
    path('', include('allauth.urls')),
    path('contact/', ContactFormView.as_view(), name='contact'),

    path('portfolio_list/', PortfolioListView.as_view(), name='portfolio_list'),
    path('portfolio/ajouter/', PortfolioCreateView.as_view(), name='portfolio_create'),
    path('portfolio/<int:pk>/', PortfolioDetailView.as_view(), name='portfolio_detail'),
    path('portfolio/<int:pk>/modifier/', PortfolioUpdateView.as_view(), name='portfolio_update'),
    path('portfolio/<int:pk>/supprimer/', PortfolioDeleteView.as_view(), name='portfolio_delete'),
    
    path('portfolio/<int:project_id>/media/add/',PortfolioMediaCreateView.as_view(),name='portfolio_media_add'),
    path('portfolio/<int:project_id>/media/delete/',PortfolioMediaDeleteView.as_view(),name='portfolio_media_delete'),
    path('portfolio_media_list/', PortfolioMediaListView.as_view(), name='portfolio_media_list'),
]
