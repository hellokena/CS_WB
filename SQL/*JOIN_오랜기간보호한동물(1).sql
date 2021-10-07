-- 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의
-- NAME과 DATETIME
-- 단, INS.DATETIME으로 정렬
SELECT INS.NAME, INS.DATETIME
FROM ANIMAL_INS INS LEFT OUTER JOIN ANIMAL_OUTS OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID -- 조인 조건(반드시 필요)
WHERE OUTS.ANIMAL_ID IS NULL -- 아직 입양을 못 간 동물 중
ORDER BY INS.DATETIME -- INS.DATETIME으로 정렬
LIMIT 3; -- 3마리

-- 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리이므로
-- OUTS.DATETIME - INS.DATETIME에서 OUTS.DATETIME이 존재하지 않으므로 불가
-- 그냥 INS.DATETIME이 가장 작은거!
