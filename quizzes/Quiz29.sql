/*
CS373: Quiz #29 (7 pts)
*/

create table Student (sID   int,  sName text,    GPA        float, sizeHS   int);
create table Apply   (sID   int,  cName text,    major      text,  decision boolean);
create table College (cName text, state char(2), enrollment int);

/* -----------------------------------------------------------------------
 1. Explain the difference between the following two queries.
    (6 pts)

students who applied in CS and any non-EE major (but maybe EE, too)
students who applied in CS and not EE
*/

select sID
    from Student
    where
        sID in (select sID from Apply where major  = 'CS')
        and
        sID in (select sID from Apply where major != 'EE');

select sID
    from Student
    where
        sID     in (select sID from Apply where major = 'CS')
        and
        sID not in (select sID from Apply where major = 'EE');
