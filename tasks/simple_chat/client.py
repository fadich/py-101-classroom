#!/usr/bin/env python3

import argparse
import socket
import sys
from threading import (
    Thread,
    Event,
)
from typing import (
    Callable,
    Optional,
    Tuple,
)

import my_chat


def receive_msg(client, buffsize, start_event: Event):
    while not start_event.is_set():
        data: bytes = client.recv(buffsize)
        if not data:
            continue

        data: bytes = data.replace(my_chat.format_address(client.getsockname()).encode(), b"ME")

        try:
            data = data.decode()
        except UnicodeDecodeError as e:
            print(e)

        print(f"\r{data}\n>>> ", end="")


def on_connection(
    client: socket.socket,
    addr: Tuple[str, int],
    buffsize: int = my_chat.DEFAULT_BUFFSIZE,
):
    print(f"Connected to {my_chat.format_address(addr)}")

    start_event = Event()

    thread = Thread(target=receive_msg, args=(client, buffsize, start_event), daemon=True)
    thread.start()

    while not start_event.is_set():
        try:
            msg = input(">>> ").strip()
            if msg:
                client.sendall(msg.encode())
        except KeyboardInterrupt:
            break
        except ConnectionError as e:
            print(f"[ERROR] {e}")
            try:
                print("Reconnecting...")
                client = start_client(host=addr[0], port=addr[1], buffsize=buffsize, on_connect=on_connection)
            except Exception as e:
                print(f"[ERROR] Could not reconnect: {e}")
                break

    start_event.set()

    thread.join()


def start_client(
    host: str,
    port: int,
    buffsize: int = my_chat.DEFAULT_BUFFSIZE,
    on_connect: Optional[Callable] = None
):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        addr = (host, port)
        s.connect(addr)
        if on_connect is not None:
            on_connect(s, addr, buffsize)

    return socket


def main():
    parser = argparse.ArgumentParser(description="Simple sockets client")
    my_chat.update_arguments(parser)

    args = parser.parse_args()

    try:
        start_client(
            host=args.host,
            port=args.port,
            buffsize=args.buffsize,
            on_connect=on_connection,
        )
    except KeyboardInterrupt:
        pass

    return 0


if __name__ == "__main__":
    sys.exit(main())
