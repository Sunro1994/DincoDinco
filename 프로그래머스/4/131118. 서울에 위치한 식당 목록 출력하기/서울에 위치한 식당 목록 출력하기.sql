-- 코드를 입력하세요
-- 1. 서울에 위치한
-- 2. 리뷰평균점수는 세번째 자리에서 반올림
-- 3. 평균점수를 기준으로 내림차순 정렬
-- 4. 평균점수가 같다면 즐겨찾기 수를 기준으로 내림차순
-- 식당 ID, 식당 이름, 음식 종류, 즐겨찾기수, 주소, 리뷰 평균 점수

SELECT I.REST_ID, I.REST_NAME, I.FOOD_TYPE, I.FAVORITES, I.ADDRESS, ROUND(AVG(R.REVIEW_SCORE),2) AS SCORE
FROM REST_INFO I
JOIN
REST_REVIEW R
ON I.REST_ID = R.REST_ID
WHERE I.ADDRESS LIKE '서울%'
GROUP BY
    I.REST_ID, I.REST_NAME, I.FOOD_TYPE, I.FAVORITES, I.ADDRESS
ORDER BY SCORE DESC, FAVORITES DESC;