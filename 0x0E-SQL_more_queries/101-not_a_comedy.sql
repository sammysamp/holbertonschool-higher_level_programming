-- LEFT JOIN
SELECT DISTINCT(s.title) FROM tv_shows s
LEFT JOIN tv_show_genres t ON
s.id = t.show_id
WHERE s.id NOT IN (SELECT t.show_id FROM tv_show_genres t INNER JOIN tv_genres g ON
t.genre_id = g.id WHERE g.name = 'Comedy')
ORDER BY 1 ASC;

