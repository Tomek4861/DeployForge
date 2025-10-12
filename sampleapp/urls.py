from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', views.HomeAPIView.as_view(), name='api_root'),
    path('api/user', views.user_delete, name='user_delete'),
    path('api/messages/count', views.messages_count, name='messages_count'),
    path('contact', views.contact_page, name='contact'),
    path('portfolio/', views.portfolio_page, name='portfolio')
    # path('portfolio/photo/<int:photo_id>/', views.portfolio_page, name='portfolio')
]
