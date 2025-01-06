from django.urls import path, include
# from . import views
#
#
# urlpatterns = [
#     path('', views.index),
#
#     # URL для статистики аккаунта
#     path('account/<int:account_id>/statistics/', views.account_statistics, name='account_statistics'),
#
#     # URL для отображения всех постов
#     path('posts/', views.all_posts, name='all_posts'),
#
#     # URL для добавления нового аккаунта
#     path('add_account/', views.add_account, name='add_account'),
#
#     # URL для добавления нового поста
#     path('add_post/', views.add_post, name='add_post'),
#
#     path('accounts/', views.all_accounts, name='all_accounts'),
#
#     path('posts/delete/<int:post_id>/', views.delete_post, name='delete_post'),
#
# ]

from .views import (
    IndexView,
    AccountStatisticsView,
    PostListView,
    AddAccountView,
    AddPostView,
    AccountListView,
    DeletePostView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('accounts/', AccountListView.as_view(), name='all_accounts'),
    path('posts/', PostListView.as_view(), name='all_posts'),
    path('account/<int:account_id>/statistics/', AccountStatisticsView.as_view(), name='account_statistics'),
    path('accounts/add/', AddAccountView.as_view(), name='add_account'),
    path('posts/add/', AddPostView.as_view(), name='add_post'),
    path('posts/delete/<int:pk>/', DeletePostView.as_view(), name='delete_post'),
]