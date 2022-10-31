from gpugpu.gpus import all_gpus
from gpugpu.utils import get_friendly_name_of_process


def colored(name, text):
    from colored import fg, attr

    return fg(name) + str(text) + attr("reset")


def show_status(gpu):
    parts = [
        colored("blue", "[{}]".format(gpu.id)),
        gpu.name,
        "|",
        colored("red", "{} C".format(gpu.temperature)),
        "|",
        colored("green", "{} %".format(gpu.utilization)),
        "|",
        colored("yellow", "{:.0f}".format(gpu.memory.used / 1024 / 1024)),
        "/",
        colored("yellow", "{:.0f}".format(gpu.memory.total / 1024 / 1024)),
        "MB",
    ]

    processes = list(gpu.processes)
    if processes:
        parts += [
            "|",
            *(
                "{}({} MB)".format(
                    get_friendly_name_of_process(p),
                    colored("yellow", int(p.used_memory / 1024 / 1024)),
                )
                for p in processes
            ),
        ]

    print(*parts, sep=" ")


if __name__ == "__main__":
    with all_gpus() as gpus:
        for gpu in gpus:
            show_status(gpu)
