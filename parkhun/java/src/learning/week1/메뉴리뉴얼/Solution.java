package learning.week1.메뉴리뉴얼;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * 메뉴 리뉴얼 / 가장 많이 시킨 메뉴를 합치기
 * 
 * @since 2022. 8. 5. 오후 5:47:59
 * @author "KyungHun Park"
 *
 * @modified 2022. 8. 5. 오후 5:47:59 || Kyunghun Park || 최초 생성
 *
 */
public class Solution {
    public static Map<String, Integer> map = new HashMap<>();

    /**
     * Test Case
     * 
     * @param args :
     *
     * @since 2022. 8. 5. 오후 5:48:56
     * @author "KyungHun Park"
     * 
     * @modified 2022. 8. 5. 오후 5:48:56 || Kyunghun Park || 최초 생성
     *
     */
    public static void main(String[] args) {
        String[] orders = { "XYZ", "XWY", "WXA" };
        int[] course = { 2, 3, 4 };

        System.out.println(Arrays.toString(solution(orders, course)));
    }

    /**
     * map을 통해 새로운 메뉴 추가
     * 
     * @param orders : 손님들이 주문한 메뉴를 담은 배열
     * @param course : 새로 만들 코스의 메뉴 개수를 담은 배열
     * @return : 새로 만들 코스 메뉴 조합
     *
     * @since 2022. 8. 5. 오후 5:49:06
     * @author "KyungHun Park"
     * 
     * @modified 2022. 8. 5. 오후 5:49:06 || Kyunghun Park || 최초 생성
     *
     */
    public static String[] solution(String[] orders, int[] course) {
        // 코스 메뉴를 담을 List
        List<String> answer = new ArrayList<>();

        // 코스 메뉴 개수마다 찾기
        for (int i = 0; i < course.length; i++) {
            // 새로운 코스를 담을 map
            map = new HashMap<>();

            // 가장 많이 주문 한 메뉴를 찾기 위한 변수
            int max = -1;

            // 메뉴 찾기
            for (int j = 0; j < orders.length; j++) {

                // 주문한 메뉴 정렬 ex) DCB -> BCD
                char[] temp = orders[j].toCharArray();
                Arrays.sort(temp);
                orders[j] = new String(temp);

                // course[i]의 개수에 맞는 메뉴 조합을 찾기 위한 함수
                dfs(orders[j], 0, 0, course[i], "");
            }

            // 가장 많이 주문한 조합의 수 찾기
            for (String key : map.keySet()) {
                max = Math.max(max, map.get(key));
            }

            // 가장 많이 주문한 조합의 수로 가장 많이 주문한 메뉴 조합 찾기
            for (String key : map.keySet()) {
                if (map.get(key) >= 2) {
                    if (max == map.get(key)) {
                        answer.add(key);
                    }
                }
            }
        }
        // 정답 정렬
        answer.sort(null);

        // 배열로 전달해주기 위해 변환
        return answer.toArray(new String[answer.size()]);
    }

    /**
     * 가능한 모든 메뉴 조합을 찾기 위한 DFS
     * 
     * @param menu       : 손님이 주문한 메뉴
     * @param idx        : 탐색 위치
     * @param depth      : 탐색한 깊이
     * @param menuLength : 코스에 들어갈 수 있는 메뉴의 개수
     * @param str        : 가능한 조합
     *
     * @since 2022. 8. 5. 오후 5:52:53
     * @author "KyungHun Park"
     * 
     * @modified 2022. 8. 5. 오후 5:52:53 || Kyunghun Park || 최초 생성
     *
     */
    public static void dfs(String menu, int idx, int depth, int menuLength, String str) {
        // 탐색한 깊이가 코스 메뉴 길이와 같아진 경우
        if (depth == menuLength) {
            // map에 코스 메뉴 저장
            map.put(str, map.getOrDefault(str, 0) + 1);
            return;
        }

        // 조건에 맞을때 까지 탐색
        for (int i = idx; i < menu.length(); i++) {
            dfs(menu, i + 1, depth + 1, menuLength, str.concat(String.valueOf(menu.charAt(i))));
        }
    }

}
