from typing import List
from Card import Card
from PlayerBase import PlayerBase


class User(PlayerBase):

    """
    ユーザーが引いたカードの合計点を計算する
    """

    def total_score(self, user_draw_card):
        #ユーザーが引いたカードの合計点
        total_score = 0
        # ユーザーが引いたカードの枚数
        n = len(user_draw_card)
        for i in range(n):
            a = int(user_draw_card[i])
            total_score += a
        return total_score
