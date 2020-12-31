# from django.shortcuts import render,redirect
# from .models import User
# from django.contrib.auth import authenticate,login,logout
# from .forms import loginForm,registerForm
# # Create your views here.


# def show_users(request):
#     users = User.objects.all()
#     return render(request,'users.html',{'users':users})



# def not_valid(request):
#     return render(request,'not_valid.html')


# def user_login(request):
#     if request.method=='POST':
#         form = loginForm(request.POST)
#         if form.is_valid():
#             print('hello')
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user =authenticate(email=email,password=password)
#             print(user)
#             if user:
#                 login(request,user)
#                 return redirect('users')
#             else:
#                 return redirect('notvalid')
#     form = loginForm()
#     return render(request,'login.html',{'form':form})


# def user_logout(request):
#     logout(request)
#     return redirect('users')



# def register_user(request):
#     if request.method=='POST':
#         form = registerForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             User.objects.create(email=email,username=username,password=password)
#             return redirect('users')
#         else:
#             print('errors')
#             for e in form.errors:
#                 print(e)
#             print(form.errors)
#             return render(request,'register.html',{'errors':form.errors,'form':form})
#     form = registerForm()
#     return render(request,'register.html',{'form':form})
