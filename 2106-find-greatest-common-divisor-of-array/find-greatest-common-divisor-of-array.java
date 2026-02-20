class Solution {
    public int findGCD(int[] nums) {
        int max=Integer.MIN_VALUE;
        int min=Integer.MAX_VALUE;
        for(int num : nums){
            max=Math.max(max,num);
            min=Math.min(min,num);
        }
        return gcd(max,min);
    }
    public int gcd(int a,int b){
        return b==0 ? a : gcd(b,a%b);
    }
}