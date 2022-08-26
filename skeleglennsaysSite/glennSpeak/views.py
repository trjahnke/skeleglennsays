from django.shortcuts import render, HttpResponse
from .models import Quotes, TokenHoken
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.http import HttpResponseRedirect
from .forms import MassUploadForm
from django.contrib.auth.mixins import LoginRequiredMixin


class TokenCreate(CreateView):
    model = TokenHoken
    fields = ['consumerKey', 'consumerSecret', 'accessToken', 'accessSecret']
    success_url = '/glennSpeak/list'


class TokenUpdate(UpdateView):
    model = TokenHoken
    fields = ['consumerKey', 'consumerSecret', 'accessToken', 'accessSecret']
    success_url = '/glennSpeak/list'


class TokenList(LoginRequiredMixin, ListView):
    model = TokenHoken
    raise_exception = True  # Raise exception when no access instead of redirect
    permission_denied_message = "You are not allowed here."


class TokenDelete(DeleteView):
    model = TokenHoken
    success_url = '/glennSpeak/list'


class QuoteNew(CreateView):
    model = Quotes
    fields = ['quote']
    success_url = '/glennSpeak/list'


class QuotesClass(LoginRequiredMixin, ListView):
    model = Quotes
    raise_exception = True  # Raise exception when no access instead of redirect
    permission_denied_message = "You are not allowed here."


class QuoteUpdate(UpdateView):
    model = Quotes

    fields = [
        'quote',
        'tweet_link'
    ]

    success_url = '/glennSpeak/list'


class QuoteDelete(DeleteView):
    model = Quotes
    success_url = '/glennSpeak/list'


def massUploadView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MassUploadForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            textarea_data = form.cleaned_data['all_quotes']
            data_line_list = textarea_data.splitlines()

            for line in data_line_list:
                each_line = line.split('\n')
                obj = Quotes()
                obj.quote = ''.join(each_line)
                obj.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/glennSpeak/list')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MassUploadForm()

    return render(request, 'massUpload.html', {'form': form})
