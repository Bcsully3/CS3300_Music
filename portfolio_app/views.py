from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import *
from .forms import *


# Create your views here.

def index(request):
    pieces_active = Piece.objects.all()
    print("active portfolio query set", pieces_active)
    return render( request, 'portfolio_app/index.html', {'pieces_active':pieces_active})


def updateMusician(request, musician_id):
    
    musician = get_object_or_404(Musician, pk=musician_id) # get the project

    if request.method == "POST":
        
        form = MusicianForm(request.POST, instance=musician)
        
        if form.is_valid(): # if form is valid, save new update and redirect to portfolio detail page
            
            form.save()
            return redirect("musician-detail", pk=musician.pk)
    else:
        # If HTTP method is not POST, create a form with the current project data
        form = MusicianForm(instance=musician)

        return render(request, "portfolio_app/musician_update.html", {"form": form, "musician": musician})



def updatePiece(request, piece_id):
    
    piece = get_object_or_404(Piece, pk=piece_id) # get the project

    if request.method == "POST":
        
        form = PieceForm(request.POST, instance=piece)
        
        if form.is_valid(): # if form is valid, save new update and redirect to portfolio detail page
            
            form.save()
            return redirect("piece-detail", pk=piece.pk)
    else:
        # If HTTP method is not POST, create a form with the current project data
        form = PieceForm(instance=piece)

        return render(request, "portfolio_app/piece_update.html", {"form": form, "piece": piece})



def createPiece(request, piece_id):
    form = PieceForm()
    piece = Piece.objects.get(pk=piece_id)

    if request.method == 'POST':
        # Create a new dictionary with form data and portfolio_id
        project_data = request.POST.copy()
        project_data['piece_id'] = piece_id

        form = PieceForm(project_data)
        if form.is_valid():
            # Save the form without committing to the database
            musician = form.save(commit=False)
            # Set the portfolio relationship
            musician.piece = piece
            musician.save()

            # Redirect back to the portfolio detail page
            return redirect('piece-detail', piece_id)


def deletePiece(request, piece_id):

    piece = get_object_or_404(Piece, pk=piece_id) # attempt to get the project, or return 404 if failed

    if request.method == "POST":
        if request.POST.get("confirm") == "yes": # delete confirmation and redirect to portfolio detail page

            piece.delete()
            return redirect("piece-detail", pk=piece.pk)

        elif request.POST.get("cancel") == "yes": # If the user cancels deletion, return to portfolio detail page
            return redirect("piece-detail", pk=piece.portfolio.pk)

    return render(request, "portfolio_app/piece_delete.html", {"piece": piece}) # Confirmation if request is not POST


class MusicianListView(generic.ListView):
    model = Musician
class MusicianDetailView(generic.DetailView):
    model = Musician

class PieceListView(generic.ListView):
    model = Piece
class PieceDetailView(generic.DetailView):
    model = Piece