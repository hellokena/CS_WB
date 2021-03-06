SELECT ID, NAME, HOST_ID -- 4. 이에 해당하는 HOST_ID 값을 가진 행들만 조회
FROM PLACES
WHERE HOST_ID IN 
(SELECT HOST_ID -- 3. HOST_ID 선택
FROM PLACES
GROUP BY HOST_ID -- 1. HOST_ID 별로 묶은 다음
HAVING COUNT(HOST_ID) >= 2) -- 2. HOST_ID가 2개 이상인
ORDER BY ID; -- 5. ID 순으로 정렬
