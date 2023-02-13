from typing import Optional


class Human:

    def __init__(self, name: str, surname: Optional[str] = None):
        self.name = name
        self.surname = surname

        self.is_pretty = True

    def introduce(self):
        print(f"My name is {self}!")

    def __str__(self):
        surname_format = "" if self.surname is None else f" {self.surname}"

        return f"{self.name}{surname_format}"


if __name__ == "__main__":
    fadi = Human("Fadi", "Ahmad")
    fadi.introduce()

    print(fadi)

    yurii = Human(name="Yurii")
    yurii.introduce()
    yurii.introduce()

    print(yurii)
