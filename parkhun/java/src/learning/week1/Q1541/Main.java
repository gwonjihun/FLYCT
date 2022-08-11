package learning.week1.Q1541;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 잃어버린 괄호, 괄호를 임의로 지정하여 최소의 수 찾기
 * 
 * @since 2022. 8. 2. 오후 3:44:37
 * @author "KyungHun Park"
 *
 * @modified 2022. 8. 2. 오후 3:44:37 || Kyunghun Park || 최초 생성
 *
 */
public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // -까지 자르기
        StringTokenizer st = new StringTokenizer(br.readLine(), "-");

        // 결과 값, 비교할 때 다른 수와 겹치지 않기 위해 범위 밖 최대값 설정
        int sum = Integer.MAX_VALUE;

        // 자른 수가 남아 있을 때까지
        while (st.hasMoreTokens()) {

            // 각각의 수를 저장할 변수
            int temp = 0;

            // -까지 자른 수에서 +마다 나누기
            StringTokenizer stPlus = new StringTokenizer(st.nextToken(), "+");

            // +로 자른 수가 남아 있을 때까지
            while (stPlus.hasMoreTokens()) {
                temp += Integer.parseInt(stPlus.nextToken());
            }

            // 가장 처음의 경우
            if (sum == Integer.MAX_VALUE) {
                sum = temp;
            } else { // 나머지의 경우
                sum -= temp;
            }
        }

        System.out.println(sum);

    }

}
