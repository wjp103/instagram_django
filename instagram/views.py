from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from instagram.models import *

def view_mainPage(request):
    context = dict()
    context['feeds'] = Board.objects.order_by("-post_data").select_related('user')
    context['comments'] = Comment.objects.all()
    context['feedlike'] = LikeBoard.objects.all() 
    return render(request, 'vietgram/feed.html', context)


def view_board_detail(request, id):
    context = dict()
    context['board'] = Board.objects.get(id=id)
    context['comments'] = Comment.objects.filter(board_id=id).order_by("-post_data").order_by("groud_id")
    context['feedlike'] = LikeBoard.objects.filter(board_id=id)
    context['commentlike'] = LikeComment.objects.filter(comment_id=id)
    return render(request, 'vietgram/detail.html', context)

def view_login_page(request):
    return render(request, "vietgram/index.html")


def Dologin(request):
    id = request.POST.get('name')
    pwd = request.POST.get('password')
    my_user = User.objects.get(username=id)

    if my_user.password == pwd:
        request.session['login_user'] = id
        return HttpResponse('Ok')
    else:
        return HttpResponse('failed')

def post_board_contents(request):
    user = User.objects.get(username = request.session['login_user'])
    board_id = request.POST.get("board_id")
    content = request.POST.get("content")
    comment = Comment()
    comment.content = content
    comment.board_id = board_id
    comment.user_id = user.id
    comment.depth = 1
    comment.groud_id = 0
    comment.save()
    comment_id = comment.id
    tmpComment = Comment.objects.get(id=comment_id)
    tmpComment.groud_id = comment_id
    tmpComment.save()
    return HttpResponse('Ok')


def post_comment_contents(request):
    user = User.objects.get(username = request.session['login_user'])
    board_id = request.POST.get("board_id")
    comment_id = request.POST.get("comment_id")
    content = request.POST.get("content")
    comment = Comment()
    comment.content = content
    comment.user_id = user.id
    comment.board_id = board_id
    comment.groud_id = comment_id
    comment.depth = 2
    comment.save()
    return HttpResponse('Ok')

def like_board(request, id):
    user = User.objects.get(username = request.session['login_user'])

    try:
        like_board = LikeBoard.objects.filter(user_id=user.id).get(board_id=id)
        if like_board:
            board = Board.objects.get(id=id)
            board.board_like -= 1
            like_board.delete()
            board.save()
    except:
        like_board = LikeBoard()
        like_board.user_id = user.id
        like_board.board_id = id
        like_board.save()
        board = Board.objects.get(id=id)
        board.board_like += 1
        board.save()
    return HttpResponse('ok')

def like_comment(request, id):
    user = User.objects.get(username = request.session['login_user'])

    try:
        like_comment = LikeComment.objects.filter(user_id=user.id).get(comment_id=id)
        if like_comment:
            comment = Comment.objects.get(id=id)
            comment.comment_like -=1
            comment.save()
            like_comment.delete()
    except:
        like_comment = LikeComment()
        like_comment.user_id = user.id
        like_comment.comment_id = id
        like_comment.save()
        comment = Comment.objects.get(id=id)
        comment.comment_like +=1
        comment.save()

    return HttpResponse('ok')