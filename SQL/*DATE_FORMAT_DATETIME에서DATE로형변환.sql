-- 2018-01-22 14:32:00 형식을 2018-01-22로 변경
SELECT ANIMAL_ID,NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') AS 날짜
FROM ANIMAL_INS
ORDER BY ANIMAL_ID

-- %Y : 2021, %y : 21
-- %M : October, %m : 10
-- %D : 7th, %d : 07
-- %W : Friday, %a : Fri, %w : 5(일요일이 0부터 시작) 등등 많음....
