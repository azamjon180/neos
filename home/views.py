from django.shortcuts import render
from base import models

# Create your views here.

def home(request):
	template_name = 'home.html'
	slider = models.Slider.objects.all().order_by('-id')
	service = models.Service.objects.filter(home = True)
	about = models.About.objects.filter(home = True)
	product = models.Product.objects.filter(home = True)
	statis = models.Product.objects.filter(statis = True).order_by('-id')[0]
	testi = models.Person.objects.filter(category = "testi")
	blog = models.Blog.objects.filter(home = True).order_by('-id')
	context = {
		'slider' : slider,
		'service' : service,
		'about' : about,
		'product' : product,
		'statis' : statis,
		'testi' : testi,
		'blog' : blog
	}
	return render(request, template_name, context)


def service(request):
	template_name = 'services.html'
	service = models.Service.objects.all()
	banner = models.Banner.objects.get(link = 'service')
	statis = models.Product.objects.filter(statis = True).order_by('-id')[0]
	context = {
		'service' : service,
		'banner' : banner,
		'statis' : statis
	}
	return render(request, template_name, context)


def about(request):
	template_name = 'about.html'
	about = models.About.objects.all()
	banner = models.Banner.objects.get(link = 'about')
	context = {
		'about' : about,
		'banner' : banner
	}
	return render(request, template_name, context)


def blog(request):
	template_name = 'blog.html'
	blog = models.Blog.objects.all().order_by('-id')
	banner = models.Banner.objects.get(link = 'blog')
	context = {
		'blog' : blog,
		'banner' : banner,
	}
	return render(request, template_name, context)


def blogitem(request, blogid):
	template_name = 'blogsing.html'
	blog = models.Blog.objects.get(id = blogid)
	category = models.BlogCategory.objects.all()
	banner = models.Banner.objects.get(link = 'blog')
	context = {
		'blogid' : blogid,
		'blog' : blog,
		'category' : category,
		'banner' : banner,
	}
	return render(request, template_name, context)


def contact(request):
	template_name = 'contact.html'
	testi = models.Person.objects.filter(category = 'testi')
	banner = models.Banner.objects.get(link = 'contact')
	context = {
		'testi' : testi,
		'banner' : banner,
	}
	return render(request, template_name, context)


def product(request):
	template_name = 'product.html'
	product = models.Product.objects.all()
	banner = models.Banner.objects.get(link = 'product')
	context = {
		'product' : product,
		'banner' : banner,
	}
	return render(request, template_name, context)


def proitem(request, proid):
	template_name = 'prosing.html'
	product = models.Product.objects.get(id = proid)
	statis = models.Product.objects.filter(statis = True).order_by('-id')[0]
	banner = models.Banner.objects.get(link = 'product')
	context = {
		'product' : product,
		'statis' : statis,
		'banner' : banner,
	}
	return render(request, template_name, context)


def testi(request):
	template_name = 'testimonials.html'
	banner = models.Banner.objects.get(link = 'testi')
	testis = models.Person.objects.filter(category = 'testi')
	context = {
		'banner' : banner,
		'testis' : testis,
	}
	return render(request, template_name, context)