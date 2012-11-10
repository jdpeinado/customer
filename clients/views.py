from clients.models import Company, Comment
from clients.forms import CompanyForm, CommentForm, ContactForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def about(request):
	html="<html><body>Example of project with django</body></html>"
	return HttpResponse(html)

def index(request):
	companies=Company.objects.all()
	return render_to_response('index.html', {'companies': companies}, context_instance=RequestContext(request))

def users(request):
    	users = User.objects.all()
    	companies = Company.objects.all()
    	return render_to_response('users.html',{'users':users,'companies':companies}, context_instance=RequestContext(request))

def list_companies(request):
	companies=Company.objects.all()
	return render_to_response('companies.html', {'data':companies}, context_instance=RequestContext(request))
	
def companies_details(request, id_company):
	data=get_object_or_404(Company, pk=id_company)
	comments=Comment.objects.filter(company=data)
	return render_to_response('company.html', {'company':data, 'comments':comments}, context_instance=RequestContext(request))

def contact(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            title = 'Message from customers'
            content = form.cleaned_data['message'] + "\n"
            content += 'Communicate to: ' + form.cleaned_data['email']
            email = EmailMessage(title, content, to=['receptor@email.com'])
            email.send()
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()
    return render_to_response('contactform.html',{'form':form}, context_instance=RequestContext(request))

def new_company(request):
    if request.method=='POST':
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/companies')
    else:
        form = CompanyForm()
    return render_to_response('companyform.html',{'form':form}, context_instance=RequestContext(request))


def new_comment(request):
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/companies')
    else:
        form = CommentForm()
    return render_to_response('commentform.html',{'form':form}, context_instance=RequestContext(request))

def new_user(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render_to_response('newuser.html',{'form':form}, context_instance=RequestContext(request))
    
def signin(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/private')
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            access = authenticate(username=username, password=password)
            if access is not None:
                if access.is_active:
                    login(request, access)
                    return HttpResponseRedirect('/private')
                else:
                    return render_to_response('noactive.html', context_instance=RequestContext(request))
            else:
                return render_to_response('nouser.html', context_instance=RequestContext(request))
    else:
        form = AuthenticationForm()
    return render_to_response('signin.html',{'form':form}, context_instance=RequestContext(request))

@login_required(login_url='/signin')
def private(request):
    user = request.user
    return render_to_response('private.html', {'user':user}, context_instance=RequestContext(request))

@login_required(login_url='/signin')
def close(request):
    logout(request)
    return HttpResponseRedirect('/')
