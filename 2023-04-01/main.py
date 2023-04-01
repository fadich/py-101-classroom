from multiprocessing import Queue, Process, Event

from generator import generate_number
from worker import read_number as worker

DELAY = 0.25
ITERATION_NUMBER = 10


if __name__ == "__main__":
    queue = Queue()
    stop_event = Event()

    worker_process = Process(
        target=worker,
        kwargs={
            "delay": DELAY / 2,
            "queue": queue,
            "stop_event": stop_event,
        }
    )

    generator_process = Process(
        target=generate_number,
        kwargs={
            "n": ITERATION_NUMBER,
            "delay": DELAY,
            "queue": queue,
            "stop_event": stop_event,
        }
    )

    worker_process.start()
    generator_process.start()

    print("[Press Ctrl+C for exit]")
    try:
        while not stop_event.is_set():
            pass
    except KeyboardInterrupt:
        stop_event.set()

    worker_process.join()
    generator_process.join()
