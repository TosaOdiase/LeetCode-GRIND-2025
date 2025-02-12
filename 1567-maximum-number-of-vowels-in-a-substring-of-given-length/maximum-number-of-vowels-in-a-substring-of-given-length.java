class Solution {
    public int maxVowels(String s, int k) {
        int n = s.length();
        int maxVowel = 0;
        int windowMax = 0;
        String vowels = "aeiou";

        for (int i = 0; i < k; i++){
            if (vowels.indexOf(s.charAt(i))!= -1){
                maxVowel++;
            }
        }

        windowMax = maxVowel;

        for (int i = k; i< n; i++){
            if(vowels.indexOf(s.charAt(i))!= -1){
                windowMax++;  
            }
            if(vowels.indexOf(s.charAt(i-k))!= -1){
                windowMax--;  
            }

            maxVowel = Math.max(windowMax, maxVowel);

            if(maxVowel == k){
                return k;
            }
        }

        return maxVowel;
    }
}