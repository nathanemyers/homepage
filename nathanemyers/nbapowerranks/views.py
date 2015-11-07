from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Team, Ranking

# Create your views here.

def rankings(request, year, week):
    rankings = Ranking.objects.filter(year=year, week=week)
    formatted_rankings = {}
    for rank in rankings:
        formatted_rankings[rank.team.name] = rank.rank

    return JsonResponse({'rankings': formatted_rankings})
