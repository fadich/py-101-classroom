import abc
import sys

from typing import Tuple


class Writer(abc.ABC):

    @abc.abstractmethod
    def write(self, *lines: Tuple[str], end: str = "\n", sep=" "):
        raise NotImplemented()


class ConsoleWriter(Writer):

    def write(self, *lines: Tuple[str], end: str = "\n", sep=" "):
        sys.stdout.write(f"{sep.join(lines)}{end}")


class TextFileWriter(Writer):
    ...


class JsonWriter(Writer):
    ...


if __name__ == "__main__":
    writer_types = {
        "cmd": ConsoleWriter,
        "txt": TextFileWriter,
        "json": JsonWriter,
    }

    writer_type = input(f"Select writer (*{', '.join(writer_types.keys())}): ")
    writer_cls = writer_types.get(writer_type.lower(), writer_types["cmd"])

    writer = writer_cls()

    while True:
        try:
            writer.write(
                input(">>> ")
            )
        except KeyboardInterrupt:
            break
