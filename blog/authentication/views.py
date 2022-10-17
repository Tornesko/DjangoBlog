# from django.contrib.auth.forms import UserChangeForm
# from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from authentication.forms import SignUpForm, EditUserDataForm, ChangePasswordForm, CreateProfileForm
from main.models import Profile


class PasswordUpdateView(PasswordChangeView):
    form_class = ChangePasswordForm
    # form_class = PasswordChangeForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('password_success')

    def get_object(self):
        return self.request.user


def password_success(request):
    return render(request, 'registration/password_succes.html', {})


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserUpdateView(generic.UpdateView):
    form_class = EditUserDataForm
    template_name = 'registration/edit_user_data.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class ProfileView(generic.DetailView):
    template_name = 'registration/profile.html'
    model = Profile

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        # users = Profile.objects.all()
        user_pr = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["user_pr"] = user_pr
        return context


class ProfileEditView(generic.UpdateView):
    model = Profile
    # form_class = EditProfileForm
    fields = ('ava', 'bio', 'facebook_url', 'instagram_url', 'web_site_url', 'twitter',)
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

class CreateProfileView(generic.CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'registration/create_profile.html'
    success_url = reverse_lazy('home')