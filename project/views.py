from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.models import Permission

from django.contrib import messages


def signup(request) -> HttpResponse:
    """Allow users to add a new todo list to the group they're in.
    """

    # Only staffers can add lists, regardless of TODO_STAFF_USER setting.
    if request.POST:
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        # print(user, pwd)
        try:
            test = User.objects.get(username = user)
            # print(test)
            if test is not None:
                messages.info(request, f"注册失败，该用户已存在，ID:{test.id}")
                # print("ttttt")
                return redirect('signup')
        except:
            pass
        try:
            
            user = User.objects.create_user(username=user, password=pwd)
        # all_permissions = Permission.objects.all()
        # for perm in all_permissions:
        #     user.user_permissions.add(perm)
            user.is_staff = True

            user.save()
        except:
            messages.info(request, "注册失败")
            redirect('signup')
            
        if user:            
            auth.login(request, user) 
            return redirect('todo:lists')
    return render(request, 'registration/signup.html')


def login(request):
    user = None
    if request.user.is_authenticated:
        return redirect('todo:lists')    
        
    if request.method == 'POST':        
        username = request.POST.get('username')        
        password = request.POST.get('password')
        try:
               
            user = auth.authenticate(username=username, password=password)        
    # if user is not None:            
            auth.login(request, user)  #这里做了登录
        except:
            messages.info(request, "登陆失败，用户名或密码错误")
            return redirect('login')    
            
        # print(user.id)
        return redirect('todo:lists')    
       
    return render(request, "registration/signin.html")



def logout(request):
    auth.logout(request)
    
    return redirect('login')