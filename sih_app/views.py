from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    DeletionMixin,
    UpdateView,
    FormView,
)
from django.views.generic.detail import DetailView
from django.views.generic.base import RedirectView, TemplateView
from django.views.generic.list import ListView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import *
from .forms import *

# Create your views here.
class UserLoginView(LoginView):
    form_class = CustomUserLoginForm
    template_name = "user_login.html"


class UserCreateView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "user_signup.html"
    success_url = "/user/login"


class HomePageView(LoginRequiredMixin, TemplateView):  # you might wanna change this
    template_name = "root.html"


class SitesView(LoginRequiredMixin, ListView):
    template_name = "all_sites.html"
    context_object_name = "sites"

    def get_queryset(self):
        return Site.objects.all()


class SiteDetailView(LoginRequiredMixin, DetailView):
    model = Site
    template_name = "site_details.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["date"] = timezone.now()

        return context

    def get_queryset(self):
        return Site.objects.all()


import os
import string
import random


def ticket_string(length):
    chars = string.ascii_letters + string.digits
    random.seed = os.urandom(1034)
    return "".join(random.choice(chars) for i in range(length))


class TicketCreateView(LoginRequiredMixin, CreateView):
    form_class = TicketCreateForm
    template_name = "ticket_book.html"
    success_url = "/sites/"

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.site = Site.objects.get(id=self.kwargs["id"])
        self.object.ticket_str = ticket_string(10)
        self.object.visit_date = self.request.GET.get("visit_date")
        self.object.count = self.request.GET.get("count")
        self.object.save()
        return HttpResponseRedirect(f"/tickets/detail/{self.object.id}/")


class TicketDetailView(LoginRequiredMixin, DetailView):
    model = Ticket
    template_name = "ticket_details.html"

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)


def TicketCheckView(request, ticketStr, password):
    password_str = "xpK9mg9RMXACkhwz"
    try:
        ticket = Ticket.objects.get(ticket_str=ticketStr, visit_date=timezone.now())
    except:
        ticket = None
    if password != password_str:
        return render(request, "access_denied.html")
    if ticket:
        site = Site.objects.filter(
            id=ticket.site.id,
            open_time__lte=timezone.now(),
            close_time__gt=timezone.now(),
        )
        if site and ticket.attend_status == "YET":
            ticket.attend_status = "YES"
            ticket.save()
            return render(request, "success.html")
        else:
            return render(request, "failed.html")
    else:
        return render(request, "failed.html")
