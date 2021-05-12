"""kijiwenongwa_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from .views import HomeView,ArticleDetailView,AddPost,UpdatePostView,DeletePostView,AddCategory,CategoryView,CategoryListView,LikeView,AddComment

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('Article/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('add_post/',AddPost.as_view(),name='add_post'),
    path('add_category/', AddCategory.as_view(), name='add_category'),
    path('Article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('Article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>',CategoryView,name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>',LikeView,name='like_post'),
    path('Article/<int:pk>/comment/', AddComment.as_view(), name='add_comment'),

]
