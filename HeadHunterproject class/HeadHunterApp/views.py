from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from .models import Company, Vacancy, Skills, Resume, Request
from .forms import RequestForm, ResumeForm, VacancyForm
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView


# Create your views here.
@method_decorator(login_required(login_url='signIn'), name='dispatch')
class Worker(ListView):
    model = Vacancy
    template_name = 'HeadHunterApp/worker.html'
    context_object_name = 'vacancies_list'

    def get_queryset(self):
        user = self.request.user
        responses = Request.objects.filter(resume__user=user)
        return Vacancy.objects.exclude(id__in=[res.vacancy.id for res in responses])

# def worker(request):
#     responses = Request.objects.filter(resume__user=request.user)
#     ctx = {
#         'vacancies_list': Vacancy.objects.exclude(id__in=[res.vacancy.id for res in responses]),
#     }
#     return render(request, 'HeadHunterApp/Worker.html', ctx)


@method_decorator(login_required(login_url='signIn'), name='dispatch')
class ResumesView(ListView):
    model = Resume
    template_name = 'HeadHunterApp/resumes.html'
    context_object_name = 'resumes_list'

    def get_queryset(self):
        return Resume.objects.filter(user=self.request.user)

# def resumes_view(request):
#     resumes = Resume.objects.filter(user=request.user)
#     ctx = {
#         'resumes_list': resumes,
#     }
#     return render(request, 'HeadHunterApp/resumes.html', ctx)


@method_decorator(login_required(login_url='signIn'), name='dispatch')
class CreateResume(CreateView):
    model = Resume
    template_name = 'HeadHunterApp/create_resumes.html'
    form_class = ResumeForm
    context_object_name = 'form'
    success_url = reverse_lazy('resumes')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['vacancy_form'] = VacancyForm
        return ctx

# @login_required(login_url='signIn')
# def create_resume(request):
#     if request.method == 'POST':
#         form = ResumeForm(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.user = request.user
#             form.save()
#             return redirect('resumes')
#     else:
#         form = ResumeForm
#     if request.method == 'POST':
#         form = VacancyForm(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.company = Company.objects.get(user=request.user)
#             form.save()
#             return redirect('vacancy')
#     else:
#         vacancy_form = VacancyForm
#     ctx = {
#         'form': form,
#         'vacancy_form': vacancy_form
#     }
#     return render(request, 'HeadHunterApp/create_resumes.html', ctx)


@method_decorator(login_required(login_url='signIn'), name='dispatch')
class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = 'HeadHunterApp/Vacancy_Detailed_View.html'
    context_object_name = 'vacancy'
    pk_url_kwarg = 'vacancy_id'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        resumes = Resume.objects.filter(user=self.request.user)
        ctx['responses'] = Request.objects.filter(resume__in=resumes)
        ctx['responded_vacancy_ids'] = ctx['responses'].values_list('vacancy_id', flat=True)
        return ctx

# @login_required(login_url='signIn')
# def vacancy_detailed_view(request, vacancy_id):
#     resumes = Resume.objects.filter(user=request.user)
#     responses = Request.objects.filter(resume__in=resumes)
#     responded_vacancy_ids = responses.values_list('vacancy_id', flat=True)
#     ctx = {
#         'vacancy': Vacancy.objects.get(id=vacancy_id),
#         'responses': responses,
#         'responded_vacancy_ids': responded_vacancy_ids
#     }
#     return render(request, 'HeadHunterApp/Vacancy_Detailed_View.html', ctx)


@method_decorator(login_required(login_url='signIn'), name='dispatch')
class Seller(ListView):
    model = Resume
    template_name = 'HeadHunterApp/Seller.html'
    context_object_name = 'resumes_list'

# @login_required(login_url='signIn')
# def seller(request):
#
#     ctx = {
#         'resumes_list': Resume.objects.all(),
#     }
#     return render(request, 'HeadHunterApp/Seller.html', ctx)


@method_decorator(login_required(login_url='signIn'), name='dispatch')
class ResumeDetailedView(DetailView):
    model = Resume
    template_name = 'HeadHunterApp/Resume_Detailed_View.html'
    context_object_name = 'resume'
    pk_url_kwarg = 'resume_id'

