from typing import List
from Card import Card
from PlayerBase import PlayerBase


class User(PlayerBase):

    # ユーザーが引いたカードの合計点を計算する

    def calculate_total_score(self, drawn_card):
        # ユーザーが引いたカードの合計点
        total_score = 0
        # ユーザーが引いたカードの枚数
        n = len(drawn_card)
        for i in range(n):
            total_score += int(drawn_card[i])
        return total_score

    def draw_card(self, card, user_score) -> str:
        error_message = ""
        while True:
            # 引いたカードを出力
            print('カードを引きますかカードを引く場合はYを引かない場合はNを入力してください')
            s = input()
            if(s == "N"):
                break
            if(s != "Y"):
                error_message = "YとN以外が入力されました。強制終了します。"
                break
            drawn_card = card.draw_card()
            user_score.append(drawn_card.split("の")[1])
            print(f'あなたの引いたカードは{drawn_card}です')
            print(f'あなたの現在の得点は{self.calculate_total_score(user_score)}です')
        return error_message
