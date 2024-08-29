from django.urls import path

from HeadHunterApp import views

urlpatterns = [
    path('', views.worker, name='worker'),
    path('profile_page/', views.seller, name='seller'),
    path('resume_detailed_view/<int:resume_id>/', views.resume_detailed_view, name='resume_detailed_view'),
    path('vacancy_detailed_view/<int:vacancy_id>/', views.vacancy_detailed_view, name='vacancy_detailed_view'),
    path('response/', views.response, name='response'),
    path('create_response/<int:vacancy_id>/', views.create_response, name='create_response'),
    path('resumes/', views.resumes_view, name='resumes'),
    path('resume_delete/<int:resume_id>/', views.resume_delete, name='resume_delete'),
    path('resume_edit/<int:resume_id>/', views.resume_edit, name='resume_edit'),
    path('create_resume/', views.create_resume, name='create_resume'),
    path('delete_response/<int:vacancy_id>/', views.response_delete, name='delete_response'),
    path('vacancy/', views.vacancy, name='vacancy'),
    path('vacancy_delete/<int:vacancy_id>/', views.vacancy_delete, name='vacancy_delete'),
    path('vacancy_edit/<int:vacancy_id>/', views.vacancy_edit, name='vacancy_edit'),
]