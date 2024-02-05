class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder s=new StringBuilder();
        int i=0,j=0;
        while (i<word1.length()||j<word2.length()) {
            if (i<word1.length()){
                s.append(word1.charAt(i));
                i++;
            }
            if (j<word2.length()) {
                s.append(word2.charAt(j));
                j++;
            }
        }
        return s.toString();


    }
}
//javascript
/* 
function mergeStrings(word1, word2) {
    let result = [];
    
    let i = 0, j = 0;
    while (i < word1.length || j < word2.length) {
        if (i < word1.length) {
            result.push(word1[i]);
            i++;
        }
        
        if (j < word2.length) {
            result.push(word2[j]);
            j++;
        }
    }
    
    return result.join('');
}

// Example usage:
let word1 = "hello";
let word2 = "world";
let mergedString = mergeStrings(word1, word2);
console.log("Merged String:", mergedString);*/