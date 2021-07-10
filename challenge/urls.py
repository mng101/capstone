"""challenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="challenge/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("markets/", views.MarketsPageView.as_view(), name="markets"),
    path("dashboard/", views.HoldingListView.as_view(), name="dashboard"),
    path("thanks/", views.ThanksPageView.as_view(), name="thanks"),
    path("contact/<int:pk>", views.AccountUpdateView.as_view(), name="contact"),
    path("watchlist/<int:pk>", views.WatchlistView.as_view(), name="watchlist"),
    path("transaction/", views.TransactionCreateView.as_view(), name="transaction"),
    path("history/", views.TransactionListView.as_view(), name="history"),
    path("updatetitle/<int:pk>", views.updatetitle, name="updatetitle"),
    # path("test/", views.TestPageView.as_view(), name="test"),
]
