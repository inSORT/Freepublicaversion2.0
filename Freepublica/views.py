from django.shortcuts import render
from django.views.generic import *

# Create your views here.

class HomePageView(TemplateView):
    template_name= 'index.html' 


class Reg_view(TemplateView):
    template_name='signin.html'


