package learning.week2.Q20310;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 타노스 0 과 1을 반으로 줄인다.
 * @since 2022. 8. 16. 오후 4:55:47
 * @author "KyungHun Park"
 *
 * @modified 2022. 8. 16. 오후 4:55:47 || Kyunghun Park || 최초 생성
 *
 */
public class Main {

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // 결과값
        StringBuilder sb = new StringBuilder();
        
        // 입력받은 0과 1
        String S = br.readLine();

        // 0의 개수
        int zeroCnt = 0;
        // 1의 개수
        int oneCnt = 0;

        char[] arr = new char[S.length()];
        
        // 0과 1의 개수 확인 및 배열에 입력
        for (int s = 0; s < S.length(); s++) {
            if (S.charAt(s) == '0') {
                zeroCnt++;
            } else {
                oneCnt++;
            }
            arr[s] = S.charAt(s);
        }

        // 타노스 0과 1의 개수를 반으로
        zeroCnt /= 2;
        oneCnt /= 2;

        // 1인 경우 앞에서부터 1삭제
        for (int i = 0; i < S.length() && oneCnt != 0; i++) {
            if (arr[i] == '1') {
                oneCnt--;
                arr[i] = '9';
            }
        }

        // 0인 경우 뒤에서부터 0삭제
        for (int i = S.length() - 1; i >= 0 && zeroCnt != 0; i--) {
            if (arr[i] == '0') {
                zeroCnt--;
                arr[i] = '9';
            }
        }
        
        // 배열 결과 출력
        for(char str : arr) {
            if(str != '9') {
                sb.append(str);
            }
        }

        System.out.println(sb);
    }

}
