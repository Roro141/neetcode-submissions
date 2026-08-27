class Solution {
    public int maxArea(int[] heights) {
        //the best apprach would be using two pointers
        //that way the pointer can represent the width of the box
        //the box can only be as big as the minimin of th eheigth at the pointers
        //we need initize the pointers
        int l=0;
        int r=heights.length-1;
        int maxArea=0;
        while(l<r)
        {
            //first we need to clauclate the area
            int leftHeight= heights[l];
            int rigthHeight= heights[r];
            int height=Math.min(leftHeight,rigthHeight);
            int width=r-l;
            int currArea= height*width;
            if(maxArea<currArea)
            {
                maxArea=currArea;
            }
            //in roder to maxmize the area, if we decrease wdith we need to maximize heigth, so we want to move th eointer at the less heigtt
            if(leftHeight<rigthHeight)
            {
                l++;
            }
            else
            {
                r--;
            }
        } 
        return maxArea;
    }
}
