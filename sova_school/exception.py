from django.shortcuts import render
from django.http import HttpResponseServerError, HttpResponseNotFound
from django.template import loader


# def page_not_found(request, template_name='../templates/errors/404_not_found.html'):
#     t = loader.get_template(template_name)
#     context = {
#         'your_var': True,
#         'request': request,
#     }
#     return HttpResponseNotFound(t.render(context))
#
#
# def server_error(request, template_name='../templates/errors/500_server_error.html'):
#     t = loader.get_template(template_name)
#     context = {
#         'your_var': True,
#         'request': request,
#     }
#
#     return HttpResponseServerError(t.render(context))

# def handler404(request, *args, **kwargs):
#     response = render(request, '../templates/errors/404_not_found.html')
#     response.status_code = 404
#     return response
#
#
# def handler500(request, *args, **kwargs):
#     response = render(request, '../templates/errors/500_server_error.html')
#     response.status_code = 500
#     return response
