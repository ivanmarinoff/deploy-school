from django.shortcuts import render
from django.http import HttpResponseServerError, HttpResponseNotFound
from django.template import loader


def bad_request(request, exception):
    context = {}
    return render(request, '../templates/errors/404_not_found.html', context, status=400)


def permission_denied(request, exception):
    context = {}
    return render(request, '../templates/errors/404_not_found.html', context, status=403)


def server_error(request):
    context = {}
    return render(request, '../templates/errors/500_server_error.html', context, status=500)
