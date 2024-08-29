from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Company, Vacancy, Skills, Resume, Request
from .forms import RequestForm, ResumeForm, VacancyForm


# Create your views here.
@login_required(login_url='signIn')
def worker(request):
    responses = Request.objects.filter(resume__user=request.user)
    ctx = {
        'vacancies_list': Vacancy.objects.exclude(id__in=[res.vacancy.id for res in responses]),
    }
    return render(request, 'HeadHunterApp/Worker.html', ctx)


@login_required(login_url='signIn')
def resumes_view(request):
    resumes = Resume.objects.filter(user=request.user)
    ctx = {
        'resumes_list': resumes,
    }
    return render(request, 'HeadHunterApp/resumes.html', ctx)


@login_required(login_url='signIn')
def create_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('resumes')
    else:
        form = ResumeForm
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.company = Company.objects.get(user=request.user)
            form.save()
            return redirect('vacancy')
    else:
        vacancy_form = VacancyForm
    ctx = {
        'form': form,
        'vacancy_form': vacancy_form
    }
    return render(request, 'HeadHunterApp/create_resumes.html', ctx)


@login_required(login_url='signIn')
def user_resume_detailed_view(request, resume_id):
    ctx = {
        'resume': Resume.objects.get(id=resume_id),
    }
    return render(request, 'HeadHunterApp/Resume_Detailed_View.html', ctx)


@login_required(login_url='signIn')
def vacancy_detailed_view(request, vacancy_id):
    resumes = Resume.objects.filter(user=request.user)
    responses = Request.objects.filter(resume__in=resumes)
    responded_vacancy_ids = responses.values_list('vacancy_id', flat=True)
    ctx = {
        'vacancy': Vacancy.objects.get(id=vacancy_id),
        'responses': responses,
        'responded_vacancy_ids': responded_vacancy_ids
    }
    return render(request, 'HeadHunterApp/Vacancy_Detailed_View.html', ctx)


@login_required(login_url='signIn')
def seller(request):

    ctx = {
        'resumes_list': Resume.objects.all(),
    }
    return render(request, 'HeadHunterApp/Seller.html', ctx)


@login_required(login_url='signIn')
def resume_detailed_view(request, resume_id):

    ctx = {
        'resume': Resume.objects.get(id=resume_id),
    }
    return render(request, 'HeadHunterApp/Resume_Detailed_View.html', ctx)


def resume_delete(request, resume_id):
    Resume.objects.get(id=resume_id).delete()
    return redirect('resumes')


def resume_edit(request, resume_id):
    resumes = Resume.objects.get(id=resume_id)
    if request.method == 'POST':
        form = ResumeForm(request.POST, instance=resumes)
        if form.is_valid():
            form.save()
            return redirect('resumes')
    else:
        form = ResumeForm(instance=resumes)
    ctx = {
        'form': form
    }
    return render(request, 'HeadHunterApp/edit_resume.html', ctx)


@login_required(login_url='signIn')
def response(request):
    resumes = Resume.objects.filter(user=request.user)
    responses = Request.objects.filter(resume__in=resumes)
    ctx = {
        'responses': responses,
    }
    return render(request, 'HeadHunterApp/response.html', ctx)


def create_response(request, vacancy_id):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.vacancy = Vacancy.objects.get(id=vacancy_id)
            form.save()
            return redirect('worker')
    form = RequestForm()
    return render(request, 'HeadHunterApp/create_response.html', {'form': form})


@login_required(login_url='signIn')
def response_delete(request, vacancy_id):
    get_object_or_404(Request, vacancy_id=vacancy_id, resume__user=request.user).delete()
    return redirect('response')


@login_required(login_url='signIn')
def vacancy(request):
    ctx = {
        'vacancies_list': Vacancy.objects.filter(company__user=request.user),
    }
    return render(request, 'HeadHunterApp/vacancies.html', ctx)


def vacancy_delete(request, vacancy_id):
    Vacancy.objects.get(id=vacancy_id).delete()
    return redirect('vacancy')


def vacancy_edit(request, vacancy_id):
    vacancies = Vacancy.objects.get(id=vacancy_id)
    if request.method == 'POST':
        form = VacancyForm(request.POST, instance=vacancies)
        if form.is_valid():
            form.save()
            return redirect('vacancy')
    else:
        form = VacancyForm(instance=vacancies)
    ctx = {
        'form': form
    }
    return render(request, 'HeadHunterApp/edit_vacancies.html', ctx)