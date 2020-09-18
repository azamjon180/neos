
from base import models

def menu(request):
	genres = models.Genre.objects.all()
	context = {
		'genres' : genres
	}
	return context


