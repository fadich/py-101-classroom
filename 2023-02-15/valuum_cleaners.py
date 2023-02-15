
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


class Robot(Device):

    def scan(self):
        """
        Робот не може нашкодити людині або через свою бездіяльність допустити,
        щоб людині було завдано шкоди. Робот мусить підкорятися наказам людини,
        коли ці накази не суперечать Першому закону.
        Робот повинен дбати про свою безпеку доти, поки це не суперечить Першому і Другому законам.
        """

        if self.is_tuned_on:
            print("I'm scanning")
        else:
            print("Turn me on first")


class VacuumCleaner(Device, CleaningItem):

    def __init__(self):
        Device.__init__(self)
        CleaningItem.__init__(self)

        self.cleaning_type = "electronic-dry"

    def clean(self):
        if self.is_tuned_on:
            print("I'm cleaning")
        else:
            print("Turn me on first")


# TODO: Start from here

class RobotCleaner(Robot, VacuumCleaner):

    # def __init__(self):
    #     super().__init__()

    def clean(self):
        super().scan()
        super().clean()


class RobotWetCleaner(RobotCleaner):
    pass


if __name__ == "__main__":
    robot = Robot()
    hoover = VacuumCleaner()
    # robo_hoover = RobotCleaner()
    # wet_robo_hoover = RobotWetCleaner()

    # stub = Robot()
    stub = VacuumCleaner()
    # stub = RobotWetCleaner()

    stub.toggle_turn()
