from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from .models import Board


def home(request):
    boards = Board.objects.all()
    boards_names = list()

    for board in boards:
        boards_names.append(board.name)

    return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board': board})


def about(request):
    # do something...
    return render(request, 'about.html')


def about_company(request):
    # do something...
    return render(request, 'aout_company.html', {'company_name': 'Simple Company'})
