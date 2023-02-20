__all__ = [
    "Device",
]


# Modifier  |  Visible in Python  |     Usage     |
# ------------------------------------------------|
# public    |     everywhere      |  everywhere   |
# protected |     everywhere      |  subclasses   |
# private   |   nowhere, but...   |    nowhere    |

class Device:

    def __init__(self):
        # self.is_tuned_on = False  # public
        self._is_tuned_on = False  # protected
        # self.__is_tuned_on = False  # private

    def toggle_turn(self):
        self._is_tuned_on = not self._is_tuned_on

    def is_turned(self) -> bool:
        return self._is_tuned_on


class Hoover(Device):

    def toggle_turn(self):
        if not check_user_subscription() and not self.is_turned():
            raise PermissionError()

        super().toggle_turn()


if __name__ == "__main__":
    device = Device()

    print(device.is_tuned_on)  # It's ok
    print(device._is_tuned_on)  # Don't do this!
    print(device.__is_tuned_on)  # Does not work!!!
