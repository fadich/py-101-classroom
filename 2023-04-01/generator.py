import time

from multiprocessing import (
    Queue,
    Event,
)


def generate_number(queue: Queue, stop_event: Event, n=10, delay=1):
    for i in range(n):
        if stop_event.is_set():
            break

        print(f"[G] {i}")
        queue.put(i)
        time.sleep(delay)

    stop_event.set()
