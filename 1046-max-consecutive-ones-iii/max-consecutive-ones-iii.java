class Solution {
    public int longestOnes(int[] nums, int k) {
        int n = nums.length;
        int left = 0;
        int right = 0;
        int zeroCount = 0;
        int longOnes = 0;

        for (right = 0; right < n; right++){
            if (nums[right]==0){
                zeroCount++;
            }

            while (zeroCount > k){
            if(nums[left] == 0){
                zeroCount--;
            }
            left++;
            }

            longOnes = Math.max(longOnes, right - left + 1);
        }

        return longOnes;
    }
}