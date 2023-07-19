from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('ads/<int:ad_id>/', views.ad_detail, name='ad_detail'),
    path('login/', views.login_view, name='login'),
    path('registration_end/', views.registration_end_view, name='registration_end'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('',views.ad_list,name='home'),
    path('search/', views.search_view, name='search'),
    path('create_ad/', views.create_ad,name='create_ad'),
    path('categories/', views.categories, name='categories'),
    path('<str:category>/', views.category_ads, name='category_ads'),
    path('ad/<int:ad_id>/edit/', views.edit_ad, name='edit_ad'),
    path('delete_ad/<int:ad_id>/', views.delete_ad, name='delete_ad'),
]