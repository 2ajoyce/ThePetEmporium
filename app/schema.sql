drop table if exists pets;
create table pets (
  id integer primary key,
  type text not null,
  name text not null,
  age integer not null,
  weight real not null,
  hungry integer not null,
  photo text not null
);