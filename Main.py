import imp
import Card
from User import User


def main():

    print("ゲームを開始します")

    user = User()
    card = Card.Card()
    # 引いたカードを出力
    user_score = []
    for _ in range(2):
        drawn_card = card.draw_card()
        user_score.append(drawn_card.split("の")[1])
        print(f'あなたの引いたカードは{drawn_card}です')
    print(f'ディーラーの引いたカードは{card.draw_card()}です')
    print(f'ディーラーの2枚目のカードは分かりません')
    print(f'あなたの現在の得点は{user.calculate_total_score(user_score)}です')
    print(user.draw_card(card, user_score))
    # print(f'残りの山札は{c.decks}')


if __name__ == '__main__':
    main()
