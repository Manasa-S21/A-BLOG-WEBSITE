# portfolio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('blog/', views.blog_view, name='blog'), # Keep this for the list view
    # --- NEW: URL for individual blog posts ---
    path('blog/<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.blog_post_detail_view,
         name='blog_post_detail'),
    # --- End NEW ---
    path('contact/', views.contact_view, name='contact'),
    path('success/', views.success_view, name='success'),
]