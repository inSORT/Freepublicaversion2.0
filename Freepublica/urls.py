from django.urls import path 

from .views import HomePageView, Reg_view

urlpatterns = [
    path('', HomePageView.as_view(),name='index'),
    path('sign_in/',Reg_view.as_view(),name='signin'),


]