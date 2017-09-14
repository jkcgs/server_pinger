import subprocess
from django.utils import timezone
from time import sleep
from .models import Server, PingEntry

from background_task import background


@background
def demo_task():
    all_servers = Server.objects.all()

    for server in all_servers:
        try:
            result = subprocess.run(['ping', '-c', '1', server.host], stdout=subprocess.PIPE, timeout=1)
            comline = result.stdout.decode('utf-8').split('\n')[1].split('time=')
            if len(comline) < 2:
                ping = 0
            else:
                ping = float(comline[1].split(' ')[0])
        except subprocess.TimeoutExpired:
            ping = 0

        entry = PingEntry(server=server, latency=ping, datetime=timezone.now())
        entry.save()
        print('[{}] ping server {}, result: {}'.format(str(timezone.now()), server.host, ping))

    sleep(3)
    demo_task()
