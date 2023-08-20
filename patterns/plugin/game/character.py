from typing import Protocol


class GameCharacter(Protocol):
    """Basic representation of a game character."""

    def make_a_noise(self) -> None:
        """Let a character make a noise."""
