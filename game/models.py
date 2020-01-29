from django.contrib.auth import get_user_model
from django.db import models


class Game(models.Model):
    weapons = (
        (2, '바위'),
        (1, '가위'),
        (0, '보')
    )
    attacker = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='attacker')
    defender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='defender')
    att_choice = models.IntegerField(choices=weapons)
    dfd_choice = models.IntegerField(choices=weapons, blank=True, null=True)
    att_at = models.DateTimeField(auto_now_add=True)
    winner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='winner', blank=True, null=True)
    loser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='loser', blank=True, null=True)
