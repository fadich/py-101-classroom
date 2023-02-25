
class Wizard:
    _instances = {}

    def __init__(self, name):
        self.name = name

        if self.name not in self._instances:
            self._instances[self.name] = 0
        self._instances[self.name] += 1

    def __del__(self):
        self._instances[self.name] -= 1
        if self._instances[self.name] == 0:
            del self._instances[self.name]

    # @classmethod
    # def get_unique_names(cls):
    #     return [k for k, v in cls._instances.items() if v > 0]

    @classmethod
    def get_instances_total(cls):
        return len(cls._instances)


if __name__ == "__main__":
    gendalf = Wizard("Gendalf")
    print(Wizard.get_unique_names())
    print(Wizard.get_instances_total())

    del gendalf
    print(Wizard.get_unique_names())
    print(Wizard.get_instances_total())
