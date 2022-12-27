class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        
        
        bulls = 0
        cows = 0
        
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                bulls += 1
                secret = secret[:i] + 'x' + secret[i+1:]
                guess = guess[:i] + 'x' + guess[i+1:]
        
        
        sDigits = {'0': 0, '1': 0, '2': 0,'3': 0,'4': 0,'5': 0,'6': 0,'7': 0,'8': 0,'9': 0}
        gDigits = {'0': 0, '1': 0, '2': 0,'3': 0,'4': 0,'5': 0,'6': 0,'7': 0,'8': 0,'9': 0}
        
        for letter in secret:
            if letter != 'x':
                sDigits[letter] += 1
        
        for letter in guess:
            if letter != 'x':
                gDigits[letter] += 1
        
        
        for key in sDigits.keys():
            cows += min(sDigits[key], gDigits[key])
        
        return "{}A{}B".format(bulls,cows)
        
        
        