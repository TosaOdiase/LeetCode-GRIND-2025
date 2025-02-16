class Solution {
    public int largestAltitude(int[] gain) {
        int maxAlt = 0;
        int currentAlt = 0;
        for (int num:gain){
            currentAlt += num;
            maxAlt = Math.max(maxAlt, currentAlt);
        }
        return maxAlt;
    }
}