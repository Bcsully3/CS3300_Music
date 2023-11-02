from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import *
from .forms import *


# Create your views here.

def index(request):
    student_active_portfolios = Musician.objects.select_related('portfolio').all().filter(portfolio__is_active=True)
    print("active portfolio query set", student_active_portfolios)
    return render( request, 'portfolio_app/index.html', {'student_active_portfolios':student_active_portfolios})




class MusicianListView(generic.ListView):
    model = Musician
class MusicianDetailView(generic.DetailView):
    model = Musician