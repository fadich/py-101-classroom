import time

from multiprocessing import (
    Queue,
    Event,
)


def read_number(queue: Queue, stop_event: Event, delay=1):
    while True:
        if stop_event.is_set():  # TODO: Make another event
            break

        time.sleep(delay)
        if queue.empty():
            print("[W] empty...")
            continue

        item = queue.get()
        print(f"[W] {item} -> {item ** 2}")
