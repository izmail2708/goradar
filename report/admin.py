from django.contrib import admin
from .models import Report

class ReportAdmin(admin.ModelAdmin):
	fields = ['report_author', 'report_type','report_subtype','report_problem', 'report_published_date', 'report_photo', 'report_description']

admin.site.register(Report,ReportAdmin)