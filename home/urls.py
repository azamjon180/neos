
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
	path('', views.home, name = 'home'),
	path('service/', views.service, name = 'service'),
	path('about/', views.about, name = 'about'),
	path('blog/', views.blog, name = 'blog'),
	path('contact/', views.contact, name = 'contact'),
	path('blog/<int:blogid>/', views.blogitem, name = 'blogitem'),
	path('product/', views.product, name = 'product'),
	path('product/<int:proid>/', views.proitem, name = 'proitem'),
	path('testi/', views.testi, name = 'testi'),
]

