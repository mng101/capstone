from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.template import Library

from django.views.generic.base import TemplateView
from django.contrib import messages
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                  CreateView, DeleteView, UpdateView, )
import requests
import json
import numpy

from . import forms

# from .models import Account

# Create your views here.

# Define the interval during which repeated API calls for market data are to be avoided
#
MARKET_DATA_REFRESH_INTERVAL = 3600
register = Library()


class HomePageView(TemplateView):
    template_name = "challenge/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        messages.info(self.request, "hello http://example.com")
        return context


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("home")
    template_name = "challenge/signup.html"


class TestPageView(TemplateView):
    template_name = 'challenge/test.html'


class ThanksPageView(TemplateView):
    template_name = 'challenge/thanks.html'


def get_market_summary(request):
    #
    # Get Market Indices for Canada
    #
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-summary"

    querystring = {"region": "CA"}

    headers = {
        'x-rapidapi-key': "438c096415mshb0589791ceeff23p107e84jsnd9ed933221e3",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    if response.status_code == 200:
        # Deserialize the response to a python object
        json_data = json.loads(response.text)
        return json_data
    else:
        return None


# def split_into_columns(indices, n):
#     # Split the list into n columns to display as a table
#     # Adapted from //djangosnippets.org/snippets/401
#     try:
#         items = list(indices)
#         columns = int(n)
#     except (ValueError, TypeError):
#         return [indices]
#
#     list_len = len(items)
#     rows = list_len // columns
#
#     if list_len % n != 0:
#         rows += 1
#
#     return [items[split * i:split * (i + 1):split * (i + 2)] for i in range(n)]


def refresh_market_summary(request):
    #
    # The Market Summary is saved in the User session to avoid repeated API calls.
    # The Summary is refreshed at intervals defined by the value of MARKET_DATA_REFRESH_INTERVAL
    #
    # The timestamp for the last API call is also saved in the User session, and is used to determine
    # when the Market data is to be refreshed
    #

    # If this is a new User sesssion, create entry for "indices" and initialize the timestamp
    if "indices" not in request.session:
        request.session["indices"] = []
        request.session["indices"].append({"timestamp": 0})

    now = timezone.now().timestamp()

    # If we are past the refresh interval, refresh the data and update the timestamp
    if (now - request.session["indices"][0]["timestamp"]) > MARKET_DATA_REFRESH_INTERVAL:
        request.session['indices'].append(get_market_summary(request)['marketSummaryAndSparkResponse'])
        request.session["indices"][0]["timestamp"] = now

    return numpy.array_split(request.session['indices'][1]["result"], 5)


class MarketsPageView(TemplateView):
    template_name = 'challenge/markets.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add list of market indices and values
        context["index_list"] = refresh_market_summary(self.request)

        return context

# TODO - Compete the AccountUpdateView
#
# class AccountUpdateView(UpdateView):
#     model = Account