from datetime import datetime

from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=256, verbose_name="player_name", unique=True)
    email = models.EmailField(verbose_name="email", unique=True)
    first_login = models.DateTimeField(blank=True, null=True, verbose_name="first login")
    last_login = models.DateTimeField(blank=True, null=True, verbose_name="last login")
    boosts = models.ManyToManyField('Boost', related_name='players', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "player"
        verbose_name_plural = "players"
        ordering = ['-first_login']

    def login_tracking(self):
        """"Отслеживание входа пользователя"""
        if not self.first_login:
            self.first_login = datetime.now()
        self.last_login = datetime.now()
        self.save()

    def add_boost(self, boost):
        """Добавление буста игроку"""
        self.boosts.add(boost)


class Boost(models.Model):
    name = models.CharField(max_length=256, verbose_name="boost_name", unique=True)
    description = models.TextField(verbose_name="description")
    duration = models.PositiveIntegerField(verbose_name="duration")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "boost"
        verbose_name_plural = "boosts"
