class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        cards = Counter(hand)
        hand.sort()
        for card in hand:
            if cards[card]:
                for i in range(groupSize):
                    if card + i in cards:
                        cards[card+i]-=1
                    else:
                        return False
        return True