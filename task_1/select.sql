SELECT * FROM tasks
WHERE user_id = 4;


SELECT * FROM tasks
WHERE status_id = (SELECT id FROM status WHERE name = 'new');


UPDATE tasks
SET status_id = (SELECT id FROM status WHERE name = 'in progress')
WHERE id = 1;


SELECT * FROM users
WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);


INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('New Task'
        , 'This is a new task description'
        , (SELECT id FROM status WHERE name = 'new')
        , 7);


SELECT * FROM tasks
WHERE status_id != (SELECT id FROM status WHERE name = 'completed');


DELETE FROM tasks
WHERE id = 31;


SELECT * FROM users
WHERE email LIKE '%@example.com';


UPDATE users
SET fullname = 'Updated User'
WHERE id = 2;


SELECT status.name, COUNT(tasks.id) AS task_count
FROM status
LEFT JOIN tasks ON status.id = tasks.status_id
GROUP BY status.name;


SELECT tasks.* FROM tasks
JOIN users ON tasks.user_id = users.id
WHERE users.email LIKE '%@example.com';


SELECT * FROM tasks
WHERE description IS NULL


SELECT users.fullname, tasks.title
FROM users
INNER JOIN tasks ON users.id = tasks.user_id
WHERE tasks.status_id = (SELECT id FROM status WHERE name = 'in progress');


SELECT users.fullname, COUNT(tasks.id) AS task_count
FROM users
LEFT JOIN tasks ON users.id = tasks.user_id
GROUP BY users.id;