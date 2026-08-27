class Solution {
    public int maxProfit(int[] prices) {
    //You want the max profits, and want to know the differnece between two points of the array
    // best approach is two pointers
    // one pointer left: is the day to buy
    int l=0;
    //one pointer rigth: the day to sell
    int r=0;
    //The day we sell can't be less than th ethe day we buy, so r must always be >0
    //default if there isno profit to be made
    int maxProf=0;
    while(r<prices.length)
    {
        //need to
        if(prices[r]>prices[l])
        {
            maxProf=Math.max(maxProf,(prices[r]-prices[l]));
        }
        else
        {
            l=r;
        }
        r++;
    }
    return maxProf;
}
}