from abc import ABCMeta, abstractclassmethod
from typing import List


class PlayerBase:

    def __init__(self, hand: List[str]=[], score: int=0) -> None:
        self.hand = hand
        self.score = score

