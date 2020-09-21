from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey

class Genre(MPTTModel):
	name = models.CharField(max_length = 256, unique = True)
	parent = TreeForeignKey('self', on_delete = models.CASCADE, null = True, blank = True, related_name = 'children')
	link = models.CharField(max_length = 256, null = True, blank = True)
	order = models.IntegerField(null = True, blank = True)

	class MPTTMeta:
		order_insertion_by = ['order']

	class Meta:
		verbose_name = 'Menu'

	def __str__(self):
		return self.name


class Slider(models.Model):
	title = models.TextField()
	image = models.ImageField(upload_to = 'slider')

	class Meta:
		verbose_name = 'Slider'

	def __str__(self):
		return self.title


class Service(models.Model):
	title = models.TextField()
	description = models.TextField(null = True, blank = True)
	icon = models.TextField(null = True, blank = True)
	home = models.BooleanField(default = False)

	class Meta:
		verbose_name = 'Servislar'

	def __str__(self):
		return self.title


class About(models.Model):
	title = models.TextField()
	description = models.TextField(null = True, blank = True)
	text = models.TextField(null = True, blank = True)
	image = models.ImageField(upload_to = 'about', null = True, blank = True)
	home = models.BooleanField(default = False)
	right = models.BooleanField(default = False)

	class Meta:
		verbose_name = 'Kompaniya haqida'

	def __str__(self):
		return self.title


class Product(models.Model):
	name = models.TextField()
	description = models.TextField(null = True, blank = True)
	content = models.TextField(null = True, blank = True)
	image = models.ImageField(upload_to = 'product', null = True, blank = True)
	price = models.DecimalField(max_digits = 10, decimal_places = 2, null = True, blank = True)
	number = models.IntegerField(null = True, blank = True)
	home = models.BooleanField(default = False)
	statis = models.BooleanField(default = False)

	class Meta:
		verbose_name = 'Mahsulotlar'

	def __str__(self):
		return self.name


class Person(models.Model):
	category_choices = (("team","Team"), ("testi","Testimonials"), ("auth", "Author"))
	category = models.CharField(max_length = 50, choices = category_choices)
	name = models.CharField(max_length = 256)
	description = models.TextField(null = True, blank = True)
	position = models.TextField(null = True, blank = True)
	image = models.ImageField(upload_to = 'person', null = True, blank = True)

	class Meta:
		verbose_name = 'Person'

	def __str__(self):
		return self.name


class BlogCategory(models.Model):
	name = models.CharField(max_length = 256)

	class Meta:
		verbose_name = 'Blog Kategoriyasi'

	def __str__(self):
		return self.name


class Blog(models.Model):
	category = models.ForeignKey(BlogCategory, on_delete = models.CASCADE, related_name = 'blog')
	author = models.ForeignKey(Person, on_delete = models.CASCADE, related_name = 'blog')
	title = models.TextField()
	description = models.TextField(null = True, blank = True)
	content = RichTextUploadingField(null = True, blank = True)
	image = models.ImageField(upload_to = 'blog', null = True, blank = True)
	date = models.DateTimeField(null = True, blank = True)
	home = models.BooleanField(default = False)

	class Meta:
		verbose_name = 'Blog'

	def __str__(self):
		return f'{self.author} - {self.title}'


class Banner(models.Model):
	title = models.TextField()
	description = models.TextField(null = True, blank = True)
	image = models.ImageField(upload_to = 'banner')
	link = models.CharField(max_length = 256, null = True, blank = True)

	class Meta:
		verbose_name = 'Banner'

	def __str__(self):
		return self.title


class Message(models.Model):
	title = models.CharField(max_length = 512)
	description = models.TextField(null = True, blank = True)
	image = models.ImageField(upload_to = 'message', null = True, blank = True)
	link = models.CharField(max_length = 256, null = True, blank = True)
	active = models.BooleanField(default = False)

	class Meta:
		verbose_name = 'Message'

	def __str__(self):
		return self.title


class Gallery(models.Model):
	title = models.CharField(max_length = 256)
	image = models.ImageField(upload_to = 'gallery', null = True, blank = True)

	class Meta:
		verbose_name = 'Fotogalereya'

	def __str__(self):
		return self.title