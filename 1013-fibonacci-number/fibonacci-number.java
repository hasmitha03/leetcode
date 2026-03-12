class Solution {
    public int fib(int n) {
       if(n==0) return 0;
        int f=1;
        int g=0;
        for(int i=1;i<n;i++){
            f=f+g;
        g=f-g;

        }
        return f; 
    }
}