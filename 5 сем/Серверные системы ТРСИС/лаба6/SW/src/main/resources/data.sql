create table if not exists user (login varchar(40), pass_hash varchar(128));
create table if not exists transporters (id integer ,name varchar(128), type integer);
create table if not exists TimeTable (TIMETABLE_ID integer ,TIMETABLE_NAME varchar(128), TIMETABLE_TYPE integer);

insert into transporters(id,name, type) values (1,'MosBus', 1);
insert into transporters(id,name, type) values (2,'SpbRailways', 2 );
insert into transporters(id,name, type) values (3,'SpbMetro',  2);
insert into transporters(id,name, type) values (4,'RZD', 2);

insert into TimeTable(TIMETABLE_ID,TIMETABLE_NAME, TIMETABLE_TYPE) values (1, '123', 3);
insert into TimeTable(TIMETABLE_ID,TIMETABLE_NAME, TIMETABLE_TYPE) values (2, '123', 2);
insert into TimeTable(TIMETABLE_ID,TIMETABLE_NAME, TIMETABLE_TYPE) values (3,'123', 1);
insert into TimeTable(TIMETABLE_ID,TIMETABLE_NAME, TIMETABLE_TYPE) values (4, '123', 2);
insert into TimeTable(TIMETABLE_ID,TIMETABLE_NAME, TIMETABLE_TYPE) values (5, '123', 1);
insert into TimeTable(TIMETABLE_ID,TIMETABLE_NAME, TIMETABLE_TYPE) values (6, '123', 3);

--login guest password hello
insert into user(login, pass_hash) values ('guest','$2a$10$6mf3CesQx9eRGB4B3sjr8e1eSr5cYO/zt87bwYVdA4O8rmjDMDdHO');
insert into user(login, pass_hash) values ('ewokasi','$2a$10$6mf3CesQx9eRGB4B3sjr8e1eSr5cYO/zt87bwYVdA4O8rmjDMDdHO');

