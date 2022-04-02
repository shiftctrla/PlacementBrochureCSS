from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm
from django.contrib import messages


def registration_view(request):

	if request.user.is_authenticated:
		messages.error(request, 'You must log out to register a new account.')
		return redirect('home')

	context = {}

	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()

			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')

			account = authenticate(email=email, password=raw_password)
			login(request, account)

			messages.success(request, 'Account created. You have been logged in.')
			return redirect('home')
		else:
			context['registration_form'] = form
	else:
		form = RegistrationForm()
		context['registration_form'] = form

	return render(request, 'account/register.html', context)


def logout_view(request):
	if not request.user.is_authenticated:
		return redirect('home')
	logout(request)
	messages.success(request, 'You have successfully logged out.')
	return redirect('home')


def login_view(request):

	context = {}
	user = request.user

	if user.is_authenticated:
		messages.info(request, 'You are already logged in.')
		return redirect('home')

	if request.POST:
		form = AccountAuthenticationForm(request.POST)

		if form.is_valid():

			email = request.POST['email']
			password = request.POST['password']

			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				messages.success(request, 'You have been successfully logged in.')
				return redirect('home')

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form
	return render(request, 'account/login.html', context)


def dashboard_view(request):

	if not request.user.is_authenticated:
		messages.error(request, 'You must be logged in to access your dashboard.')
		return redirect('login')

	return render(request, 'account/dashboard.html', {})
