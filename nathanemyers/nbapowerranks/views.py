from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Team, Ranking

# Create your views here.
def chart(request):
    return render(request, 'chart/nba_power_rankings.html')

def week_rankings(request, year, week):
    rankings = Ranking.objects.filter(year=year, week=week)
    formatted_rankings = {}
    for rank in rankings:
        formatted_rankings[rank.team.name] = rank.rank

    return JsonResponse({'rankings': formatted_rankings})

def year_rankings(request, year):
    rankings = Ranking.objects.filter(year=year)
    formatted_rankings = {}
    for rank in rankings:
        if rank.team.name in formatted_rankings:
            formatted_rankings[rank.team.name].append(rank.rank)
        else:
            formatted_rankings[rank.team.name] = [rank.rank]

    return JsonResponse({'rankings': formatted_rankings})
