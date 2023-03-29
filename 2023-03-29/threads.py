import time

import random

from threading import (
    Thread,
    current_thread,
    Lock,
)

import requests


urls = [
    "https://google.com",
    "https://pypi.org/project/requests/",
    "https://youtube.com",
    "https://lms.beetroot.academy/",
]


def make_request(url: str, lock: Lock):
    with lock:
        print(f"[{current_thread().name}] 1")
        time.sleep(0.5)
        print(f"[{current_thread().name}] 2")
        time.sleep(0.5)
        print(f"[{current_thread().name}] 3")
        time.sleep(0.5)

    print(f"[{current_thread().name}] END OF THE THREAD")

    # print(f"[{current_thread().name}] Request to <{url}>")
    #
    # time.sleep(random.randint(3, 5))
    # # response = requests.get(url)
    #
    # # with open(f"results/{time.time()}.html", "w") as file:
    # #     file.write(response.text)
    #
    # print(f"[{current_thread().name}] Saved for <{url}>")


if __name__ == "__main__":
    threads = []
    lock = Lock()
    lock2 = Lock()

    for url in urls:
        thread = Thread(
            target=make_request,
            args=(url, lock),
            daemon=True,
            # name=url
        )
        thread.start()

        threads.append(thread)

    with lock:
        print(f"[{current_thread().name}] 1")
        time.sleep(0.5)
        print(f"[{current_thread().name}] 2")
        time.sleep(0.5)
        print(f"[{current_thread().name}] 3")
        time.sleep(0.5)

    print(f"[{current_thread().name}] Before join")
    for thread in threads:
        thread.join()
    print(f"[{current_thread().name}] After join")
