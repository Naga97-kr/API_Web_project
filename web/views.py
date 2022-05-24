# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password , make_password


def index(request):
    return render(request,"index.html")

def indexin(request):
    return render(request,"indexin.html")

def weather(request):
    return render(request,"weather.html")

def register(request):
    if request.method == 'POST':
        if request.POST['pw'] == request.POST['pw-confirm']:
            user = User (
                        user_id=request.POST['id'],
                        pwd=request.POST['pw'],
                        name=request.POST['name'],
                        gender=request.POST['gender'],
                        addr=request.POST['addr'],
                        birth=request.POST['birth'],
                        email=request.POST['email'],
                        )
            user.save()
            return redirect('/')
        return render(request, 'register.html')
    return render(request, 'register.html')

def login(request):
    response_data = {}

    if request.method == "GET" :
        return render(request, 'login.html')

    elif request.method == "POST":
        login_username = request.POST.get('user_id')
        login_password = request.POST.get('pwd')

        if not (login_username and login_password):
            response_data['error']="아이디와 비밀번호를 모두 입력해주세요."
        else:
            user = User.objects.get(user_id=login_username)
            upwd = user.pwd
            checkpwd = login_password
            if (upwd == checkpwd):
                print(upwd, checkpwd)
                request.session['user'] = user.id 
                #세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                #세션 user라는 key에 방금 로그인한 id를 저장한것.
                return render(request, 'indexin.html',response_data)
            else:
                response_data['error'] = "비밀번호를 틀렸습니다."


    return redirect('/')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')

def home(request):
    user_id = request.session.get('user')
    if user_id :
        user_info = User.objects.get(pk=user_id)
        return HttpResponse(user_info.user_id)
    
    return HttpResponse('로그인을 해주세요')

def board(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['contents']
        user = request.user
        board = Board(
            title=title,
            content=content,
            user=user,
        )
        board.save()
        return redirect('board')
    else:
        boardForm = BoardForm
        board = Board.objects.all()
        context = {
            'boardForm' : boardForm,
            'board': board,
        }

        return render(request, 'board.html', context)

def boardEdit(request, pk):
    board = Board.objects.get(id=pk)
    if request.method == "POST":
        board.title = request.POST['title']
        board.content = request.POST['content']
        board.writer = request.user

        board.save()
        return redirect('board')

    else:
        boardForm = BoardForm
        return render(request, 'update.html',{'boardForm':boardForm})

def boardDelete(request, pk):
    board = Board.objects.get(id=pk)
    board.delete()
    return redirect('board')

def bd_write(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        board = Board(
            title=title,
            content=content,
        )
        board.save()
        return redirect('bd_write.html')

    else :
        boardForm = BoardForm
        board = Board.objects.all()
        context = {
            'boardForm' : boardForm,
                'board': board,
            }

    return render(request, 'bd_write.html', context)

def intro(request):
    return render(request,'intro.html')

def bd_list(request):
    board = Board.objects.all()
    context = {'board':board}

    return render(request, 'bd_list.html',context)