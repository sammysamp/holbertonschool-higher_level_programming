-- LEFT JOIN
select distinct(s.title) from tv_shows s
LEFT JOIN tv_show_genres t on
s.id = t.show_id
where s.id not in (select t.show_id from tv_show_genres t INNER JOIN tv_genres g on
t.genre_id = g.id where g.name = 'Comedy')
order by 1 asc;

