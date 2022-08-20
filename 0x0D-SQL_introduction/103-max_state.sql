-- displays the max temperature of each state
SELECT `state`, MAX(`temp`) AS `max_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;
