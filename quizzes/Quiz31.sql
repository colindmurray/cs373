/*
CS373: Quiz #31 (7 pts)
*/

/* -----------------------------------------------------------------------
 1. The Joel Test consists of 12 questions.
    List any two.
    [The Joel Test]
    (2 pts)

 1. Do you use source control?
 2. Can you make a build in one step?
 3. Do you make daily builds?
 4. Do you have a bug database?
 5. Do you fix bugs before writing new code?
 6. Do you have an up-to-date schedule?
 7. Do you have a spec?
 8. Do programmers have quiet working conditions?
 9. Do you use the best tools money can buy?
10. Do you have testers?
11. Do new candidates write code during their interview?
12. Do you do hallway usability testing?
*/

create table Student (sID   int,  sName text,    GPA        float, sizeHS   int);
create table Apply   (sID   int,  cName text,    major      text,  decision boolean);
create table College (cName text, state char(2), enrollment int);

/* -----------------------------------------------------------------------
 2. Write a query to compute the average GPA of students applying to CS.
    (4 pts)
*/

select avg(GPA)
    from Student
    where sID in
        (select sID
            from Apply
                where major = 'CS');
