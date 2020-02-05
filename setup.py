from django.contrib.auth.models import User

User.objects.create_superuser('admin', 'mikhail@example.com', 'assword')

from .boards.models import Board

Board.objects.create(name='b', description='Random')
Board.objects.create(name='pony', description='My Little Pony')
Board.objects.create(name='rns', description='Russian National State')