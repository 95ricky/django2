from django.shortcuts import render, get_object_or_404
from myapp.models import Card, Heart, Board
from datetime import datetime
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from itertools import chain
from django.db.models.query import QuerySet
from django.db.models import Manager, Q
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from distributed.http.utils import redirect
from loginapp.models import User
from django.contrib import messages
from django.db.models.aggregates import Count


# Create your views here.

def indexFunc(request):
    return render(request, 'index.html')

def mainFunc(request): 
    CardTag = request.GET.get('tag')
    cdata = Card.objects.filter(card_tag__icontains = CardTag)

    paginator = Paginator(cdata, 3)
    page = request.GET.get('page')

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
        
    return render(request, 'main.html', {'card_data':data, 'cardtag':CardTag})
    



def MSearchFunc(request):
    CardCo = request.GET.get("CardCo")
    CardKind = request.GET.get("CardKind")
    CardTag = request.GET.get('tag')

    CardColist = ['우리','신한','농협','현대','삼성','국민']
    if CardCo in CardColist: 
        if CardKind == 'check': 
            cdata = Card.objects.filter(card_tag__icontains = CardTag, card_type = CardKind, card_co = CardCo)
            
        elif CardKind == 'credit': 
            cdata = Card.objects.filter(card_tag__icontains = CardTag, card_type = CardKind, card_co = CardCo)
            
        else:
            cdata = Card.objects.filter(card_tag__icontains = CardTag, card_co = CardCo)
    
    else: 
        if CardKind == 'check': 
            cdata = Card.objects.filter(card_tag__icontains = CardTag, card_type = CardKind)
            
        elif CardKind == 'credit': 
            cdata = Card.objects.filter(card_tag__icontains = CardTag, card_type = CardKind)

        else:
            cdata = Card.objects.filter(card_tag__icontains = CardTag)


    paginator = Paginator(cdata, 3) 
    page = request.GET.get('page')

    try:
        data = paginator.page(page)
    except PageNotAnInteger: 
        data = paginator.page(1)
    except EmptyPage: 
        data = paginator.page(paginator.num_pages)

    return render(request, 'main.html', {'card_data':data ,'cardtag':CardTag})


def compareFunc(request):
    result1 = request.GET.get('code')
    data = Card.objects.filter(card_code = result1);

    return render(request, 'cardcompare.html', {'cresult':data})


def comparechoiceFunc(request):  
    queryset = Card.objects.all()
    return render(request, 'cardcomparechoice.html', {'cdata':queryset})


def comparechoice2Func(request):
    queryset2 = Card.objects.all()  
    return render(request, 'cardcomparechoice2.html', {'cdata':queryset2})


def showFunc(request):
    data = Card.objects.filter(card_index = request.GET.get('idx'))
    data2 = Board.objects.filter(card_index = request.GET.get('idx')).order_by('-board_code')
    index = request.GET.get('idx')
    
    return render(request, 'card.html', {'card_data2':data, 'board_data':data2, 'index' : index})


@csrf_exempt
def writesingupFunc(request):
    if request.method == 'POST':
        cindex = get_object_or_404(Card, card_index = request.POST.get('signok'))
        index = request.POST.get('signok')

        Board(
            board_title = request.POST.get('title'),
            board_write = request.POST.get('comment'),
            card_index = get_object_or_404(Card, card_index = request.POST.get('signok')),
            board_date = datetime.now()
        ).save()
        
        return HttpResponseRedirect('/cardshow?idx=' + index)


def loginFunc(request):
    return render(request, 'login.html')


@csrf_exempt
def findIDFunc(request):
    if request.method == 'GET':
        return render(request, 'findID.html')
        
    elif request.method == 'POST':
        find_name = request.POST.get('name')
        find_email = request.POST.get('email')
        emailChecked = False
    
        try :     
            dataFindID = User.objects.filter(customer_name = find_name, customer_email = find_email)

            if dataFindID != None :
                emailChecked = True
    
        except Exception as e:
            print('err:',e)
    
        context = {'email' : emailChecked}

        return HttpResponse(json.dumps(context), content_type = "application/json")
        
    else:
        return render(request, 'error.html')


