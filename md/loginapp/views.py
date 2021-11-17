from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
import json
from django.contrib.auth import authenticate
from django.contrib import auth
from loginapp.models import User
from django.contrib.auth import get_user_model


def LoginView(request):
    return render(request, 'login.html')


@csrf_exempt
def LoginFunc(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    elif request.method == 'POST':
            
        lg_id = request.POST.get('id')
        #print(lg_id) ok
        lg_passwd = request.POST.get('password')
        #print(lg_passwd) ok
        idChecked = False
        psChecked = False

        try :     
            dataID = User.objects.get(username = lg_id, password = lg_passwd)
            #print(dataID) ok
            if dataID != None :
                idChecked = True                     
        except Exception as e:
            print('err:',e)
            
        try :
            dataPS = User.objects.filter(username=lg_id, password = lg_passwd).exists()
            #print(dataPS)    
            if dataPS == True:
                psChecked = True        
        except Exception as e:
            print('err:',e)    

        context = {'id' : idChecked, 'password':psChecked}

        #print(context)
        return HttpResponse(json.dumps(context), content_type = "application/json")


    
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        print(username)
        #password = request.POST.get("password")
        #print(password)
        #print(get_user_model())
        user = User.objects.get(username = username)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return HttpResponse('Login failed. Try again.')
    else:
        return render(request, 'video/user_login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('/')
