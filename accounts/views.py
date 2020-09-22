from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from base import models



class SignUp(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'registration/signup.html'


@login_required
def profile(request):
	template_name = 'registration/profile.html'
	banner = models.Banner.objects.get(link = 'profile')
	context = {
		'banner' : banner
	}
	return render(request, template_name, context)


