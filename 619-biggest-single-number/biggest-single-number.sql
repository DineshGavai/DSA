SELECT MAX(num) AS num
FROM (
    select num
    from MyNumbers
    group by num
    having count(*) =1
)t;