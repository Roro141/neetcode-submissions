class Solution {
    public int maxProfit(int[] prices) {
        //so i can pick a day to buy from, and then a day to sell
        // to calculate profit, I want the max profit, so this is two pointer question
        int l=0; //time for user to buy stock
        int r=1; // time to sell stock
        int maxProfit=0; 
        while(r<prices.length)
        {
           if(prices[l]<prices[r])
           {
            //left poiunter will stay in place
             int currProfit= prices[r]-prices[l]; //current profit
             maxProfit=Math.max(maxProfit, currProfit); //find the max profit 
           }
           else
           {
             l=r;// if the new profit ins't greater, move the day to buy to the right
           }
           //check the next day
           r++;
        }
        return maxProfit;
    }
}
