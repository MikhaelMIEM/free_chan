from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
import datetime


from .models import Board, Thread, Reply


def root(request):
    board_list = Board.objects.all()
    return render(request, 'main.html', {'board_list': board_list})


def boards(request, board_name):
    try:
        board = Board.objects.get(name=board_name)
    except:
        raise Http404()
    threads = Thread.objects.filter(board=board).order_by('-date')
    threads_and_last_replies = []
    for thread in threads:
        thread_and_last_replies = {}
        thread_and_last_replies['thread'] = thread
        thread_and_last_replies['replies'] = reversed(Reply.objects.filter(thread=thread).order_by('-date')[:3])
        threads_and_last_replies.append(thread_and_last_replies)
    return render(request, 'board.html', {'board': board, 'threads_and_last_replies': threads_and_last_replies})


def threads(request, board_name, thread_id):
    try:
        thread = Thread.objects.get(id=thread_id)
        board = Board.objects.get(name=board_name)
    except:
        raise Http404()
    replies = Reply.objects.filter(thread=thread)
    return render(request, 'thread.html', {'thread': thread, 'replies': replies, 'board': board})


def create_thread(request, board_name):
    try:
        board = Board.objects.get(name=board_name)
    except:
        raise Http404()
    thread = Thread.objects.create(message=request.POST['message'], theme=request.POST['theme'], board=board,
                                   date=datetime.datetime.now())
    return HttpResponseRedirect(reverse('boards:threads', args=(board.name, thread.id)))


def leave_reply(request, board_name, thread_id):
    try:
        thread = Thread.objects.get(id=thread_id)
        board = Board.objects.get(name=board_name)
    except:
        raise Http404()
    Reply.objects.create(message=request.POST['message'], email=request.POST['email'], date=datetime.datetime.now(),
                         thread=thread)
    return HttpResponseRedirect(reverse('boards:threads', args=(board.name, thread.id)))