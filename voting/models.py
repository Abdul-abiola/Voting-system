from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Voting(models.Model):
#     name = models.CharField(max_length=200)
    
#     def __str__(self):
#         return self.name

# class Vote(models.Model):
#     host  = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
#     voting = models.ForeignKey(Voting, on_delete = models.SET_NULL, null=True)
#     candidate_party  = models.CharField(max_length=200)
#     candidate_name  = models.CharField(max_length=200)
#     # participants
    
#     def __str__(self):
#         return self.candidate_name
    
    
# class Voters(models.Model):
#     voting_room = models.ForeignKey(Vote, on_delete = models.CASCADE) 
#     updated = models.DateTimeField(auto_now=True)
    
# class User(models.Model):
#     user_voting = models.OneToOneField(Voters, on_delete= models.CASCADE)    
    
    
class Candidate(models.Model):
    name = models.CharField(max_length=100, unique=True)
    party = models.CharField(max_length =100, unique=True)
    
    
    
    def __str__(self):
        return f"{self.name} ({self.party})" 
    
   
    
class Vote(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vote')
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='votes')
    voted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} voted for {self.candidate.name}"        