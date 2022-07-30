from typing import List
from Card import Card
from PlayerBase import PlayerBase


class User(PlayerBase):

    def draw_card(self, card: object, user_score: List[str]) -> None:
        while True:
            # 引いたカードを出力
            print('カードを引きますかカードを引く場合はYを引かない場合はNを入力してください')
            s = input()
            if(s == "N"):
                break
            if(s != "Y"):
                print("YとN以外が入力されました。強制終了します。")
                break
            drawn_card = card.draw_card()
            user_score.append(drawn_card.split("の")[1])
            print(f'あなたの引いたカードは{drawn_card}です')
            print(f'あなたの現在の得点は{self.calculate_total_score(user_score)}です')
            if(21 < self.calculate_total_score(user_score)):
                print("21を超えました。あなたの負けです!!")
                exit()
