from django.shortcuts import render
from . import forms
from accounts.forms import RegisterForm,ProfileForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string,get_template
from django.utils.html import strip_tags
from django.template import Context
# Create your views here.
def home(request):
	value=request.GET.get('items')
	price=request.GET.get('total')

	# value=request.POST['items']
	# price=request.POST['total']
	# print("value="+value)
	# print(price)
	if value is not None and price is not None:
		# msg=EmailMessage('Request Callback',
  #                      #'Here is the message.', to=['mailme.bidyadhar123@gmail.com'])
		# msg.send()
		array=value.splitlines();
		gbnc=""
		nc8b=""
		nc3b=""
		nc7b=""
		for val in array:
			if "Girls Block NC" in val:
				gbnc+=val
				gbnc+='\n'
			elif "3rd Block NC" in val:
				nc3b+=val
				nc3b+='\n'
			elif "8th Block NC" in val:
				nc8b+=val
				nc8b+='\n'
			elif "7th Block NC" in val:
				nc7b+=val
				nc7b+='\n'
		if gbnc != "":
			temp=gbnc.splitlines()

			gbnc_tot=0
			for val in temp:
				gbnc_tot+=int(val.split(',')[1])*int(val.split(',')[2])
			#temp.append(gbnc_tot)
			print(temp)
			item=[]
			price=[]
			quant=[]
			name=[]
			prods=[]
			for i in temp:
				l=i.split(",")
				item.append(l[0])
				price.append(l[2])
				quant.append(l[1])
				name.append(l[3])
				prods.append([l[0],l[1],l[2],l[3]])
			#return render(request,'accounts/email.html', {'prods':prods,'price':price,'quant':quant,'name':name,'total':gbnc_tot,"user":request.user})

			#html_message=get_template('accounts/email.html').render(Context(prods))
			html_message = render_to_string('accounts/email.html', {'prods':prods,'item':item,'price':price,'quant':quant,'name':name,'total':gbnc_tot,"user":request.user})
			#plain_message = strip_tags(html_message)
			plain_message=render_to_string('accounts/email.txt', {'prods': prods})
			s=""
			for val in temp:
				if type(val) is int:
					s+=str(val)+'\n'
				else:
					s+=val+'\n'
			#print(s)
			send_mail("GBNC ORDER", s, settings.EMAIL_HOST_USER, ["mailme.bidyadhar123@gmail.com"],html_message=html_message)

		if nc8b != "":
			temp=nc8b.splitlines()
			nc8b_tot=0
			for val in temp:
				nc8b_tot+=int(val.split(',')[1])*int(val.split(',')[2])
			#temp.append(nc8b_tot)
			print(temp)
			item=[]
			price=[]
			quant=[]
			name=[]
			prods=[]
			for i in temp:
				l=i.split(",")
				item.append(l[0])
				price.append(l[2])
				quant.append(l[1])
				name.append(l[3])
				prods.append([l[0],l[1],l[2],l[3]])
			#return render(request,'accounts/email.html', {'prods':prods,'price':price,'quant':quant,'name':name,'total':gbnc_tot})

			html_message = render_to_string('accounts/email.html', {'prods':prods,'item':item,'price':price,'quant':quant,'name':name,'total':nc8b_tot,"user":request.user})
			plain_message = strip_tags(html_message)
			# s=""
			# for val in temp:
			# 	if type(val) is int:
			# 		s+=str(val)+'\n'
			# 	else:
			# 		s+=val+'\n'
			#print(s)
			send_mail("8th Block NC ORDER", plain_message, settings.EMAIL_HOST_USER, ["mailme.bidyadhar123@gmail.com"],html_message=html_message)

		if nc7b != "":
			temp=nc7b.splitlines()
			nc7b_tot=0
			for val in temp:
				nc7b_tot+=int(val.split(',')[1])*int(val.split(',')[2])
			#temp.append(nc7b_tot)
			print(temp)
			item=[]
			price=[]
			quant=[]
			name=[]
			prods=[]
			for i in temp:
				l=i.split(",")
				item.append(l[0])
				price.append(l[2])
				quant.append(l[1])
				name.append(l[3])
				prods.append([l[0],l[1],l[2],l[3]])
			#return render(request,'accounts/email.html', {'prods':prods,'price':price,'quant':quant,'name':name,'total':gbnc_tot})

			html_message = render_to_string('accounts/email.html', {'prods':prods,'item':item,'price':price,'quant':quant,'name':name,'total':nc7b_tot,"user":request.user})
			plain_message = strip_tags(html_message)
			# s=""
			# for val in temp:
			# 	if type(val) is int:
			# 		s+=str(val)+'\n'
			# 	else:
			# 		s+=val+'\n'
			#print(s)
			send_mail("7th Block NC ORDER", plain_message, settings.EMAIL_HOST_USER, ["mailme.bidyadhar123@gmail.com"],html_message=html_message)

		if nc3b != "":
			temp=nc3b.splitlines()
			nc3b_tot=0
			for val in temp:
				nc3b_tot+=int(val.split(',')[1])*int(val.split(',')[2])
			#temp.append(nc3b_tot)
			print(temp)
			item=[]
			price=[]
			quant=[]
			name=[]
			prods=[]
			for i in temp:
				l=i.split(",")
				item.append(l[0])
				price.append(l[2])
				quant.append(l[1])
				name.append(l[3])
				prods.append([l[0],l[1],l[2],l[3]])
			#return render(request,'accounts/email.html', {'prods':prods,'price':price,'quant':quant,'name':name,'total':gbnc_tot})

			html_message = render_to_string('accounts/email.html', {'prods':prods,'item':item,'price':price,'quant':quant,'name':name,'total':nc3b_tot,"user":request.user})
			plain_message = strip_tags(html_message)
			# s=""
			# for val in temp:
			# 	if type(val) is int:
			# 		s+=str(val)+'\n'
			# 	else:
			# 		s+=val+'\n'
			#print(s)
			send_mail("3rd Block ORDER", plain_message, settings.EMAIL_HOST_USER, ["mailme.bidyadhar123@gmail.com"],html_message=html_message)


		

		##send_mail("subject", value+price, settings.EMAIL_HOST_USER, ["mailme.bidyadhar123@gmail.com"],fail_silently=False)
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
		    return HttpResponseRedirect('/account/')
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
	##send_mail("subject", "value+price", settings.EMAIL_HOST_USER, ["mailme.bidyadhar123@gmail.com"],fail_silently=False)
	auth_logout(request)
	return HttpResponseRedirect('/account/')
