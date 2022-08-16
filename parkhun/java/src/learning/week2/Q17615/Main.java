package learning.week2.Q17615;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static int N;
    private static char[] arr;

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        arr = new char[N];

        String S = br.readLine();

        for (int n = 0; n < N; n++) {
            arr[n] = S.charAt(n);
        }

        int result = Integer.MAX_VALUE;

        result = Math.min(result, leftMove('R', 'B'));
        result = Math.min(result, leftMove('B', 'R'));
        
        result = Math.min(result, rightMove('R', 'B'));
        result = Math.min(result, rightMove('B', 'R'));

        System.out.println(result);
    }

    private static int leftMove(char firstBall, char secondBall) {
        int count = 0;
        boolean jump = false;

        for (int i = 0; i < N; i++) {
            if (arr[i] == firstBall && jump) {
                count++;
                continue;
            }

            if (arr[i] == secondBall) {
                jump = true;
            }
        }
        return count;
    }

    private static int rightMove(char firstBall, char secondBall) {
        int count = 0;
        boolean jump = false;

        for (int i = N - 1; i >= 0; i--) {
            if (arr[i] == firstBall && jump) {
                count++;
                continue;
            }

            if (arr[i] == secondBall) {
                jump = true;
            }
        }
        return count;
    }

}
