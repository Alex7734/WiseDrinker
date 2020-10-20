from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Drink(models.Model):
	category = models.CharField(max_length=1000)
	percentage = models.CharField(max_length=100)
	bio = RichTextUploadingField(null=True, blank=True)
	severity = models.PositiveIntegerField()
	image = models.ImageField(null=True, blank=False)

	def __str__(self):
		return self.category

	class Meta:
		ordering = ['severity']

class SeverityLevel(models.Model):
	severity = models.PositiveIntegerField()
	bac = models.FloatField()
	bio = RichTextUploadingField(null=True, blank=True)
	name = models.CharField(max_length = 1000)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['severity']
