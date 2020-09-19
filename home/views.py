from django.views.generic.base import TemplateView

from resume.forms import NewResumeForm
from vacancy.forms import NewVacancyForm


class AddVacancyAndResumeView(TemplateView):
    template_name = "add_vacancy_and_resume.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vacancy_form'] = NewVacancyForm()
        context['resume_form'] = NewResumeForm()
        return context

