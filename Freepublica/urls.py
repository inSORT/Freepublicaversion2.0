from django.urls import path 

from .views import HomePageView, Post_view, Reg_view

urlpatterns = [
    path('index/', HomePageView.as_view(),name='index'),
    path('sign_in/',Reg_view.as_view(),name='signin'),
    path('post/',Post_view.as_view(), name='post'),

]