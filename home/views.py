from django.shortcuts import render
from base import models
from django.core.paginator import Paginator

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
	hlove = models.Message.objects.get(link = 'hlove')
	hshare = models.Message.objects.get(link = 'hshare')
	htesti = models.Message.objects.get(link = 'htesti')
	hresent = models.Message.objects.get(link = 'hresent')
	context = {
		'slider' : slider,
		'service' : service,
		'about' : about,
		'product' : product,
		'statis' : statis,
		'testi' : testi,
		'blog' : blog,
		'hlove' : hlove,
		'hshare' : hshare,
		'htesti' : htesti,
		'hresent' : hresent,
		
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
	paginator = Paginator(blog, 3)
	page = request.GET.get('page')
	blog = paginator.get_page(page)
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
	contactinfo = models.Message.objects.get(link = 'contactinfo')
	address = models.Message.objects.get(link = 'address')
	phone = models.Message.objects.get(link = 'phone')
	email = models.Message.objects.get(link = 'email')
	context = {
		'testi' : testi,
		'banner' : banner,
		'contactinfo' : contactinfo,
		'address' : address,
		'phone' : phone,
		'email' : email,
	}
	return render(request, template_name, context)


def product(request):
	template_name = 'product.html'
	product = models.Product.objects.all()
	banner = models.Banner.objects.get(link = 'product')
	paginator = Paginator(product, 3)
	page = request.GET.get('page')
	product = paginator.get_page(page)
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


def gallery(request):
	template_name = 'gallery.html'
	image = models.Gallery.objects.all()
	banner = models.Banner.objects.get(link = 'gallery')
	context = {
		'image' : image,
		'banner' : banner,
	}
	return render(request, template_name, context)