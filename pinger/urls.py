from django.conf.urls import url
from django.db import ProgrammingError

from . import views
from .tasks import demo_task

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

try:
    demo_task()
except ProgrammingError:
    pass
