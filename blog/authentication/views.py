# from django.contrib.auth.forms import UserChangeForm
# from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
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

        user_pr = get_object_or_404(Profile, id=self.kwargs['pk'])
        followed = False
        if user_pr.followers.filter(id=self.request.user.profile.id).exists():
            followed = True
        context["user_pr"] = user_pr
        context["followed"] = followed
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


class FollowersView(generic.ListView):
    # model = Profile
    def get_queryset(self):
        current_pk = self.kwargs['pk']

        current_user = Profile.objects.get(pk=current_pk)
        # print(Profile.objects.filter(followers=current_user))
        return Profile.objects.filter(followers=current_user)
        # return Profile.objects.filter(followers=current_user.followers)

    template_name = 'registration/followers.html'


def SubscribeView(request, pk):
    profile = get_object_or_404(Profile, id=request.POST.get('profile_id'))
    followed = False
    if profile.followers.filter(id=request.user.profile.id).exists():
        profile.followers.remove(request.user.profile)
        followed = False
    else:
        profile.followers.add(request.user.profile)
        followed = True

    return HttpResponseRedirect(reverse('profile', args=[str(pk)]))
