from typing import List
from Card import Card
from PlayerBase import PlayerBase


class User(PlayerBase):

    def is_burst(self) -> bool:
        total_score = self.calculate_total_score()
        if 21 < total_score:
            return True
        return False
