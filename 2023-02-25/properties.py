
# def fun():
#     a = 0
#     def inner():
#         b = a + 1


class Wizard:
    DEFAULT_POWER = 0
    DEFAULT_CLASS_PROP = []

    def __init__(self, power: str = DEFAULT_POWER, cls_prop: list = None):
        self.power = power

        if cls_prop is None:
            cls_prop = self.DEFAULT_CLASS_PROP

        self._spells = cls_prop

    @property
    def spells(self):
        return self._spells

    @spells.setter
    def spells(self, value):
        spell = value
        if isinstance(spell, list):
            spell = value[0]

        if not isinstance(spell, str):
            raise TypeError()

        self._spells = [value]

    def cast_spell(self, spell_name: str):
        if spell_name not in self._spells:
            raise RuntimeError()

        self.log_cast_spell(spell_name)

    # @staticmethod
    @classmethod
    def log_cast_spell(cls, spell_name: str):
        print(f"Magic! {spell_name} has been cast, {cls.calculate_mana_points(spell_name)} mana spent")

    @classmethod
    def calculate_mana_points(cls, spell_name: str):
        return len(spell_name)


class Necromancer(Wizard):
    MANA_FACTOR = 2

    @classmethod
    def calculate_mana_points(cls, spell_name: str):
        return len(spell_name) * cls.MANA_FACTOR


if __name__ == "__main__":
    gendalf = Wizard()
    saruman = Wizard()

    spell = "Fireball!"
    if spell in gendalf.spells:
        gendalf.cast_spell(spell)
    else:
        gendalf.spells = spell
        gendalf.cast_spell(spell)

    # print(gendalf.__dict__)
    # print(Wizard.__dict__)
    #
    # print(gendalf.DEFAULT_CLASS_PROP)
    # print(saruman.DEFAULT_CLASS_PROP)
    # print(gendalf.__dict__)
    # print(saruman.__dict__)
    #
    # saruman.abc = 0
    # saruman.DEFAULT_CLASS_PROP.append(0)
    # saruman.DEFAULT_CLASS_PROP.append(89)
    # print(gendalf.__dict__)
    # print(saruman.__dict__)
    # print(Wizard.__dict__)
    #
    # print(gendalf.DEFAULT_CLASS_PROP)
    # print(saruman.DEFAULT_CLASS_PROP)
    # print(Wizard.DEFAULT_CLASS_PROP)
    #
    # saruman.cast_spell()  # saruman.cast_spell = lambda: 0
    # saruman.cast_spell = 0
    # print(saruman.__dict__)
    # saruman.cast_spell()
