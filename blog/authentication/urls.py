from django.urls import path

from .views import UserRegisterView, UserUpdateView, PasswordUpdateView, ProfileView, ProfileEditView, \
    CreateProfileView, FollowersView, SubscribeView

from . import views
# from django.contrib.auth import views as auth_view

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_user_data/', UserUpdateView.as_view(), name='edit_user_data'),
    path('password/', PasswordUpdateView.as_view(), name='change_password'),
    path('password_succes/', views.password_success, name='password_success'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='edit_profile'),
    path('create_profile/', CreateProfileView.as_view(), name='create_profile'),
    path('profile/<int:pk>/followers/', FollowersView.as_view(), name='followers'),
    path('subscribe/<int:pk>/', SubscribeView, name='subscribe'),
]
