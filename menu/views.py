from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView


class MainMenuView(TemplateView):
    template_name = "menu.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['url_tuples'] = (('/login', 'Login'),
                                 ('/signup', 'Signup'),
                                 ('/vacancies', 'Vacancies'),
                                 ('/resume', 'Resume'),
                                 ('/new', 'Add vacancy and resume'))
        return self.render_to_response(context)


class CustomLoginView(LoginView):
    template_name = "login.html"
    form_class = AuthenticationForm


class CustomSignUpView(CreateView):
    template_name = "signup.html"
    success_url = "/login"
    form_class = UserCreationForm
