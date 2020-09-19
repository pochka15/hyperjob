from django.http import HttpResponseForbidden, HttpResponseRedirect, HttpResponseBadRequest
from django.views.generic.base import TemplateView, View

from vacancy.forms import NewVacancyForm
from vacancy.models import Vacancy


class VacanciesView(TemplateView):
    template_name = "vacancies.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vacancies'] = Vacancy.objects.all()
        return context


class NewVacancyView(View):
    template_name = "new_vacancy.html"
    success_url = "/home"

    def post(self, request):
        form = NewVacancyForm(request.POST)
        if form.is_valid():
            request_user = self.request.user
            form_data = form.cleaned_data
            if request_user.is_authenticated and request_user.is_staff:
                Vacancy(description=form_data['description'],
                        author=request_user) \
                    .save()
                return HttpResponseRedirect(self.success_url)
            return HttpResponseForbidden()
        return HttpResponseBadRequest()
