"""sih URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sih_app.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomePageView.as_view()),
    path("user/login/", UserLoginView.as_view()),
    path("user/logout/", LogoutView.as_view()),
    path("user/signup/", UserCreateView.as_view()),
    path("sites/", SitesView.as_view()),
    path("sites/detail/<pk>/", SiteDetailView.as_view()),
    path("tickets/book/<int:id>/", TicketCreateView.as_view()),
    path("tickets/detail/<pk>/", TicketDetailView.as_view()),
    path("tickets/check/<str:ticketStr>/", TicketCheckView),
]
