from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .forms import TaskForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Task


@csrf_exempt
def index(request):
	return render(request, 'index.html')


def signup(request):
	if request.method == "POST":
		fname = request.POST.get('firstName')
		lname = request.POST.get('lastName')
		uname = request.POST.get('Username')
		email = request.POST.get('emailAddress')
		password = request.POST.get('password')
		confirmpassword = request.POST.get('confirm password')
		user = User.objects.create_user(username=uname, email=email, password=password, first_name=fname,
										last_name=lname)
		user.save()
		return redirect('/login/')

	return render(request, 'signIn.html')


def signIn(request):
	if request.method == "POST":
		form = AuthenticationForm(data=request.POST)
		if form.is_valid:
			return redirect('/')
	else:
		form = AuthenticationForm()
	return render(request, 'signup.html', {'form': form})


def blog(request):
	return render(request, 'blog.html')


def login(request):
	if request.method == "POST":
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			return redirect('/addnote')
	else:
		form = AuthenticationForm()
	return render(request, 'login.html', {'form': form})


def subject(request):
	return render(request, 'subject.html')


def ict(request):
	return render(request, 'ict.html')


def addnote(request):
	title = Task.objects.all()
	form = TaskForm()
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			_form = form.save(commit=False)
			_form.completed = False
			_form.user = request.user
			_form.save()
			return redirect('/notes/')
	else:
		form = TaskForm()
	return render(request, 'addnote.html', {'title': title})


def notes(request):
	tasks = Task.objects.all()
	return render(request, 'notes.html', {'tasks': tasks})


def delete(request, id):
	title = Task.objects.get(id=id)
	title.delete()
	return redirect('notes')


def update(request, id):
	context = {}
	title = Task.objects.get(id=id)
	updateForm = TaskForm(instance=title)
	if request.method == 'POST':
		updateForm = TaskForm(request.POST)
		if updateForm.is_valid():
			updateForm.save()
		return redirect('/addnote/')
	context["updateForm"] = updateForm
	return render(request, 'update.html', context)


class TaskUpdate(UpdateView):
	model = Task


class TaskDelete(DeleteView):
	model = Task