# @login_required(login_url='signIn')
# def resume_detailed_view(request, resume_id):
#
#     ctx = {
#         'resume': Resume.objects.get(id=resume_id),
#     }
#     return render(request, 'HeadHunterApp/Resume_Detailed_View.html', ctx)


def resume_delete(request, resume_id):
    Resume.objects.get(id=resume_id).delete()
    return redirect('resumes')


@method_decorator(login_required(login_url='signIn'), name='dispatch')
class ResumeEdit(UpdateView):
    model = Resume
    template_name = 'HeadHunterApp/edit_resume.html'
    form_class = ResumeForm
    context_object_name = 'form'
    pk_url_kwarg = 'resume_id'
    success_url = reverse_lazy('resumes')

# def resume_edit(request, resume_id):
#     resumes = Resume.objects.get(id=resume_id)
#     if request.method == 'POST':
#         form = ResumeForm(request.POST, instance=resumes)
#         if form.is_valid():
#             form.save()
#             return redirect('resumes')
#     else:
#         form = ResumeForm(instance=resumes)
#     ctx = {
#         'form': form
#     }
#     return render(request, 'HeadHunterApp/edit_resume.html', ctx)


@method_decorator(login_required(login_url='signIn'), name='dispatch')
class Response(ListView):
    model = Request
    template_name = 'HeadHunterApp/response.html'
    context_object_name = 'responses'

    def get_queryset(self):
        resumes = Resume.objects.filter(user=self.request.user)
        return Request.objects.filter(resume__in=resumes)

# @login_required(login_url='signIn')
# def response(request):
#     resumes = Resume.objects.filter(user=request.user)
#     responses = Request.objects.filter(resume__in=resumes)
#     ctx = {
#         'responses': responses,
#     }
#     return render(request, 'HeadHunterApp/response.html', ctx)


@method_decorator(login_required(login_url='signIn'), name='dispatch')
class CreateResponse(CreateView):
    model = Request
    template_name = 'HeadHunterApp/create_response.html'
    form_class = RequestForm
    context_object_name = 'form'
    success_url = reverse_lazy('worker')
    pk_url_kwarg = 'vacancy_id'

    def form_valid(self, form):
        form.instance.vacancy = Vacancy.objects.get(id=self.kwargs['vacancy_id'])
        return super().form_valid(form)

# def create_response(request, vacancy_id):
#     if request.method == 'POST':
#         form = RequestForm(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.vacancy = Vacancy.objects.get(id=vacancy_id)
#             form.save()
#             return redirect('worker')
#     form = RequestForm()
#     return render(request, 'HeadHunterApp/create_response.html', {'form': form})


@login_required(login_url='signIn')
def response_delete(request, vacancy_id):
    get_object_or_404(Request, vacancy_id=vacancy_id, resume__user=request.user).delete()
    return redirect('response')


# @method_decorator(login_required(login_url='signIn'), name='dispatch')
# class Vacancy(ListView):
#     model = Vacancy
#     template_name = 'HeadHunterApp/vacancies.html'
#     context_object_name = 'vacancies_list'
#
#     def get_queryset(self):
#         return Vacancy.objects.filter(company__user=self.request.user)

@login_required(login_url='signIn')
def vacancy(request):
    ctx = {
        'vacancies_list': Vacancy.objects.filter(company__user=request.user),
    }
    return render(request, 'HeadHunterApp/vacancies.html', ctx)


def vacancy_delete(request, vacancy_id):
    Vacancy.objects.get(id=vacancy_id).delete()
    return redirect('vacancy')


@method_decorator(login_required(login_url='signIn'), name='dispatch')
class VacancyEdit(UpdateView):
    model = Vacancy
    template_name = 'HeadHunterApp/edit_vacancies.html'
    form_class = VacancyForm
    context_object_name = 'form'
    pk_url_kwarg = 'vacancy_id'
    success_url = reverse_lazy('vacancy')


# def vacancy_edit(request, vacancy_id):
#     vacancies = Vacancy.objects.get(id=vacancy_id)
#     if request.method == 'POST':
#         form = VacancyForm(request.POST, instance=vacancies)
#         if form.is_valid():
#             form.save()
#             return redirect('vacancy')
#     else:
#         form = VacancyForm(instance=vacancies)
#     ctx = {
#         'form': form
#     }
#     return render(request, 'HeadHunterApp/edit_vacancies.html', ctx)
