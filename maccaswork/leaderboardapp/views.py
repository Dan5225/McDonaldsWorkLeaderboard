from django.shortcuts import render
from django.db.models import Max
from .models import Tehs

def leaderboard(request):
    participants = Tehs.objects.select_related(
        'participant',
        'participant__first_name',
        'participant__last_name'
    ).order_by('-tehs')

    last_updated = Tehs.objects.aggregate(
        latest_update=Max('updated_at')
    )['latest_update']

    return render(
        request,
        'leaderboardapp/leaderboard.html',
        {
            'participants': participants,
            'last_updated': last_updated,
        }
    )