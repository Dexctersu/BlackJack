import Card
from Deck import Deck
from User import User


def main():

    print("ゲームを開始します")

    user = User()
    dealer = User()
    deck = Deck()

    # プレイヤーが最初のカードを2枚引く
    user.hand.append(deck.draw("あなた"))
    user.hand.append(deck.draw("あなた"))

    # ディーラーがカードを2枚引く
    dealer.hand.append(deck.draw("ディーラー"))
    dealer.hand.append(deck.draw("ディーラー", hide=True))

    print(f"あなたの現在の得点は{user.calculate_total_score()}です")

    # ユーザーのターン
    while True:
        print("カードを引きますか? 引く場合はYを、引かない場合はNを入力してください。")
        s = input()
        if(s == "Y" or s == "y"):

            user.hand.append(deck.draw("あなた"))

            print(f"あなたの現在の得点は{user.calculate_total_score()}です")

            if(user.is_burst()):
                print("21を超えました")
                print("あなたの負けです")
                exit()

        elif(s == "N" or s == "n"):
            break
        else:
            print("YかNを入力してください。")

    print(f"ディーラーの2枚目のカードは{dealer.hand[1].card_name}でした")

    print(f"ディーラーの現在の得点は{dealer.calculate_total_score()}です")

    while dealer.calculate_total_score() < 17:
        dealer.hand.append(deck.draw("ディーラー"))

    # ユーザーとディーラーの合計点
    print(f"あなたの得点は{user.calculate_total_score()}です。")
    print(f"ディーラーの得点は{dealer.calculate_total_score()}です")

    if dealer.is_burst() or abs(21-user.calculate_total_score()) < abs(21-dealer.calculate_total_score()):
        print("あなたの勝ちです")
    elif user.calculate_total_score() == dealer.calculate_total_score():
        print("引き分けです")
    else:
        print("ディーラーの勝ちです")

    print("ブラックジャック終了")


if __name__ == '__main__':
    main()
