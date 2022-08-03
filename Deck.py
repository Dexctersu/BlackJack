from operator import truediv
from typing import List
from Card import Card
import random


class Deck:
    def _initialize(self) -> List[int]:
        marks = ["ハート", "スペード", "ダイヤ", "クローバー"]
        self.cards = [Card(marks[i % 4], i % 13+1) for i in range(52)]
        return self.cards

    def draw(self, role: str, hide: bool = False) -> List[str]:
        """_summary_
        カードを引いて、カード名を表示する

        Args:
            role (str): _description_ プレイヤー名
            hide (bool, optional): _description_. Defaults to False. カードの値を表示するか? true:非表示 false:表示

        Returns:
            List[str]: _description_
        """
        card = self._initialize()
        r = random.randint(0, 51)
        drawn_card = card[r]
        while True:
            if(not(drawn_card.used)):
                drawn_card.used = True

                if hide:
                    print(f"{role}の引いたカードは分かりません")
                else:
                    print(f"{role}の引いたカードは{drawn_card.card_name}です")
                return drawn_card
