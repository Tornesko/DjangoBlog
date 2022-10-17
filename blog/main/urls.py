from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>/', PostView.as_view(), name="post"),
    path('create_post/', AddPostView.as_view(), name="add_post"),
    path('post/edit/<int:pk>/', UpdatePostView.as_view(), name="edit_post"),
    path('post/delete/<int:pk>/', DeletePostView.as_view(), name="delete_post"),
    path('create_category/', AddCategoryView.as_view(), name="add_category"),
    path('see_by_category/<slug:slug>/', SeeByCategoryView.as_view(), name="see_by_category"),
    path('like/<int:pk>/', LikeView, name="like_post"),
    path('comments/<int:pk>/', CommentsView.as_view(), name="comments"),
    path('posts_by/<int:pk>/', PostsByUsersView.as_view(), name="posts_by_user"),
    path('post/<int:pk>/add_comment/', AddCommentView.as_view(), name="add_comment")
]
