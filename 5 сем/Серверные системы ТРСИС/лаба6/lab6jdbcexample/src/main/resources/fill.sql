insert into SCHOOL (SCHOOL_NUMBER, SCHOOL_NAME) values (1, 'Факультет 1');
insert into SCHOOL (SCHOOL_NUMBER, SCHOOL_NAME) values (2, 'Факультет 2');
insert into SCHOOL (SCHOOL_NUMBER, SCHOOL_NAME) values (3, 'Факультет 3');
insert into SCHOOL (SCHOOL_NUMBER, SCHOOL_NAME) values (4, 'Факультет 4');
insert into SCHOOL (SCHOOL_NUMBER, SCHOOL_NAME) values (5, 'Факультет 5');

insert into BATCH (BATCH_NUMBER, BATCH_SCHOOL_ID) values ('111',1);
insert into BATCH (BATCH_NUMBER, BATCH_SCHOOL_ID) values ('112',1);
insert into BATCH (BATCH_NUMBER, BATCH_SCHOOL_ID) values ('113',1);
insert into BATCH (BATCH_NUMBER, BATCH_SCHOOL_ID) values ('121',1);
insert into BATCH (BATCH_NUMBER, BATCH_SCHOOL_ID) values ('122',1);
insert into BATCH (BATCH_NUMBER, BATCH_SCHOOL_ID) values ('123',1);
insert into BATCH (BATCH_NUMBER, BATCH_SCHOOL_ID) values ('411',4);
insert into BATCH (BATCH_NUMBER, BATCH_SCHOOL_ID) values ('412',4);
insert into BATCH (BATCH_NUMBER, BATCH_SCHOOL_ID) values ('413',4);
insert into BATCH (BATCH_NUMBER, BATCH_SCHOOL_ID) values ('421',4);
insert into BATCH (BATCH_NUMBER, BATCH_SCHOOL_ID) values ('422',4);
insert into BATCH (BATCH_NUMBER, BATCH_SCHOOL_ID) values ('423',4);

insert into STUDENT(STUD_FNAME,STUD_PNAME, STUD_LNAME,STUD_NUM_ZACH,STUD_BATCH_ID) values('Иван','Иванович','Иванов','А112/2016',1);
insert into STUDENT(STUD_FNAME,STUD_PNAME, STUD_LNAME,STUD_NUM_ZACH,STUD_BATCH_ID) values('Петр','Петрович','Петров','А113/2016',1);
insert into STUDENT(STUD_FNAME,STUD_PNAME, STUD_LNAME,STUD_NUM_ZACH,STUD_BATCH_ID) values('Сидор','Сидорович','Сидоров','А114/2016',2);
insert into STUDENT(STUD_FNAME,STUD_PNAME, STUD_LNAME,STUD_NUM_ZACH,STUD_BATCH_ID) values('Семен','Семенович','Семенов','А115/2016',2);
