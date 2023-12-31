from django.contrib.auth import login

from django.urls import reverse_lazy

from django.views.generic import CreateView

from e_commerce_website.accounts.forms import RegisterUserForm

from e_commerce_website.common.mixins import NavigationBarMixin


class RegisterUserView(NavigationBarMixin, CreateView):
    template_name = 'account/register.html'
    form_class = RegisterUserForm

    success_url = reverse_lazy('index_page')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['next'] = self.request.GET.get('next', '')

        nav_bar_context = self.get_nav_bar_context()
        context.update(nav_bar_context)

        return context

    def get_success_url(self):
        next_url = self.request.POST.get('next', '')
        return next_url if next_url else self.success_url
