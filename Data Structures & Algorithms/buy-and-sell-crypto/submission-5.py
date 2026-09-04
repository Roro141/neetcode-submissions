class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #well number one you can't sell and buy on the same day, additonally you woud buy before you sell
        #easy bruth force is to do a double for loop and chekc eveyr combo
        #wait profit is you want to buy on a low day and sell on a high day and make money
        
        #need  to initialize the bairbale
        max_profit=0
        
        #currently the mimimun price is the first price
        min_price=prices[0]

        for i in range(len(prices)):
            min_price=min(prices[i], min_price)

            profit=prices[i]-min_price

            max_profit=max(max_profit, profit)

        return max_profit