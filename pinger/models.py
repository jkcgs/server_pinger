from django.contrib import admin
from django.db import models


class Server(models.Model):
    host = models.CharField(max_length=255, verbose_name='IP or host')
    add_date = models.DateTimeField('date added', auto_now_add=True, blank=True)
    description = models.TextField('Server description', default='No description')

    def __str__(self):
        return 'Server: ' + self.host


class ServerAdmin(admin.ModelAdmin):
    list_display = ['host', 'description', 'add_date']


class PingEntry(models.Model):
    class Meta:
        verbose_name = 'Ping entry'
        verbose_name_plural = 'Ping entries'

    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    latency = models.FloatField('latency in ms')
    datetime = models.DateTimeField('latency time')

    def __str__(self):
        return 'Ping to server ' + str(self.server)


class PingEntryAdmin(admin.ModelAdmin):
    list_display = ['server', 'latency', 'datetime']
