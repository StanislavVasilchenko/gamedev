import csv
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from second_task.models import PlayerLevel, LevelPrize


def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="player_level.csv"'

    writer = csv.writer(response)
    writer.writerow(['Player ID', 'Level Name', 'Level completed', 'Prize Tittle',])

    player_levels = PlayerLevel.objects.select_related('player', 'level').prefetch_related('level__levelprize_set')

    for player_level in player_levels:
        prize_title = None
        try:
            level_prize = LevelPrize.objects.get(level=player_level.level)
            prize_title = level_prize.title
        except ObjectDoesNotExist:
            prize_title = "No Prize"

        writer.writerow([
            player_level.player.player_id,
            player_level.level.title,
            player_level.is_completed,
            prize_title
        ])

        return response


