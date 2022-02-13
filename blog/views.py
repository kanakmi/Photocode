from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import blog
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.models import User


@login_required
def blogs(request, slug):
    user = request.user
    data1 = blog.objects.filter(topic=slug)
    auth0user = user.social_auth.get(provider='auth0')
    data = {
        'user_id': auth0user.uid,
        'name': user.first_name,
        'picture': auth0user.extra_data['picture'],
        'email': auth0user.extra_data['email'],
        'datas': data1,
    }
    return render(request, 'blog.html', data)


@login_required
def new_blog(request):
    user = request.user
    if(request.method == 'POST'):
        ttle = request.POST.get('title')
        dcx = request.POST.get('description')
        tpc = request.POST.get('topic')
        temp = blog()
        temp.name = user
        temp.title = ttle
        temp.description = dcx
        temp.topic = tpc
        temp.save()
        return redirect('/blog')
    auth0user = user.social_auth.get(provider='auth0')
    data = {
        'user_id': auth0user.uid,
        'name': user.first_name,
        'picture': auth0user.extra_data['picture'],
        'email': auth0user.extra_data['email'],
    }
    return render(request, 'new_blog.html', data)


@csrf_exempt
def like(request):
    if request.is_ajax():
        message = "success"
        dta = request.POST.get('post_id')
        data = blog.objects.get(id=dta)
        data.likes += 1
        data.save()
        #print(dta, " Yes")
        return HttpResponse(message)
    else:
        print('no')


@login_required
def user_blog(request, slug):
    usr = User.objects.get(username=slug)
    print(usr)
    data = blog.objects.filter(name=usr)
    auth0user = usr.social_auth.get(provider='auth0')
    print(usr.first_name)
    datas = {
        'user_id': auth0user.uid,
        'name': usr.first_name,
        'picture': auth0user.extra_data['picture'],
        'email': auth0user.extra_data['email'],
    }
    context = {
        'datas': data,
        'usr': datas
    }
    return render(request, 'blog.html', context)


@login_required
def all_blogs(request):
    data = blog.objects.all()
    context = {
        'datas': data
    }

    return render(request, 'blog.html', context=context)


def my_blogs(request):
    user = request.user
    data = blog.objects.filter(name=user)
    context = {
        'datas': data,
        'my': True
    }
    return render(request, 'blog.html', context=context)
