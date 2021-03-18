from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from account.forms import UserRegistrationForm


class OnlyNotAuthenticated(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_authenticated


class UserView(generic.TemplateView):
    template_name = 'account/user.html'


class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = get_user_model()
    template_name = 'account/user_update.html'
    fields = ('first_name', 'last_name', 'phone',)

    def get_object(self, queryset=None):
        return self.request.user


class UserRegistrationView(OnlyNotAuthenticated, generic.CreateView):
    model = get_user_model()
    template_name = 'account/registration.html'
    form_class = UserRegistrationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('user-detail')

