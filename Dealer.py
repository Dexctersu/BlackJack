from typing import List
from PlayerBase import PlayerBase


class Dealer(PlayerBase):

    def draw_card(self, card: object, dealer_score: List[str]):
        total_score=self.calculate_total_score(dealer_score)
        while total_score < 17:
            drawn_card = card.draw_card()
            dealer_score.append(drawn_card.split("の")[1])
            print(f'ディーラーの引いたカードは{drawn_card}です')
            total_score = self.calculate_total_score(dealer_score)
        return self.calculate_total_score(dealer_score)
