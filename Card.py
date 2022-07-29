from typing import List
import random


class Card:

    decks = []

    nos = [i for i in range(1,14)]
    marks = ["ハート", "スペード", "ダイヤ", "クラブ"]
    def __init__(self, nos: List[int] = nos, marks: List[str] = marks) -> None:
        self.marks = marks
        self.nos = nos

    # デッキを作成する
    def create_decks(self) -> List[str]:
        for mark in self.marks:
            for no in self.nos:
                message = f'{mark}の{no}'
                Card.decks.append(message)
        return self.decks

    # デッキからカードを引く
    def draw_card(self) -> str:
        # 乱数を生成
        r = random.randint(0, 51)
        # カードを生成
        decks = self.create_decks()
        # カードを引く
        drawn_card = decks[r]
        # 引いたカードを削除
        Card.decks.remove(drawn_card)
        return drawn_card


# nos = [str(i) for i in range(1, 14)]
# nos[0] = "A"
# nos[10] = "J"
# nos[11] = "Q"
# nos[12] = "K"
# c = Card(["ハート", "スペード", "ダイヤ", "クラブ"], nos)

# print(c.marks)
# print(c.nos)
# print(c.create_decks())
