-- ANIMAL_INS 테이블에서 가장 먼저 들어온(DATETIME이 가장 작은) 동물의 시간
SELECT MIN(DATETIME) AS '시간'
FROM ANIMAL_INS;
