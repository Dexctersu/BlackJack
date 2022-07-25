from os import remove
import random
import Card


def main():

    print("ゲームを開始します")
    nos = [str(i) for i in range(1, 14)]

    nos[0] = "A"
    nos[10] = "J"
    nos[11] = "Q"
    nos[12] = "K"
    c = Card.Card(["ハート", "スペード", "ダイヤ", "クラブ"], nos)
    # 引いたカードを出力
    print(f'あなたの引いたカードは{c.draw_card()}です')
    print(f'あなたの引いたカードは{c.draw_card()}です')
    print(f'残りのカードは{c.decks}')


if __name__ == '__main__':
    main()
