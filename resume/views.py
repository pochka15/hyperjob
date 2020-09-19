from django.http import HttpResponseForbidden, HttpResponseBadRequest, HttpResponseRedirect
from django.views.generic.base import TemplateView, View

from resume.forms import NewResumeForm
from resume.models import Resume


class ResumeView(TemplateView):
    template_name = "resume.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resume'] = Resume.objects.all()
        return context


class NewResumeView(View):
    template_name = 'new_resume.html'
    success_url = "/home"

    def post(self, request):
        form = NewResumeForm(request.POST)
        if form.is_valid():
            request_user = self.request.user
            form_data = form.cleaned_data
            if request_user.is_authenticated and not request_user.is_staff:
                Resume(description=form_data['description'],
                       author=request_user) \
                    .save()
                return HttpResponseRedirect(self.success_url)
            return HttpResponseForbidden()
        return HttpResponseBadRequest()
