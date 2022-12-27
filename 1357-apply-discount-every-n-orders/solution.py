class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.curr = 1
        self.discount = discount
        self.products = {}
        for ID, price in zip(products, prices):
            self.products[ID] = price
        

    def getBill(self, product: List[int], amount: List[int]) -> float:
        bill = 0
        for ID, q in zip(product, amount):
            bill += self.products[ID]*q
        
        
        if self.curr == self.n:
            self.curr = 1
            return bill * (((100.0)-self.discount)/100.0)
        else:
            self.curr += 1
            return bill


        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)