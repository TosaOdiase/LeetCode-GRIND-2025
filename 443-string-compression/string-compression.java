class Solution {
    public int compress(char[] chars) {
        
        int write = 0;
        int read = 0;
        if (chars == null || chars.length == 0){
            return write;
            }
        while (read < chars.length){
            char currentChar = chars[read];
            int counter = 0;

            while(read < chars.length && chars[read] == currentChar){
                read++;
                counter++;
            }
        

            chars[write++] = currentChar;

            if (counter > 1){
                for (char c: Integer.toString(counter).toCharArray()){
                    chars[write++] = c;
                }
            }
        }

        return write;
    }
}