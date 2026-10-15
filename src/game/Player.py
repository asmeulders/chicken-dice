from Hand import Hand, EmptyHand

class Player():
    def __init__(self, id: int):
        self.player_id = id
        self.score = 0
        self.hand = EmptyHand()

    def get_player_id(self) -> int:
        return self.player_id

    def get_score(self) -> int:
        return self.score

    def get_hand(self) -> Hand:
        return self.hand

    def set_hand(self, hand) -> None:
        self.hand = hand