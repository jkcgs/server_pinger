from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.db import ProgrammingError

from . import views
from .tasks import demo_task

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/servers$', views.servers, name='servers'),
] + static(settings.STATIC_URL)

try:
    demo_task()
except ProgrammingError:
    pass
