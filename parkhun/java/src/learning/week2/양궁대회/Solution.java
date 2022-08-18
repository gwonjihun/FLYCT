package learning.week2.양궁대회;

public class Solution {
    private static int n = 5;
    private static int[] info = { 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0 };
    private static int[] temp = {};
    private static int[] lion = new int[n];

    public static void main(String[] args) {

        solution(n, info);
    }

    private static int[] solution(int n, int[] info) {
        int[] answer = {};

        dfs(0, 0, info);

        return answer;
    }

    private static void dfs(int depth, int index, int[] info) {
        if (depth == n) {
            int aPoint = 0;
            int lPoint = 0;
            
            for(int i = 0 ; i < 11; i++) {
                
            }
        }

        for (int i = index; i <= 11; i++) {
            lion[i]++;
            dfs(depth + 1, index + 1, info);
        }
    }
}
