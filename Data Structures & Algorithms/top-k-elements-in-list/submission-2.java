class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Count frequencies
        Map<Integer, Integer> freqMap = new HashMap<>();
        for (int num : nums) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        // Get unique numbers and sort by frequency descending
        List<Integer> uniqueNums = new ArrayList<>(freqMap.keySet());
        uniqueNums.sort((n1, n2) -> freqMap.get(n2) - freqMap.get(n1));

        // Take top k elements
        int[] output = new int[k];
        for (int i = 0; i < k; i++) {
            output[i] = uniqueNums.get(i);
        }

        return output;
    }
}
