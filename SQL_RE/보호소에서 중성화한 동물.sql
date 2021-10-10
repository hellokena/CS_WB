-- 코드를 입력하세요
SELECT INS.ANIMAL_ID, INS.ANIMAL_TYPE, INS.NAME
FROM ANIMAL_INS INS, ANIMAL_OUTS OUTS
WHERE INS.ANIMAL_ID = OUTS.ANIMAL_ID
AND INS.SEX_UPON_INTAKE LIKE 'Intact%'
AND (OUTS.SEX_UPON_OUTCOME LIKE 'Spayed%' OR 'Neutered%'
     OR OUTS.SEX_UPON_OUTCOME LIKE 'Neutered%')
ORDER BY ANIMAL_ID;

-- 코드를 입력하세요
SELECT INS.ANIMAL_ID, INS.ANIMAL_TYPE, INS.NAME
FROM ANIMAL_INS INS, ANIMAL_OUTS OUTS
WHERE INS.ANIMAL_ID = OUTS.ANIMAL_ID
AND INS.SEX_UPON_INTAKE LIKE 'Intact%'
AND OUTS.SEX_UPON_OUTCOME NOT LIKE 'Intact%'
ORDER BY ANIMAL_ID;
