from django.urls import path
from app import views

urlpatterns = [
   
    path('',views.home,name='home'),
    
    path('blog',views.blog,name='blog'),
    
    path('post_blog',views.post_blog,name='post_blog'),

    # category
    path('category',views.category,name='category'),

    #category api
    path('catcrt/', views.CategoryCreateAPIView.as_view(), name='catcrt'),
    path('catlist/', views.CategoryList, name='catlist'),

    # category
    # path('tag',views.tag_view,name='tag'),

    # contact api
    path('contactcrt/', views.ContactCreateAPIView.as_view(), name='contactcrt'),
    path('contactlist/', views.ContactList, name='contactlist'),


    
    #comment
    path('cmt/<str:pk>/',views.comment,name='cmt'),
    
    
    #comment api
    path('cmtcreate/<str:pk>/', views.comment_blog_api, name='cmtcreate'),
    # path('cmtcrt/<str:pk>/', views.CommentCreateAPIView.as_view(), name='cmtcrt'),

    path('cmtlist/', views.CommentList, name='cmtlist'),


    # like
    # path('user_like/<str:pk>/', views.user_like, name="user_like"),
    path('like_post/', views.like_post, name="like_post"),

    

    #like api

    path('likelist/', views.LikeList, name='likelist'),
    
    
    #blog api
    
    path('blogcrt/', views.BlogCreateAPIView.as_view(), name='blogcrt'),
    path('bloglist/', views.BlogList, name='bloglist'),
    path('blogdetail/<str:pk>/', views.BlogDetail, name='blogdetail'),
    path('blogupdate/<str:pk>/', views.BlogUpdate, name='blogupdate'),
    path('blogdelete/<str:pk>/', views.BlogDelete, name='blogdelete'),
    
    
    #login with template
    path('logout/',views.logout,name='logout'),
]

