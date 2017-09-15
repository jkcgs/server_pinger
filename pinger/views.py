from compat import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.serializers import serialize

from .models import PingEntry, Server


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('admin/')

    # results = PingEntry.objects.select_related().distinct('server_id')
    # context = {'entries': results}
    with open('pinger/templates/index.html') as f:
        return HttpResponse(f.read())


def servers(request):
    if not request.user.is_authenticated:
        return HttpResponse('{}', mimetype='application/json', status=403)

    results = PingEntry.objects.select_related().distinct('server_id')
    servers = [x.server for x in results]
    results_json = serialize('json', results)
    servers_json = serialize('json', servers)
    json_cont = '{' + '"results":{results}, "servers":{servers}'.format(results=results_json, servers=servers_json) + '}'
    return HttpResponse(json_cont, content_type='application/json')

