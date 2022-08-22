package learning.week2.Q8979;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

/**
 * 올림픽 등수 매기기
 * 
 * @since 2022. 8. 8. 오후 9:14:26
 * @author "KyungHun Park"
 *
 * @modified 2022. 8. 8. 오후 9:14:26 || Kyunghun Park || 최초 생성
 *
 */
public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // 참여 국가 수
        int N = Integer.parseInt(st.nextToken());
        // 등수를 알고 싶은 국가 수
        int K = Integer.parseInt(st.nextToken());

        // 국가 별 성적
        int[][] rank = new int[N][4];

        // 국가별 성적 입력
        for (int n = 0; n < N; n++) {
            st = new StringTokenizer(br.readLine());
            for (int m = 0; m < 4; m++) {
                rank[n][m] = Integer.parseInt(st.nextToken());
            }
        }

        // 정렬 함수
        Arrays.sort(rank, new Comparator<int[]>() {

            @Override
            public int compare(int[] o1, int[] o2) {

                // 금메달 개수가 같은 경우
                if (o1[1] == o2[1]) {
                    // 은메달 개수가 같은 경우
                    if (o1[2] == o2[2]) {
                        // 동메달 순으로 정렬
                        return o2[3] - o1[3];
                    } else {
                        // 은메달 순으로 정렬
                        return o2[2] - o1[2];
                    }
                } else {
                    // 금메달 순으로 정렬
                    return o2[1] - o1[1];
                }
            }
        });

        // 등수를 담은 변수
        int rate = 1;
        // 같은 등수의 국가 개수를 담은 변수
        int count = 1;

        // 원하는 국가가 1등인 경우
        if (rank[0][0] == K) {
            System.out.println(1);
        } else {
            for (int n = 1; n < N; n++) {
                // 금, 은, 동 중 개수가 하나라도 다른 경우
                if ((rank[n][1] != rank[n - 1][1]) || (rank[n][2] != rank[n - 1][2]) || (rank[n][3] != rank[n - 1][3])) {
                    rate += count;
                    count = 1;
                } else {
                    // 금, 은, 동의 개수가 모두 같은 경우
                    count++;
                }

                if (rank[n][0] == K) {
                    System.out.println(rate);
                    break;
                }
            }
        }
    }
}
