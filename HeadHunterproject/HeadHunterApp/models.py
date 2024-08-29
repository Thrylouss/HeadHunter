from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    name = models.CharField(
        max_length=100
    )
    description = models.TextField()
    address = models.CharField(
        max_length=100
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class Skills(models.Model):
    name = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    title = models.CharField(
        max_length=100
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='vacancies'
    )
    salary = models.IntegerField()
    skills = models.ManyToManyField(
        Skills,
        related_name='vacancy_skills'
    )
    description = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    job_types = [
        ('FULL_TIME', 'full time'),
        ('PART_TIME', 'part time'),
        ('FREELANCE', 'freelance')
    ]
    type_of_job = models.CharField(
        max_length=100,
        choices=job_types
    )

    def __str__(self):
        return self.title


class Resume(models.Model):
    dream_job = models.CharField(
        max_length=100
    )
    name = models.CharField(
        max_length=100
    )
    surname = models.CharField(
        max_length=100
    )
    lastname = models.CharField(
        max_length=100
    )
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=16)
    skills = models.ManyToManyField(
        Skills,
        related_name='resume_skills'
    )
    exp = models.CharField(
        max_length=100
    )
    education_type = [
        ('ELEMENTARY', 'Elementary school'),
        ('MIDDLE_SCHOOL', 'Middle school'),
        ('HIGHER_EDUCATION', 'Higher education'),
        ('UNIVERSITY', 'University'),
        ('OTHER', 'Other')
    ]
    education = models.CharField(
        max_length=100,
        choices=education_type
    )
    gender_type = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other')
    ]
    gender = models.CharField(
        max_length=100,
        choices=gender_type
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='resume'
    )

    def __str__(self):
        return self.dream_job


class Request(models.Model):
    vacancy = models.ForeignKey(
        Vacancy,
        on_delete=models.CASCADE,
        related_name='response'
    )
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name='response'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    status_type = [
        ('NEW', 'New'),
        ('IN_PROGRESS', 'In progress'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected')
    ]
    status = models.CharField(
        max_length=100,
        choices=status_type,
        default='NEW'
    )

    