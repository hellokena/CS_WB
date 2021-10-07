-- ANIMAL_INS 테이블에서 가장 최근에 들어온(DATETIME이 가장 큰) 동물의 시간
SELECT MAX(DATETIME) AS '시간'
FROM ANIMAL_INS;
