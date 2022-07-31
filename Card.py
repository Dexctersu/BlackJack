from multiprocessing.sharedctypes import Value
from pickletools import markobject
from typing import List
import random


class Card:

    def __init__(self, mark, no) -> None:
        def convert(number: int) -> str:
            if number == 1:
                return "A"
            if number == 11:
                return "J"
            if number == 12:
                return "Q"
            if number == 13:
                return "K"
            return str(number)

        if not(1 <= no <= 13):
            raise ValueError
        self.mark = mark
        self.no = no
        self.card_name = f"{mark}の{convert(no)}"



