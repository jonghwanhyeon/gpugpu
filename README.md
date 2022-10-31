# gpugpu

![Screenshot: docker run --rm --gpus=all --pid=host --env DOCKER_HOST=unix://tmp/docker.sock --volume /var/run/docker.sock:/tmp/docker.sock:ro ghcr.io/jonghwanhyeon/gpugpu](screenshot.png)

Do you want to know which docker containers are currently using GPUs? `gpugpu` shows current statistics of GPUs and memory usage by running containers.


## Usage
To run it:
```bash
$ docker run \
        --rm \
        --tty \
        --gpus=all \
        --pid=host \
        --env DOCKER_HOST=unix://tmp/docker.sock \
        --volume /var/run/docker.sock:/tmp/docker.sock:ro \
        ghcr.io/jonghwanhyeon/gpugpu
```

## Acknowledgments
Reporting formats are inspired by [`gpustat`](https://github.com/wookayin/gpustat)
