from abc import ABCMeta, abstractclassmethod
from typing import List


class PlayerBase:

    def __init__(self, hand: List[str] = [], score: int = 0) -> None:
        self.hand = hand
        self.score = score

    def calculate_total_score(self, drawn_card: List[str]):
        # ユーザーが引いたカードの合計点
        total_score = 0
        # ユーザーが引いたカードの枚数
        n = len(drawn_card)
        for i in range(n):
            total_score += int(drawn_card[i])
        return total_score
