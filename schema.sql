drop table if exists pets;
create table pets (
  id integer primary key autoincrement,
  type text not null,
  name text not null,
  age integer not null,
  weight real not null,
  hungry integer not null,
  photo text not null
);
insert into pets values (1, 'Cat', 'Triangle', 12, 12.5, 0, '(=^o.o^=)__');