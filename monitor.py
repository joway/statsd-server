import socket

import psutil
import statsd as statsd_lib

from settings import STATSD_HOST, STATSD_PORT

hostname = socket.gethostname()
statsd = statsd_lib.StatsClient(host=STATSD_HOST, port=STATSD_PORT, prefix=hostname)


def monitoring_gauge(key, obj):
    for item in obj.__dict__:
        statsd.gauge('%s.%s' % (key, item), int(obj.__getattribute__(item)))


def monitoring_mem():
    monitoring_gauge('mem', psutil.virtual_memory())


def monitoring_swap():
    monitoring_gauge('swap', psutil.swap_memory())


def monitoring_cpu():
    monitoring_gauge('cpu', psutil.cpu_times())


def monitoring_net():
    monitoring_gauge('net', psutil.net_io_counters())
