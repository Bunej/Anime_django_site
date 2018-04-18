from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, update_session_auth_hash
from accounts.forms import SignupForm, EditProfileForm, EditProfileFormDetail
from django.contrib.auth.models import User


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')


def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    context = {'user': user}
    return render(request, 'accounts/profile.html', context)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        form_detail = EditProfileFormDetail(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid() and form_detail.is_valid():
            form.save()
            form_detail.save()
            return redirect(reverse('accounts:profile', args=[request.user.username]))

    else:
        form = EditProfileForm(instance=request.user)
        form_detail = EditProfileFormDetail(instance=request.user.userprofile)
        context = {'form': form, 'form_detail': form_detail}
        return render(request, 'accounts/edit_profile.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts:profile', args=[request.user.username]))
        else:
            return redirect('accounts:change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        context = {'form': form}
        return render(request, 'accounts/change_password.html', context)
