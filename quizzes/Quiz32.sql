/*
CS373: Quiz #32 (7 pts)
*/

/* -----------------------------------------------------------------------
 1. The Self-Adaptive Process
    The first part of self-adaptivity is regular reviews of the process.
    Usually you do these with every iteration. At the end of each
    iteration, have a short meeting and ask yourself the following
    questions (culled from Norm Kerth)...
    List any TWO of the FOUR.
    [The New Methodology]
    (2 pts)

What did we do well?
What have we learned?
What can we do better?
What puzzles us?
*/

/* -----------------------------------------------------------------------
 2. Practices of Continuous Integration
    List any TWO of the TEN.
    [Continuous Integration]
    (2 pts)

Maintain a Single Source Repository
Automate the Build
Make Your Build Self-Testing
Everyone Commits To the Mainline Every Day
Every Commit Should Build the Mainline on an Integration Machine
Keep the Build Fast
Test in a Clone of the Production Environment
Make it Easy for Anyone to Get the Latest Executable
Everyone can see what's happening
Automate Deployment
*/

create table Student (sID   int,  sName text,    GPA        float, sizeHS   int);
create table Apply   (sID   int,  cName text,    major      text,  decision boolean);
create table College (cName text, state char(2), enrollment int);

/* -----------------------------------------------------------------------
 3. Write a query to compute the majors whose applicant's max GPA is less
    than the average.
    (2 pts)
*/

select major
    from Student
    inner join Apply using (sID)
    group by major
    having
        max(GPA)
        <
        (select avg(GPA) from Student);
