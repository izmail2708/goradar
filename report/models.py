from django.db import models
from django.conf import settings
from django.contrib import auth 
from django.utils import timezone

class Report(models.Model):
	class Meta():
		db_table = "report"
	report_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	report_type = models.CharField(max_length=200)
	report_subtype = models.CharField(max_length=200)
	report_problem = models.CharField(max_length=200)
	report_published_date = models.DateTimeField()
	report_photo = models.ImageField(upload_to='problems')
	report_description = models.CharField(max_length=300)
