from django.contrib import admin

from HeadHunterApp.models import Company, Skills, Vacancy, Resume, Request

# Register your models here.
admin.site.register([Company, Skills, Vacancy, Resume, Request])