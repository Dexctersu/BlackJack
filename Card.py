from multiprocessing.sharedctypes import Value
from pickletools import markobject
from typing import List
import random


class Card:

    def __init__(self, mark: str, no: int, used: bool=False) -> None:
        """_summary_

        Args:
            mark (str): _description_
            no (int): _description_
            used (bool, optional): _description_. Defaults to False. 引いたカードか？ true:引いた false:引いていない
        """
        def convert(number: int) -> str:
            """_summary_
            1,11,12,13を数値から文字列に変換する
            Args:
                number (int): _description_

            Returns:
                str: _description_
            """
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
        self.used =used
        self.card_name = f"{mark}の{convert(no)}"
