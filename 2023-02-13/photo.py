from datetime import datetime
from pprint import pprint

from human import Human


class Photo:

    def __init__(
        self,
        height: int,
        width: int,
        color_style: str,
        author: Human,
        format_: str = "JPEG"
    ):
        self.height = height
        self.width = width
        self.color_style = color_style
        self.author = author
        self.format = format_

        self.is_converted = False
        self.date = datetime.now()

    def get_size(self):
        return self.height, self.width

    def get_details(self):
        return {
            "size": self.get_size(),
            "color_style": self.color_style,
            "author_name": str(author),
            "format": self.format,
            "is_converted": self.is_converted,
            "date": self.date.isoformat(),
        }

    def convert(self):
        if self.is_converted:
            raise RuntimeError("Already converted")

        self.is_converted = True


if __name__ == "__main__":
    author = Human(
        name=input("Name: "),
        surname=input("Surname: "),
    )

    photo = Photo(
        height=1920,
        width=1080,
        color_style="uncolored",
        author=author,
        format_="gif".upper(),
    )

    pprint(photo.get_details())

    photo.convert()

    pprint(photo.get_details())

    photo.convert()
