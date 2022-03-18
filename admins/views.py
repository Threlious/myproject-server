from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm


@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {
        'title': 'GeekShop - Admin'
    }
    return render(request, 'admins/index.html', context)


class UserAdminListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'


class UserAdminCreateView(CreateView):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegistrationForm
    success_url = reverse_lazy('admin_staff:admin_users')


# Update controller
@user_passes_test(lambda u: u.is_staff)
def admin_users_update(request, pk):
    selected_user = User.objects.get(id=pk)
    if request.method == 'POST':
        form = UserAdminProfileForm(instance=selected_user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    else:
        form = UserAdminProfileForm(instance=selected_user)
    context = {
        'title': 'GeekShop - Admin',
        'form': form,
        'selected_user': selected_user,
    }
    return render(request, 'admins/admin-users-update-delete.html', context)


# Delete controller
@user_passes_test(lambda u: u.is_staff)
def admin_users_delete(request, pk):
    user = User.objects.get(id=pk)
    user.safe_delete()
    return HttpResponseRedirect(reverse('admin_staff:admin_users'))

# # Read controller
# @user_passes_test(lambda u: u.is_staff)
# def admin_users(request):
#     users = User.objects.all()
#     context = {
#         'title': 'GeekShop - Admin',
#         'users': users,
#     }
#     return render(request, 'admins/admin-users-read.html', context)

# # Create controller
# @user_passes_test(lambda u: u.is_staff)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admin_staff:admin_users'))
#     else:
#         form = UserAdminRegistrationForm()
#     context = {
#         'title': 'GeekShop - Admin',
#         'form': form
#     }
#     return render(request, 'admins/admin-users-create.html', context)
