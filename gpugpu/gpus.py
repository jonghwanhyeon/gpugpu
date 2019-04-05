import psutil

from contextlib import contextmanager
from collections import namedtuple
from pynvml import *

class GPU:
    Memory = namedtuple('Memory', ['total', 'used', 'free'])
    Power = namedtuple('Power', ['usage', 'limit'])
    Process = namedtuple('Process', ['pid', 'user', 'name', 'used_memory'])

    def __init__(self, id):
        self.id = id
        self.handle = nvmlDeviceGetHandleByIndex(id)

    @property
    def name(self):
        return nvmlDeviceGetName(self.handle).decode()

    @property
    def memory(self):
        m = nvmlDeviceGetMemoryInfo(self.handle)
        return GPU.Memory(total=m.total, used=m.used, free=m.free)

    @property
    def utilization(self):
        return nvmlDeviceGetUtilizationRates(self.handle).gpu

    @property
    def temperature(self):
        return nvmlDeviceGetTemperature(self.handle, NVML_TEMPERATURE_GPU)

    @property
    def power(self):
        return GPU.Power(
            usage=nvmlDeviceGetPowerUsage(self.handle) / 1000,
            limit=nvmlDeviceGetPowerManagementLimit(self.handle) / 1000)

    @property
    def processes(self):
        for p in nvmlDeviceGetComputeRunningProcesses(self.handle):
            try:
                name = nvmlSystemGetProcessName(p.pid).decode()
            except NVMLError:
                name = None

            yield GPU.Process(
                pid=p.pid,
                user=psutil.Process(p.pid).username(),
                name=name,
                used_memory=p.usedGpuMemory)

@contextmanager
def all_gpus():
    nvmlInit()
    yield [GPU(id) for id in range(nvmlDeviceGetCount())]
    nvmlShutdown()
