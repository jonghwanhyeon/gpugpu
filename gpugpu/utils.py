import os
from itertools import chain
from typing import Optional, Set

import docker
import psutil
from docker.models.containers import Container

docker_host = os.environ.get("DOCKER_HOST", "unix://var/run/docker.sock")
docker_client = docker.DockerClient(base_url=docker_host)


def get_pids(container: Container) -> Set[int]:
    return set(
        map(int, chain.from_iterable(container.top(ps_args="-o pid")["Processes"]))
    )


def find_container_by_pid(pid: int) -> Optional[Container]:
    for container in docker_client.containers.list():
        if pid in get_pids(container):
            return container
    return None


def find_user_by_pid(pid: int) -> Optional[str]:
    try:
        return psutil.Process(pid).username()
    except psutil.NoSuchProcess:
        return None
