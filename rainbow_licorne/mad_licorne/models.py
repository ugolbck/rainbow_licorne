from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    """
    Category model for handling different category across application
    """
    name = models.CharField(max_length=50, verbose_name='Name')
    slug = models.SlugField(verbose_name='Slug')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', ]
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


"""
Test pour ajout d'une section de commentaire
"""
class Comment(models.Model):
	name = models.CharField(max_length=50)
	content = models.TextField()
	comment_date = models.DateTimeField(auto_now_add=True)


class Article(models.Model):
	"""
	Modèles d'articles
	"""
	title = models.CharField(max_length=150)
	slug = models.SlugField()
	containt = models.TextField()
	release_date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	picture = models.ImageField()
	category = models.ManyToManyField(Category)
	comments = models.ManyToManyField(Comment, blank=True)

	def __str__(self):
		return self.title