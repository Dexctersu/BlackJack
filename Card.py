
class Card:
    
    def __init__(self,marks,nos):
        self.marks=marks
        self.nos =nos


c = Card(["ハート", "スペード", "ダイヤ", "クラブ"],[str(i) for i in range(1,14)])
print(c)
