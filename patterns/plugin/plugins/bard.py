"""Game extention that adds a bard character."""

from dataclasses import dataclass
from game import factory


@dataclass
class Bard:
    name: str
    instrument: str = "flute"

    def make_a_noise(self) -> None:
        print(f"Toss a coin to your witcher!... Plaing with {self.instrument}")


def initialize() -> None:
    factory.register("bard", Bard)
