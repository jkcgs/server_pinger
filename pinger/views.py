from django.shortcuts import render, redirect

from .models import PingEntry


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('admin/')

    results = PingEntry.objects.select_related().distinct('server_id')
    context = {'entries': results}
    return render(request, 'index.html', context)
