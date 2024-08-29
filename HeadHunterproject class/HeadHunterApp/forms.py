from django import forms
from .models import Request, Resume, Vacancy


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('resume',)


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('name', 'surname', 'lastname', 'dream_job', 'skills', 'date_of_birth', 'email', 'phone', 'exp', 'education', 'gender')


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ('title', 'description', 'salary', 'skills', 'company', 'type_of_job')