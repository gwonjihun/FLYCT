package learning.week1.Q1316;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 그룹 단어 체커, 연속된 알파벳은 계속 연속되어야 한다.
 * 
 * @since 2022. 8. 2. 오후 3:43:21
 * @author "KyungHun Park"
 *
 * @modified 2022. 8. 2. 오후 3:43:21 || Kyunghun Park || 최초 생성
 *
 */
public class Main {

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 결과를 담은 변수
        int answer = 0;

        // 총 테스트 케이스
        int N = Integer.parseInt(br.readLine());

        for (int n = 0; n < N; n++) {
            // 입력된 알파벳을 담을 배열
            char[] arr = new char[26];

            // 단어를 입력 받는 변수
            String str = br.readLine();

            // 단어의 길이만큼 반복
            for (int w = 0; w < str.length(); w++) {
                // 현재 알파벳
                char present = str.charAt(w);

                // str 길이를 벗어나지 않을 때
                if (w + 1 < str.length()) {

                    // 다음에 나올 알파벳
                    char next = str.charAt(w + 1);

                    // 현재와 다음 알파벳이 같은 경우
                    if (present == next) {
                        continue;
                    }
                    // 마지막 알파벳인 경우
                    else if (w == str.length()) {
                        arr[present - 97]++;
                    }
                    // 현재와 다음 알파벳이 다른 경우 현재 알파벳에 해당하는 배열에 1증가
                    else if (present != next) {
                        arr[present - 97]++;
                    }
                } else {
                    arr[present - 97]++;
                }
            }

            answer += count(arr);
        }
        System.out.println(answer);
    }

    /**
     * 배열에 저장된 값이 2이상인 배열을 찾아내는 함수
     * 
     * @param arr
     * @return :
     *
     * @since 2022. 8. 2. 오후 3:43:52
     * @author "KyungHun Park"
     * 
     * @modified 2022. 8. 2. 오후 3:43:52 || Kyunghun Park || 최초 생성
     *
     */
    public static int count(char[] arr) {
        int cnt = 1;
        
        for (int k : arr) {
            // 2이상인 경우 0을 리턴
            if (k > 1) {
                return 0;
            }
        }
        return cnt;
    }
}