@csrf_exempt    
def findID(request):
    if request.method == 'POST':
        customer_name = request.POST.get("name")
        customer_email = request.POST.get("email")
        user = User.objects.get(customer_name = customer_name)
        if user is not None:
            return render(request, 'IDresult.html', {'user':user})
    
        else:
            return HttpResponse('findID failed. Try again.')
    else:
        return render(request, 'video/user_login.html')


@csrf_exempt    
def findPWFunc(request):
    if request.method == 'GET':
        return render(request, 'findPW.html')
        
    elif request.method == 'POST':
        find_id = request.POST.get('id')
        find_name = request.POST.get('name')
        find_email = request.POST.get('email')
        emailChecked = False
    
        try :     
            dataFindPW = User.objects.filter(username = find_id, customer_name = find_name, customer_email = find_email)
    
            if dataFindPW != None :
                emailChecked = True
    
        except Exception as e:
            print('err:',e)
    
    
        context = {'email' : emailChecked}
    
        return HttpResponse(json.dumps(context), content_type = "application/json")
        
    else:
        return render(request, 'error.html')

@csrf_exempt
def findPW(request):
    if request.method == 'POST':
        username = request.POST.get("id")
        customer_name = request.POST.get("name")
        customer_email = request.POST.get("email")
        
        users = User.objects.all().filter(customer_email = customer_email)

        if users is not None:
            return render(request, 'PWresult.html', {'users':users})
    
        else:
            return HttpResponse('findPW failed. Try again.')
    else:
        return render(request, 'video/user_login.html')


@csrf_exempt
def IdDbFunc(request):
    id = request.POST.get('id')
    isRegister = True
    try :
        data = User.objects.get(username = id)
        if data != None:
            isRegister = False
    except Exception as e:
        print('err', e)
        
    context = {'id' : isRegister}
    

    return HttpResponse(json.dumps(context), content_type = "application/json")

def signupFunc(request):
    if request.method == 'GET':
        return render(request, 'signUp.html')
    elif request.method == 'POST':
        
        #ORM
        User(
            username = request.POST.get('id_input'),
            password = request.POST.get('password'),
            customer_name = request.POST.get('name'),
            customer_email = request.POST.get('email'),
            customer_birth = request.POST.get('birthday')
                   
        ).save()
        return render(request, 'login.html')

    else:
        return render(request, 'error.html')

    

def okloginFunc(request):
    uname = request.GET.get('uname') 
    code = request.GET.get('code') 
    index = get_object_or_404(Card, card_index = request.GET.get('idx'))
    
    if request.method == 'GET':
        if Heart.objects.filter(card_index = index, username = uname):
            return render(request, 'alreadyexist.html')
            
        elif len(Heart.objects.filter(username=uname)) == 4:                
            return render(request, 'hearterror.html')
        
        else:
            Heart(
                username = uname,
                card_index = index 
                ).save()            
            return render(request, 'okheart.html')


def mypageFunc(request):
    card = Card.objects.all()
    uname = request.GET.get('uname')  #qwe123
    heart = Heart.objects.filter(username=uname)

    list= []
    for row in heart.values_list():
        print(row[2]) 
        list.append(row[2]) #4,2,3,5
    card = Card.objects.filter(card_index__in=list)  #sql의 in연산자

    return render(request, 'mypage.html', {'card':card})


def DeleteFunc(request):
    uname = request.GET.get('uname')
    idx = request.GET.get('index')
    item = Heart.objects.get(username=uname, card_index=idx)
    item.delete()
    
    return HttpResponseRedirect('/mypage?uname=' + uname)


def moreFunc(request):
    data2 = Board.objects.filter(card_index = request.GET.get('idx')).order_by('-board_code')

    return render(request, 'morecomment.html', {'board_data':data2})