# -*-encoding:utf-8-*-
from telnetlib import IP

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from models import User, ToDo
from list import models


class UserForm(forms.Form):
    username = forms.CharField()
    mail = forms.EmailField()
    password = forms.CharField()
    password2 = forms.CharField()


class ToDoForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(required=False)
    date = forms.DateTimeField()


def register(req):
    if req.method == "POST":
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            mail = uf.cleaned_data['mail']
            password = uf.cleaned_data['password']
            password2 = uf.cleaned_data['password2']
            db_mail = models.User.objects.filter(mail=mail).first()
            if db_mail:
                return render_to_response('register.html', {'message': '该邮箱已注册'})
            else:
                if password == password2:
                    user = User()
                    user.username = username
                    user.mail = mail
                    user.password = password
                    user.save()
                    return HttpResponseRedirect('/login/')
                else:
                    return render_to_response('register.html', {'message': '两次密码不一致'})
    return render(req, 'register.html')


def login(req):
    if req.method == 'POST':
        mail = req.POST.get('mail')
        password = req.POST.get('password')
        user = models.User.objects.filter(mail=mail, password=password).first()
        if user:
            req.session['mail'] = user.mail
            req.session['username'] = user.username
            return HttpResponseRedirect('/create_todo/')
        else:
            return render_to_response('login.html', {'message': '邮箱或密码错误！'})
    return render(req, 'login.html')


def index(req):
    return render(req, 'index.html')


def create_todo(req):
    if req.session.get('mail'):
        user = models.User.objects.filter(mail=req.session.get('mail')).first()
        if req.method == 'POST':
            tdf = ToDoForm(req.POST)
            if tdf.is_valid():
                title = tdf.cleaned_data['title']  # 获取form表单中的值
                content = tdf.cleaned_data['content']
                date = tdf.cleaned_data['date']
                todo = ToDo()
                todo.title = title
                todo.content = content
                todo.date = date
                todo.user = user
                todo.save()
                return HttpResponseRedirect('/todo_list/')
        else:
            return render(req, 'create_todo.html')
    else:
        return render_to_response('login.html', {})


def logout(req):
    req.session.clear()
    return render(req, 'login.html')


def my_context_processor(req):
    user = models.User.objects.filter(mail=req.session.get('mail')).first()
    if user:
        return {'user': user}
    else:
        return {'user': None}


def todo_list(req):
    user = models.User.objects.filter(mail=req.session.get('mail')).first()
    todos = models.ToDo.objects.order_by('date').filter(user=user).all()
    return render(req, 'todo_list.html', {'todos': todos})


def detail(req, todo_id):
    user = models.User.objects.filter(mail=req.session.get('mail')).first()
    todo = models.ToDo.objects.filter(user=user, id=todo_id).first()
    return render(req, 'detail.html', {'todo': todo})


def detail_done(req, todo_done_id):
    user = models.User.objects.filter(mail=req.session.get('mail')).first()
    todo_done = models.ToDo.objects.filter(user=user, id=todo_done_id).first()
    return render(req, 'detail_done.html', {'todo_done': todo_done})


def operate(req):
    if req.method == 'POST':
        todo_id = req.POST['todo_id']
        if 'update' in req.POST:
            title = req.POST['title']
            content = req.POST['content']
            models.ToDo.objects.filter(id=todo_id).update(title=title, content=content)
            return HttpResponseRedirect('/todo_list/')
        else:
            models.ToDo.objects.filter(id=todo_id).delete()
            return HttpResponseRedirect('/todo_list/')
    return render(req, 'todo_list.html')


def operate_done(req):
    if req.method == 'POST':
        todo_id = req.POST['todo_id']
        models.ToDo.objects.filter(id=todo_id).delete()
        return HttpResponseRedirect('/todo_done/')
    return render(req, 'todo_done.html')


def done(req, todo_id):
    models.ToDo.objects.filter(id=todo_id).update(status='done')
    return HttpResponseRedirect('/todo_list/')


def todo_done(req):
    if req.session.get('mail'):
        user = models.User.objects.filter(mail=req.session.get('mail')).first()
        todo_dones = models.ToDo.objects.order_by('date').filter(user=user).all()
        return render(req, 'todo_done.html', {'todo_dones': todo_dones})
    else:
        return render_to_response('login.html', {})


def show_day(req, todo_id):
    user = models.User.objects.filter(mail=req.session.get('mail')).first()
    date = models.ToDo.objects.filter(id=todo_id).first().date
    todos_day = models.ToDo.objects.filter(user=user, date=date).all()
    return render(req, 'show_day.html', {'todos_day': todos_day, 'date': date})



