from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def index(request):
    pieces_active = Piece.objects.all()
    print("active portfolio query set", pieces_active)
    return render( request, 'portfolio_app/index.html', {'pieces_active':pieces_active})

@login_required(login_url='login')
@allowed_users(allowed_roles=['musician_group'])
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['musician_group'])
def updatePiece(request, piece_id):
    
    piece = get_object_or_404(Piece, pk=piece_id) # get the project

    if request.method == "POST":
        
        form = PieceForm(request.POST, request.FILES, instance=piece)
        
        if form.is_valid(): # if form is valid, save new update and redirect to portfolio detail page
            
            form.save()
            return redirect("piece-detail", pk=piece.pk)
    else:
        # If HTTP method is not POST, create a form with the current project data
        form = PieceForm(instance=piece)

        return render(request, "portfolio_app/piece_update.html", {"form": form, "piece": piece})



@login_required(login_url='login')
@allowed_users(allowed_roles=['musician_group'])
def createPiece(request, musician_id):

    form = PieceForm()
    musician = Musician.objects.get(pk=musician_id)

    if request.method == 'POST':
        # Create a new dictionary with form data and portfolio_id
        project_data = request.POST.copy()
        project_data['musicain_id'] = musician_id

        form = PieceForm(project_data, request.FILES)
        if form.is_valid():
            # Save the form without committing to the database
            piece = form.save(commit=False)
            # Set the portfolio relationship
            piece.musician = musician
            piece.save()

            # Redirect back to the portfolio detail page
            return redirect('musician-detail', musician_id)

    context = {'form': form}
    return render(request, 'portfolio_app/piece_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['musician_group'])
def deletePiece(request, piece_id):

    piece = get_object_or_404(Piece, pk=piece_id) # attempt to get the project, or return 404 if failed

    if request.method == "POST":
        if request.POST.get("confirm") == "yes": # delete confirmation and redirect to portfolio detail page

            piece.delete()
            return redirect("piece-detail", pk=piece.pk)

        elif request.POST.get("cancel") == "yes": # If the user cancels deletion, return to portfolio detail page
            return redirect("piece-detail", pk=piece.portfolio.pk)

    return render(request, "portfolio_app/piece_delete.html", {"piece": piece}) # Confirmation if request is not POST


def registerPage(request):
    user_form = CreateUserForm()
    musician_form = MusicianForm()
    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        musician_form = MusicianForm(request.POST)
        if user_form.is_valid() and musician_form.is_valid():
            user = user_form.save()
            musician = musician_form.save(commit=False)
            musician.user = user
            musician.save()
            newusername = user_form.cleaned_data.get('username')
            group = Group.objects.get(name='musician_group')
            user.groups.add(group)
            messages.success(request, 'Account was created for ' + newusername)
            return redirect('login')
    context = {'user_form': user_form, 'musician_form': musician_form}
    return render(request, 'registration/register.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['musician_group'])
def userPage(request):
    musician = request.user.musician
    form = MusicianForm(instance=musician)
    print('musician', musician)
    if request.method == 'POST':
        form = MusicianForm(request.POST, request.FILES, instance=musician)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'portfolio_app/user.html', context)





class MusicianListView(generic.ListView):
    model = Musician
class MusicianDetailView(generic.DetailView):
    model = Musician

    def get_context_data(self, **kwargs):
        context = super(MusicianDetailView, self).get_context_data(**kwargs)
        pieces = Piece.objects.filter(musician_id=self.object)
        context["pieces"] = pieces
        return context

class PieceListView(generic.ListView):
    model = Piece
class PieceDetailView(generic.DetailView):
    model = Piece