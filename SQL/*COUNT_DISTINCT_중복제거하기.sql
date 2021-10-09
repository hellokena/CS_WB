-- ANIMAL_INS 테이블에서 동물의 이름은 몇개인지 확인하는 SQL
-- 단, NULL은 집계하지 않으며, 중복되는 이름은 하나로 가정
SELECT COUNT(DISTINCT NAME) AS 'count'
FROM ANIMAL_INS;

-- COUNT(*) 하면 NULL이 포함되지만
-- COUNT(DISTINCT COL) 하면 NULL이 포함되지 않음
-- COUNT(COL)해도 NULL은 포함되지 않음
