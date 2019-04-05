import docker
from itertools import chain

docker_client = docker.DockerClient(base_url='unix://tmp/docker.sock')

def get_pids(container):
    return set(map(int, chain.from_iterable(container.top(ps_args='-o pid')['Processes'])))

def find_container_by_pid(pid):
    for container in docker_client.containers.list():
        if pid in get_pids(container):
            return container
    return None
