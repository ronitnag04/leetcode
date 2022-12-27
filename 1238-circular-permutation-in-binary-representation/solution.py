class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        def getBinary(n):
            length = 2**n
            arr = []
            trues = [False for i in range(n)]
            for i in range(length):
                if i == 0:
                    arr.append(0)
                else:
                    bit = n
                    while i % (2**(bit-1)) != 0:
                        bit -= 1
                        
                    if trues[bit-1]:
                        arr.append(arr[-1] - 2**(bit-1))
                    else:
                        arr.append(arr[-1] + 2**(bit-1))
                    trues[(bit-1)] = not trues[(bit-1)]
                
            return arr
        
        arr = getBinary(n)
        i = arr.index(start)
        return arr[i:] + arr[:i]

"""        
0 1

0 1 3 2

0 1 3 2  6 7 5 4

0 1 3 2  6 7 5 4   12 13 15 14  10 11 9 8
 1 2 1  4 1 2 1  8   1  2  1   4  1  2  1
 + + -  + + - -  +   +  +  -   -  +  -  -

0 1 3 2  6 7 5 4   12 13 15 14  10 11 9 8   24 25 27 26 30 31 29 28 20 21 23 22 18 19 17 16 
 1 2 1 4  1 2 1  8   1  2  1   4  1  2 1  16  1  2  1  4  1  2  1  8  1  2  1  4  1  2  1
 + + - +  + - -  +   +  +  -   -  +  - -   +  +  +  -  +  +  -  -  -  +  +  -  -  +  -  -
             1100                 1000
                   1001"""