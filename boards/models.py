from django.db import models


class Board(models.Model):
    name = models.CharField('board name', max_length=10)
    description = models.CharField('board description', max_length=200)

    def __str__(self):
        return f'/{self.name}/'


class Thread(models.Model):
    theme = models.CharField('thread theme', max_length=190)
    message = models.TextField('thread message')
    date = models.DateTimeField('thread creation date')
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return self.theme if self.theme else 'no theme'


class Reply(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    date = models.DateTimeField('reply creation date')
    message = models.TextField('reply message')
    email = models.CharField('author email', max_length=190, blank=True, null=True)

    def __str__(self):
        return self.message
