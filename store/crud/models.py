from __future__ import unicode_literals

from django.db import models


class Branch(models.Model):
	brach_name = models.CharField(max_length=30)


class Brands(models.Model):
	brand_name = models.CharField(max_length=30)

class Products(models.Model):
	product_name = models.CharField(max_length=30)

class Store(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	image = models.CharField(max_length=50)
	rating = models.IntegerField()
	branch = models.ManyToManyField(Branch)
	brands = models.ManyToManyField(Brands)
	product = models.ForeignKey(Products)