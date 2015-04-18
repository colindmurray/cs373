/*
CS373: Quiz #33 (7 pts)
*/

create table Student (sID   int,  sName text,    GPA        float, sizeHS   int);
create table Apply   (sID   int,  cName text,    major      text,  decision boolean);
create table College (cName text, state char(2), enrollment int);

/* -----------------------------------------------------------------------
 1. Write a query to delete students who applied to two or more majors.
    (6 pts)
*/

delete
    from Student
    where sID in
        (select sID
            from Apply
            group by sID
            having count(distinct major) > 2);
