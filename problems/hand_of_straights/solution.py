class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        cards = {}
        for num in hand:
            if num in cards:
                cards[num]+=1
            else:
                cards[num] = 1
                
        keys = sorted(list(cards.keys()))
        
        while keys:
            m = keys[0]
            groups = cards[m]
            for i in range(m, m+groupSize):
                
                if i not in keys:
                    return False
                
                cards[i] -= groups
                if cards[i] == 0 :
                    if i == keys[0]:
                        keys.pop(0)
                    else:
                        return False
            
            
        return True
        
        