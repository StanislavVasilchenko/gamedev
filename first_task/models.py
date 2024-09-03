from datetime import datetime

from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=256, verbose_name="player_name", unique=True)
    email = models.EmailField(verbose_name="email", unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    first_login = models.DateTimeField(blank=True, null=True, verbose_name="first login")
    last_login = models.DateTimeField(blank=True, null=True, verbose_name="last login")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "player"
        verbose_name_plural = "players"
        ordering = ['-date_joined']

    def login_tracking(self):
        """"Отслеживание входа пользователя"""
        if not self.first_login:
            self.first_login = datetime.now()
        self.last_login = datetime.now()
        self.save()

    def add_boost(self, boost):
        """Добавление буста игроку"""
        player_boost = PlayerBoost(player=self, boost=boost)
        player_boost.save()


class Boost(models.Model):
    name = models.CharField(max_length=256, verbose_name="boost_name", unique=True)
    description = models.TextField(verbose_name="description")
    duration = models.PositiveIntegerField(verbose_name="duration")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "boost"
        verbose_name_plural = "boosts"


class PlayerBoost(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    boost = models.ForeignKey(Boost, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player.name} - {self.boost.name} - {self.date_added}"

    class Meta:
        verbose_name = "player-boost"
        verbose_name_plural = "player-boosts"
        ordering = ['-date_added']
