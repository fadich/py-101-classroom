import time

from multiprocessing.pool import ThreadPool


urls = [
    "goo",
    "lms",
    "pipy",
]


def make_rq(url: str):
    time.sleep(3)
    return f"{url} + {url}"


if __name__ == "__main__":
    with ThreadPool() as pool:
        results = pool.map(make_rq, urls)

    print(results)
