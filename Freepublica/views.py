from django.shortcuts import render
from django.views.generic import *
from .models import*

# Create your views here.

class HomePageView(TemplateView):
    template_name= 'index.html' 


class Reg_view(TemplateView):
    template_name='signin.html'



class Post_view(ListView):
    model = Demo_Post
    template_name='post.html'



