-- ANIMAL_INS 테이블에서 같은 이름이 2번 이상 쓰인 이름과 갯수를 출력
-- 단, 이름이 없는 동물은 집계에서 죄외, 결과는 이름순으로 조회
SELECT NAME, COUNT(NAME)
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(NAME)>=2
ORDER BY NAME;
