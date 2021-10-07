-- ANIMAL_INS 테이블에서 Lucy, Ella, Pickle, Rogan, Sabrina, Mitty를 찾아서
-- ANIMAL_ID, NAME, SEX_UPON_INTAKE를 출력
-- 단, ANIMAL_ID로 정렬하여 출력
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY ANIMAL_ID;
