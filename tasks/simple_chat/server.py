#!/usr/bin/env python3

import argparse
import socket
import sys
import time
from threading import Thread
from typing import (
    Callable,
    Optional,
    Dict,
    List,
)

import my_chat


class SocketObject:

    def __init__(
        self,
        host: str,
        port: int,
        buffsize: int,
    ):
        self._host = host
        self._port = port
        self._buffsize = buffsize

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def buffsize(self):
        return self._buffsize

    @property
    def address(self):
        return self._host, self._port

    @property
    def address_formatted(self):
        return my_chat.format_address(self.address)


class Client(SocketObject):

    def __init__(
        self,
        host: str,
        port: int,
        buffsize: int,
        connection: socket.socket,
    ):
        super().__init__(host=host, port=port, buffsize=buffsize)

        self._connection = connection

    @property
    def connection(self) -> socket.socket:
        return self._connection


class SockerServer(SocketObject):

    def __init__(
        self,
        host: str,
        port: int,
        buffsize: int,
        debug: Optional[bool] = False,
        on_start: Optional[Callable] = None,
        on_connection: Optional[Callable] = None,
        on_disconnection: Optional[Callable] = None,
        on_receive: Optional[Callable] = None,
        on_error: Optional[Callable] = None,
    ):
        super().__init__(host=host, port=port, buffsize=buffsize)

        self._debug = debug

        pass_cb = print if self._debug else (lambda *args, **kwargs: None)

        self._on_start = on_start or pass_cb
        self._on_connection = on_connection or pass_cb
        self._on_disconnection = on_disconnection or pass_cb
        self._on_disconnection = on_disconnection or pass_cb
        self._on_receive = on_receive or pass_cb
        self._on_error = on_error or pass_cb

        self._started = False
        self._socket: Optional[socket.socket] = None
        self._clients: Dict[str, Client] = {}

        self._thread: Optional[Thread] = None
        self._connection_threads: Dict[str, Thread] = {}

    @property
    def address(self):
        return self._host, self._port

    @property
    def address_formatted(self):
        return my_chat.format_address(self.address)

    @property
    def is_started(self):
        return self._socket is not None

    def start(self):
        self._started = True

        self._thread = Thread(target=self._start, daemon=True)
        self._thread.start()

    def stop(self):
        self._started = False
        self._thread = None

    def _start(self):
        # socket.setdefaulttimeout(1)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            self._socket = self._bind_socket(s)

            self._socket.listen()

            while self._started:
                client = self._accept_connection()
                if client is None:
                    continue

                th = Thread(target=self._handle_connection, args=(client, ), daemon=True)
                th.start()

                self._connection_threads[client.address_formatted] = th

        self._socket = None

    def _bind_socket(self, server: socket.socket):
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(self.address)

        self._on_start(self)

        return server

    def _accept_connection(self):
        conn, addr = self._socket.accept()

        client = Client(
            connection=conn,
            host=addr[0],
            port=addr[1],
            buffsize=self.buffsize,
        )

        self._clients[client.address_formatted] = client
        self._on_connection(client)

        return client

    def _disconnect_client(self, client: Client):
        if client.address_formatted in self._clients:
            client = self._clients.pop(client.address_formatted)

        if client.address_formatted in self._connection_threads:
            self._connection_threads.pop(client.address_formatted)

        self._on_disconnection(client)

        return client

    def _handle_connection(self, client: Client):
        def target():
            while self._started:
                try:
                    data = client.connection.recv(self.buffsize)
                    if not data:
                        continue

                    for a, c in self._clients.items():
                        c.connection.sendall(b"[" + client.address_formatted.encode() + b"] " + data)

                except ConnectionError:
                    self._disconnect_client(client)
                    break

                except Exception as e:
                    self._on_error(self, e)

        thread = Thread(target=target, daemon=True)
        thread.start()


def writeln(line: str):
    sys.stdout.write(f"{line}\n")
    sys.stdout.flush()


def on_server_started(server: SocketObject):
    writeln(f"Listening on {server.address_formatted}")


def on_client_connected(client: SocketObject):
    writeln(f"New connection {client.address_formatted}")


def on_client_disconnected(client: SocketObject):
    writeln(f"Disconnected {client.address_formatted}")


def on_data_received(client: SocketObject, data: bytes):
    writeln(f"Data received from {client.address_formatted}")
    writeln(f"\t{data}")


def log_error(server: SocketObject, error: Exception):
    sys.stderr.write(f"{error}\n")
    sys.stderr.flush()


def main():
    parser = argparse.ArgumentParser(description="Simple sockets server")
    my_chat.update_arguments(parser)

    args = parser.parse_args()

    server = SockerServer(
        host=args.host,
        port=args.port,
        buffsize=args.buffsize,
        debug=args.debug,

        # Callbacks
        on_start=on_server_started,
        on_connection=on_client_connected,
        on_disconnection=on_client_disconnected,
        on_receive=on_data_received,
        on_error=log_error
    )

    if args.debug:
        writeln("DEBUG MOD IS ON")

    try:
        server.start()
        writeln("Press [Ctrl+C] for exit...")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        writeln("Press [Ctrl+C] for force stop...")
        server.stop()

    return 0


if __name__ == "__main__":
    sys.exit(main())
