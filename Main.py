import imp
import Card
from User import User
from Dealer import Dealer


def main():

    print("ゲームを開始します")

    user = User()
    dealer = Dealer()
    card = Card.Card()
    # 引いたカードを出力
    user_score = []
    dealer_score=[]
    for _ in range(2):
        drawn_card = card.draw_card()
        user_score.append(drawn_card.split("の")[1])
        print(f'あなたの引いたカードは{drawn_card}です')
    for _ in range(2):
        dealer_score.append(card.draw_card())
    print(f'ディーラーの引いたカードは{dealer_score[0]}です')
    print(f'ディーラーの2枚目のカードは分かりません')
    print(f'あなたの現在の得点は{user.calculate_total_score(user_score)}です')
    print(user.draw_card(card, user_score))
    print(f'ディーラーの2枚目のカードは{dealer_score[1]}でした')
    dealer_score[0]=dealer_score[0].split("の")[1]
    dealer_score[1]=dealer_score[1].split("の")[1]
    print(f'ディーラーの現在の得点は{dealer.calculate_total_score(dealer_score)}です')
    print(f'ディーラーの得点は{dealer.draw_card(card,dealer_score)}です')
    print(f'あなたの得点は{user.calculate_total_score(user_score)}です')
    if abs(21-user.calculate_total_score(user_score)) < abs(21-dealer.calculate_total_score(dealer_score)):
        print("あなたの勝ちです")
    else:
        print("ディーラーの勝ちです")
    print("ブラックジャック終了!!!")
    # print(f'残りの山札は{c.decks}')


if __name__ == '__main__':
    main()
