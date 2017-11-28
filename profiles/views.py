from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
def home(request):
	context = {}
	temlates = 'home.html'
	return render(request,temlates,context)

def about(request):
	context = {}
	temlates = 'about.html'
	return render(request,temlates,context)	


@login_required
def userProfile(request):
	user = request.user
	context = {'user': user}
	temlates = 'profile.html'
	return render(request,temlates,context)	
