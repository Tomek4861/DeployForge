from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeAPIView.as_view(), name="home"),
    path('user', views.user_delete, name='user_delete'),
    path('home', views.home, name='home'),
    path('contact', views.contact_page, name='contact'),
    path('portfolio/', views.portfolio_page, name='portfolio')
    # path('portfolio/photo/<int:photo_id>/', views.portfolio_page, name='portfolio')
]
