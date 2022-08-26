from django.contrib import admin
from django.urls import path
from .views import QuotesClass, QuoteUpdate, QuoteDelete, QuoteNew, massUploadView, TokenUpdate, TokenCreate, TokenList, TokenDelete

urlpatterns = [
    path("list", QuotesClass.as_view(), name='QuoteList'),
    path('new', QuoteNew.as_view()),
    path('<pk>/edit', QuoteUpdate.as_view()),
    path('<pk>/delete', QuoteDelete.as_view()),
    path('mass-upload', massUploadView, name='MassView'),
    path('token/new', TokenCreate.as_view(), name='TokenCreate'),
    path('token/<pk>/edit', TokenUpdate.as_view(), name='TokenUpdate'),
    path("token/list", TokenList.as_view(), name='TokenList'),
    path('token/<pk>/delete', TokenDelete.as_view(), name='TokenDelete'),
]
