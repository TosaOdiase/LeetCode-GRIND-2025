class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        // create hash sets for both number sets 
        // add the numbers from int list to the hash sets 
        //initilaize array list 
        //create a for loop with an if ststaemnt making sure different numbs are added to new array lists 
        //then Arrays.asList

        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();

        for (int num:nums1){set1.add(num);}
        for (int num:nums2) {set2.add(num);}

        List<Integer> diff1 = new ArrayList<>();
        for (int num: set1){
            if(! set2.contains(num)){
                diff1.add(num);
            }
        }

        List <Integer> diff2 = new ArrayList<>();
        for (int num: set2){
            if(! set1.contains(num)){
                diff2.add(num);
            }
        }

        return Arrays.asList(diff1,diff2);

    }
}