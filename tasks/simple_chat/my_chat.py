import argparse
from typing import Tuple

DEFAULT_BUFFSIZE = 1024


def update_arguments(parser: argparse.ArgumentParser):
    parser.add_argument("--host", type=str, default="0.0.0.0", help="connecting server host")
    parser.add_argument("--port", type=int, default=9000, help="connecting server port")
    parser.add_argument("--buffsize", type=int, default=DEFAULT_BUFFSIZE, help="Buffer size (bytes to read)")
    parser.add_argument(
        "-d",
        "-v",
        "--debug",
        "--verbose",
        dest="debug",
        action="store_true",
        help="set debug log level"
    )


def format_address(addr: Tuple[str, int]):
    return f"{addr[0]}:{addr[1]}"
