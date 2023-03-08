from queue import (
    Queue as BQueue,
    LifoQueue,
)
from random import random
from time import (
    sleep,
)

MODELING_TIME = 8 * 60  # Minutes
TIME_SCALE = 8 * 60 * 60  # Modeling total time ~ 1 sec
# MODELING_TIME = 10
# TIME_SCALE = 20

REQUEST_PROB = 0.7

SERVER_ORDER_PROB = 0.35
SERVER_DONE_PROB = 0.4
SERVER_RENEW_PROB = 0.25

SERVER_SPEED = 1
MANAGER_SPEED = 3


class Queue(BQueue):

    def __init__(self, maxsize=0):
        super().__init__(maxsize=maxsize)

        self._total_max = 0

    @property
    def total_max(self):
        return self._total_max

    def put(self, item, block=True, timeout=None) -> None:
        super().put(item=item, block=block, timeout=timeout)

        if self.qsize() > self._total_max:
            self._total_max = self.qsize()


class Manager:

    def __init__(self, speed: int, queue: Queue, req_history: LifoQueue):
        self._speed = speed
        self._queue = queue
        self._req_history = req_history

        self._item = None
        self._process = 0

    def process(self):
        if self._process == 0:
            if self._queue.empty():
                print("<manager: idling>")
                return None

            self._process = self._speed
            self._item = self._queue.get()

        self._process -= 1
        print(f"MANAGER: {self._process}")
        if self._process:
            return None

        self._req_history.put(self._item)
        del self._item


class Server:

    def __init__(
        self,
        speed: int,
        queue: Queue,
        order_queue: Queue,
        req_history: LifoQueue,
        order_prob: float,
        done_prob: float,
    ):
        self._speed = speed
        self._queue = queue
        self._ord_queue = order_queue
        self._req_history = req_history
        self._order_prob = order_prob
        self._done_prob = done_prob

        self._item = None
        self._process = 0

    def process(self):
        if self._process == 0:
            if self._queue.empty():
                print("<server: idling>")
                return None

            self._process = self._speed
            self._item = self._queue.get()

        self._process -= 1
        if self._process:
            return None

        server_res = random()
        if server_res <= self._order_prob:
            ord_queue.put(self._item)
            print("Server: ORDER")
        elif server_res <= (self._order_prob + self._done_prob):
            request_history.put(self._item)
            print("Server: DONE")
        else:
            req_queue.put(self._item)
            print("Server: RENEW")

        del self._item


class ClientRequest:

    def __init__(self, prob: float, queue: Queue):
        self._prob = prob
        self._queue = queue

    def generate_request(self):
        if random() <= self._prob:
            item = f"REQUEST!"
            print(item)
            self._queue.put(item)
        else:
            print("<no client request>")


req_queue = Queue()
ord_queue = Queue()

request_history = LifoQueue()

client = ClientRequest(
    prob=REQUEST_PROB,
    queue=req_queue
)

server = Server(
    speed=SERVER_SPEED,
    queue=req_queue,
    order_queue=ord_queue,
    req_history=request_history,
    order_prob=SERVER_ORDER_PROB,
    done_prob=SERVER_DONE_PROB
)
manager = Manager(
    speed=MANAGER_SPEED,
    queue=ord_queue,
    req_history=request_history
)

if __name__ == "__main__":
    for i in range(MODELING_TIME):
        print(f"\n[{i + 1:>10}/{MODELING_TIME:<10}]")

        client.generate_request()
        server.process()
        manager.process()

        sleep(60 / TIME_SCALE)

    print()
    print(f"req_queue.max = {req_queue.total_max}")
    print(f"ord_queue.max = {ord_queue.total_max}")

    print(f"Requests processed = {request_history.qsize()}")
    print(f"Requests left = {req_queue.qsize()}")
    print(f"Orders left = {ord_queue.qsize()}")
