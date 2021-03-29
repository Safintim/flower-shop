from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from account.forms import UserRegistrationForm, UserLoginForm


class OnlyNotAuthenticated(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect('user-detail')


class UserView(generic.TemplateView):
    template_name = 'account/user_detail.html'


class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = get_user_model()
    template_name = 'account/user_update.html'
    fields = ('first_name', 'last_name', 'phone',)

    def get_object(self, queryset=None):
        return self.request.user


class UserRegistrationView(OnlyNotAuthenticated, generic.CreateView):
    model = get_user_model()
    template_name = 'account/user_registration.html'
    form_class = UserRegistrationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('user-detail')


class Login(OnlyNotAuthenticated, generic.FormView):
    form_class = UserLoginForm
    template_name = 'account/user_login.html'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return redirect('user-detail')


class Logout(generic.View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('user-login')
