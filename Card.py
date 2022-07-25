from typing import List


class Card:

    def __init__(self, marks: str, nos: str):
        self.marks = marks
        self.nos = nos

    # カードを格納する
    def create_decks(self) -> List[str]:
        decks = []
        for mark in self.marks:
            for no in self.nos:
                message = f'{mark}の{no}'
                decks.append(message)
        return decks


# nos = [str(i) for i in range(1, 14)]
# nos[0] = "A"
# nos[10] = "J"
# nos[11] = "Q"
# nos[12] = "K"
# c = Card(["ハート", "スペード", "ダイヤ", "クラブ"], nos)

# print(c.marks)
# print(c.nos)
# print(c.create_decks())
