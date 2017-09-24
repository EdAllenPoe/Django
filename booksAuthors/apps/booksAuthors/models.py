from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Author(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Book(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField(max_length=1000)
    published_date = models.DateTimeField()
    category = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    authors = models.ForeignKey(Author)
