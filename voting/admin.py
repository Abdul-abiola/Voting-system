from django.contrib import admin

# Register your models here.
from .models import Vote, Candidate

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'party', 'get_total_votes')
    
    def get_total_votes(self, obj):
        return obj.votes.count()
    
    get_total_votes.short_description = 'Total Votes cast'


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'candidate', 'voted_at')
    list_filter = ('candidate', 'candidate__party')