from abc import ABCMeta, abstractclassmethod
from typing import List


class PlayerBase:

    def __init__(self, hand: List[object] = None):
        if hand is None:
            hand = list()
        self.hand = hand

    def calculate_total_score(self) -> int:
        """_summary_
        引いたカードの合計点を計算する

        Returns:
            _type_: _description_
        """
        total_score = 0
        for i in self.hand:
            total_score += i.no
        return total_score

    def is_burst(self) -> bool:
        """_summary_
            引いたカードの合計が21を超えたかを判定する
        Returns:
            bool: _description_ True:21より大きい False:21以下
        """
        total_score = self.calculate_total_score()
        if 21 < total_score:
            return True
        return False
