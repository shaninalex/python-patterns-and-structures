import json
from dataclasses import dataclass
from game import factory, loader


@dataclass
class Sorcerer:
    name: str

    def make_a_noise(self) -> None:
        print("sorcerer made a noise")


@dataclass
class Wizard:
    name: str

    def make_a_noise(self) -> None:
        print("wizard made a noise")


@dataclass
class Witcher:
    name: str

    def make_a_noise(self) -> None:
        print("witcher made a noise")


def main() -> None:
    factory.register("sorcerer", Sorcerer)
    factory.register("witcher", Witcher)
    factory.register("wizard", Wizard)

    with open("./level.json") as file:
        data = json.load(file)
        loader.load_plugins(data["plugins"])
        characters = [factory.create(item) for item in data["characters"]]

        for character in characters:
            print(character, end="\t")
            character.make_a_noise()


if __name__ == "__main__":
    main()
