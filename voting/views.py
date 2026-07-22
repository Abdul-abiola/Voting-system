from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout 
from .models import Candidate, Vote
from .forms import VoteForm

# Create your views here.

# voting_candidates = [
#     {'id': 1, 'party': 'APC CANDIDATE'},
#     {'id': 2, 'party': 'ADC CANDIDATE'},
#     {'id': 3, 'party': 'PDP CANDIDATE'},
#     {'id': 4, 'party': 'NNPP CANDIDATE'}
    
# ]

def loginPage(request):
    
    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, 'Username or Password does not exists ')
              
                
    context = {'page' : page}
    return render(request, 'voting/login_register.html', context)
    
def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration ')
           
    return render(request, 'voting/login_register.html', {'form': form })
    

def home(request):
    voting_candidates = Vote.objects.all()
    votes_count = voting_candidates.count()
    context = {'voting_candidates':  voting_candidates, 'votes_count' : votes_count}
    return render(request, 'voting/home.html', context)
    

@login_required(login_url='login')
def vote(request):
    if Vote.objects.filter(user=request.user).exists():
        messages.warning(request, "You have already voted. You cannot vote more than once.")
        return redirect('home')
     
    form = VoteForm()
    
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            vote_instance = form.save(commit=False)
            vote_instance.user = request.user
            vote_instance.save()
            messages.success(request, "Your vote has been recorded successfully.")
            return redirect('home')  
          
    context = {'form': form }
    return render(request, 'voting/voting_room_form.html', context)