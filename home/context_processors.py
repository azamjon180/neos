
from base import models
from django.shortcuts import get_object_or_404

def menu(request):
	genres = models.Genre.objects.all()
	btry = models.Message.objects.get(link = 'btry')
	contactus = models.Message.objects.get(link = 'contactus')
	babout = models.Message.objects.filter(link = 'babout')[0]
	bquick = models.Message.objects.get(link = 'bquick')
	bfree = models.Message.objects.get(link = 'bfree')
	bsocial = models.Message.objects.get(link = 'bsocial')
	bstay = models.Message.objects.get(link = 'bstay')
	copy = models.Message.objects.get(link = 'copy')
	subscribe = models.Message.objects.get(link = 'subscribe')
	context = {
		'genres' : genres,
		'btry' : btry,
		'contactus' : contactus,
		'babout' : babout,
		'bquick' : bquick,
		'bfree' : bfree,
		'bsocial' : bsocial,
		'bstay' : bstay,
		'copy' : copy,
		'subscribe' : subscribe,
	}
	return context


