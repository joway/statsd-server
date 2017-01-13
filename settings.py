INTERVAL = 10000  # ms
STATSD_HOST = 'localhost'
STATSD_PORT = 8125
try:
    from local_settings import *
except:
    pass
