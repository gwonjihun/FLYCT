package learning.week1.Q9012;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 좌우 괄호의 짝 맞추기
 * @since 2022. 8. 2. 오후 3:54:17
 * @author "KyungHun Park"
 *
 * @modified 2022. 8. 2. 오후 3:54:17 || Kyunghun Park || 최초 생성
 *
 */
public class Main {

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        // TC 개수
        int N = Integer.parseInt(br.readLine());

        for (int n = 0; n < N; n++) {
            // 한줄 입력
            String str = br.readLine();

            // '(' 괄호의 개수
            int cnt = 0;

            // 한 줄의 한 글자씩
            line: for (char smallWord : str.toCharArray()) {

                switch (smallWord) {
                // 왼쪽 소괄호인 경우
                case '(':
                    cnt++;
                    break;

                // 오른쪽 소괄호인 경우
                case ')':
                    cnt--;
                    // cnt가 음수가 되면 짝이 맞지 않음
                    if (cnt < 0) {
                        // line 부분 break
                        break line;
                    }
                    break;
                }
            }

            // 괄호가 모두 소진된 경우
            if (cnt == 0) {
                sb.append("YES\n");
            } else {
                // 나머지의 경우
                sb.append("NO\n");
            }
        }
        
        System.out.println(sb);
    }

}
