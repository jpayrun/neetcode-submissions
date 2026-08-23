class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cards = {}
        for card in hand:
            cards[card] = cards.get(card, 0) + 1
        n = len(hand)
        while n:
            m_key = float('inf')
            for key, val in cards.items():
                if val > 0:
                    m_key = min(key, m_key)
            i = 0
            # print(m_key)
            while i < groupSize:
                # print(i)
                if i + m_key in cards and cards[m_key+i] > 0:
                    cards[m_key+i]-=1
                    i+=1
                    n-=1
                else:
                    return False
        return True