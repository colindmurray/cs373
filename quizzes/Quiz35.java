/*
CS373: Quiz #35 (7 pts)
*/

/* -----------------------------------------------------------------------
 1. What is the output of the following:
    (6 pts)

A.A()
B.f()
B.B()
*/

class A {
    public A () {
        System.out.println("A.A()");
        f();}

    public void f () {
        System.out.println("A.f()");}}

class B extends A {
    public B () {
        System.out.println("B.B()");}

    public void f () {
        System.out.println("B.f()");}}

final class Quiz35 {
    public static void main (String[] args) {
        A x = new B();}}
