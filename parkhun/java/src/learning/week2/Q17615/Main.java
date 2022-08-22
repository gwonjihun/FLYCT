package learning.week2.Q17615;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 공 모으기
 * 
 * @since 2022. 8. 16. 오후 5:31:19
 * @author "KyungHun Park"
 *
 * @modified 2022. 8. 16. 오후 5:31:19 || Kyunghun Park || 최초 생성
 *
 */
public class Main {
    // 공의 개수
    private static int N;
    // 공의 색을 담은 배열
    private static char[] arr;

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        arr = new char[N];

        // 입력받은 공의 색
        String S = br.readLine();

        // 배열에 공의 색 입력
        for (int n = 0; n < N; n++) {
            arr[n] = S.charAt(n);
        }

        // 최소 이동횟수
        int result = Integer.MAX_VALUE;

        // 왼쪽으로 빨간 공 모으기
        result = Math.min(result, leftMove('R', 'B'));
        // 왼쪽으로 파란 공 모으기
        result = Math.min(result, leftMove('B', 'R'));
        // 오른쪽으로 빨간 공 모으기
        result = Math.min(result, rightMove('R', 'B'));
        // 오른쪽으로 파란 공 모으기
        result = Math.min(result, rightMove('B', 'R'));

        System.out.println(result);
    }

    /**
     * 왼쪽으로 모으기
     * 
     * @param firstBall  : 모으는데 기준이 될 공
     * @param secondBall : firstBall의 반대 색의 공
     * @return : 이동 횟수
     *
     * @since 2022. 8. 16. 오후 5:32:34
     * @author "KyungHun Park"
     * 
     * @modified 2022. 8. 16. 오후 5:32:34 || Kyunghun Park || 최초 생성
     *
     */
    private static int leftMove(char firstBall, char secondBall) {

        // 이동 횟수
        int count = 0;
        // 왼쪽부터 진행할 때 가장 처음 secondBall을 만나고 난 후의 firstBall의 개수
        boolean jump = false;

        // 왼쪽부터 진행
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

    /**
     * 오른쪽으로 공 모으기
     * 
     * @param firstBall  : 모으는데 기준이 될 공
     * @param secondBall : firstBall의 반대 색의 공
     * @return : 이동 횟수
     *
     * @since 2022. 8. 16. 오후 5:33:14
     * @author "KyungHun Park"
     * 
     * @modified 2022. 8. 16. 오후 5:33:14 || Kyunghun Park || 최초 생성
     *
     */
    private static int rightMove(char firstBall, char secondBall) {

        // 이동 횟수
        int count = 0;
        // 오른쪽부터 진행할 때 가장 처음 secondBall을 만나고 난 후의 firstBall의 개수
        boolean jump = false;

        // 오른쪽부터 진행
        for (int i = N - 1; i >= 0; i--) {
            if (arr[i] == firstBall && jump) {
                count++;
                continue;
            }

            // 가장 처음 secondBall을 만나는 경우
            if (arr[i] == secondBall) {
                jump = true;
            }
        }
        return count;
    }

}
