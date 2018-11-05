from django.shortcuts import render
from . import forms
from accounts.forms import RegisterForm,ProfileForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail,EmailMessage

# Create your views here.
def home(request):
	value=request.GET.get('items')
	price=request.GET.get('total')

	# value=request.POST['items']
	# price=request.POST['total']
	print(value)
	print(price)
	if value is not None and price is not None:
		# msg=EmailMessage('Request Callback',
  #                      #'Here is the message.', to=['mailme.bidyadhar123@gmail.com'])
		# msg.send()
		send_mail("subject", value+price, settings.EMAIL_HOST_USER, ["mailme.bidyadhar123@gmail.com"],fail_silently=False)
	return render(request,'accounts/index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            print("success")
            # Redirect to a success page?
            return HttpResponseRedirect('/account/')
        else:
            print("failed")
            context = {'error': 'Wrong credintials'}  # to display error?
            return render(request, 'accounts/login.html', {'context': context})
    else:
        context = ''
        return render(request, 'accounts/login.html', {'context': context})

def register_user(request):
	if request.method == 'POST':
		register = RegisterForm(request.POST, prefix='register')
		usrprofile = ProfileForm(request.POST, prefix='profile')
		print(register.is_valid(),register.errors)
		print(usrprofile.is_valid())
		if register.is_valid() * usrprofile.is_valid():
		    user = register.save()
		    usrprof = usrprofile.save(commit=False)
		    usrprof.user = user
		    usrprof.set_token()
		    usrprof.subscribed = '1'
		    usrprof.save()
		    return HttpResponse('congrats')
		else:
		    messages.info(request, 'Password do not match!')
		    userform = RegisterForm(prefix='register')
		    userprofileform = ProfileForm(prefix='profile')
		    #return HttpResponse('errors')
		    return render(request, 'accounts/register.html', {'messages': messages.get_messages(request),'userform': userform, 'userprofileform': userprofileform})
	else:
	    userform = RegisterForm(prefix='register')
	    userprofileform = ProfileForm(prefix='profile')
	    return render(request, 'accounts/register.html', {'userform': userform, 'userprofileform': userprofileform})

def logout(request):
	#send_mail("subject", "value+price", settings.EMAIL_HOST_USER, ["mailme.bidyadhar123@gmail.com"],fail_silently=False)
	auth_logout(request)
	return HttpResponseRedirect('/account/')
