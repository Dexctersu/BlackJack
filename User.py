from typing import List
from Card import Card


class User:
    def __init__(self, hand: List[object] = None):
        if hand is None:
            hand = list()
        self.hand = hand

    def calculate_total_score(self):
        total_score = 0
        for i in self.hand:
            total_score += i.no
        return total_score
