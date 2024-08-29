from django.urls import path

from HeadHunterApp import views

urlpatterns = [
    path('', views.Worker.as_view(), name='worker'),
    path('profile_page/', views.Seller.as_view(), name='seller'),
    path('resume_detailed_view/<int:resume_id>/', views.ResumeDetailedView.as_view(), name='resume_detailed_view'),
    path('vacancy_detailed_view/<int:vacancy_id>/', views.VacancyDetailView.as_view(), name='vacancy_detailed_view'),
    path('response/', views.Response.as_view(), name='response'),
    path('create_response/<int:vacancy_id>/', views.CreateResponse.as_view(), name='create_response'),
    path('resumes/', views.ResumesView.as_view(), name='resumes'),
    path('resume_delete/<int:resume_id>/', views.resume_delete, name='resume_delete'),
    path('resume_edit/<int:resume_id>/', views.ResumeEdit.as_view(), name='resume_edit'),
    path('create_resume/', views.CreateResume.as_view(), name='create_resume'),
    path('delete_response/<int:vacancy_id>/', views.response_delete, name='delete_response'),
    path('vacancy/', views.vacancy, name='vacancy'),
    path('vacancy_delete/<int:vacancy_id>/', views.vacancy_delete, name='vacancy_delete'),
    path('vacancy_edit/<int:vacancy_id>/', views.VacancyEdit.as_view(), name='vacancy_edit'),
]
