from random import choice
from enum import Enum
from dataclasses import dataclass
from typing import Dict, List


RERUNS = 100000


class Color(Enum):
    red = 'red'
    blue = 'blue'


class Hand(Enum):
    left = 'left'
    right = 'right'


CONFIG = {
    Hand.left: {
        Color.red: 3,
        Color.blue: 7
    },
    Hand.right: {
        Color.red: 8,
        Color.blue: 5
    }
}


@dataclass
class Pill:
    def __init__(self, color: Color, hand: Hand):
        self.color = color
        self.hand = hand


def refillArray(config: Dict[Hand, Dict[Color, int]] = CONFIG) -> List[Pill]:
    return [Pill(color, hand) for hand, item in config.items() for color, num in item.items() for _ in range(num)]


def main() -> None:
    left: int = 0
    right: int = 0

    while left + right < RERUNS:
        pills_in_hands: List[Pill] = refillArray()

        while True:
            pill = choice(pills_in_hands)
            if pill.color == Color.red:
                break

        if pill.hand == Hand.right:
            right += 1
        else:
            left += 1

    print(
        f'Left: {left}, {100*left/(left+right)}%\nRight: {right}, {100*right/(left+right)}%')


if __name__ == "__main__":
    main()
