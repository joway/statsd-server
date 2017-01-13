from time import sleep

from monitor import monitoring_mem, monitoring_swap, monitoring_cpu, monitoring_net
from settings import INTERVAL
while True:
    monitoring_mem()
    monitoring_swap()
    monitoring_cpu()
    monitoring_net()

    sleep(INTERVAL // 1000)
