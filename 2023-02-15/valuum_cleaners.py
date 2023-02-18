
class CleaningItem:

    def __init__(self):
        print(f"{self.__class__.__name__} | This is a cleaning item")

        self.cleaning_type = "dry"


class Device:

    def __init__(self):
        print(f"{self.__class__.__name__} | This is an electronic device")

        self.is_tuned_on = False

    def toggle_turn(self):
        self.is_tuned_on = not self.is_tuned_on

    def is_turned(self) -> bool:
        return self.is_tuned_on

    # if device.is_turned():
    #     print("DEVICE IS TURNED ON")


class Robot(Device):
    """
    Робот не може нашкодити людині або через свою бездіяльність допустити,
    щоб людині було завдано шкоди. Робот мусить підкорятися наказам людини,
    коли ці накази не суперечать Першому закону.
    Робот повинен дбати про свою безпеку доти, поки це не суперечить Першому і Другому законам.
    """

    def scan(self):
        if self.is_tuned_on:
            print("I'm scanning")
        else:
            # raise
            print("Turn me on first")


class VacuumCleaner(Device, CleaningItem):

    def __init__(self):
        Device.__init__(self)
        CleaningItem.__init__(self)

        self.cleaning_type = "electronic-dry"

    def clean(self):
        if self.is_tuned_on:
            print(f"I'm cleaning {self.cleaning_type}")
        else:
            print("Turn me on first")


class RobotCleaner(Robot, VacuumCleaner):

    def clean(self):
        if not self.is_turned():
            raise RuntimeError("Turn me on first")
            # print("Turn me on first")

        Robot.scan(self)
        VacuumCleaner.clean(self)

# def vacuum_cleaner_clean():
#     ...
#
#
# def robot_scan():
#     ...
#
#
# def robot_cleaner_clean():
#     robot_scan()
#     vacuum_cleaner_clean()


class RobotWetCleaner(RobotCleaner):

    def __init__(self):
        super().__init__()
        self.cleaning_type = "wet"


if __name__ == "__main__":
    robot = Robot()
    hoover = VacuumCleaner()

    robo_hoover = RobotCleaner()
    robo_hoover.toggle_turn()
    robo_hoover.clean()
    robo_hoover.toggle_turn()

    wet_robo_hoover = RobotWetCleaner()
    if not wet_robo_hoover.is_turned():
        wet_robo_hoover.toggle_turn()

    wet_robo_hoover.clean()
    wet_robo_hoover.toggle_turn()

    print(wet_robo_hoover)

    # stub = Robot()
    # stub = VacuumCleaner()
    # stub = RobotWetCleaner()

    # stub.toggle_turn()
