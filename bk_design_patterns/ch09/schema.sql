CREATE TABLE if not exists tasks ( id integer primary key autoincrement, name char(100) not null, closed bool not null );

INSERT or ignore into tasks (id, name, closed) values (0, 'Start learning Pyramid', 0);

INSERT or ignore into tasks (id, name, closed) values (1, 'Do quick tutorial', 0);

INSERT or ignore into tasks (id, name, closed) values (2, 'Have some beer!', 0);