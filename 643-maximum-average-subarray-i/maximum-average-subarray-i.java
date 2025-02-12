class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int n = nums.length;
        double maxVal = 0;

        for (int i = 0; i<k; i++){
            maxVal += nums[i];
        }

        double windowMax = maxVal;

        for (int i = k; i<n; i++){
            windowMax += nums[i] - nums[i-k];
            maxVal = Math.max(windowMax, maxVal);
        }

        return maxVal/k;
    }
}