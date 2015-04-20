// ---------------------
// SingletonPattern.java
// ---------------------

class Singleton {
    ...

    public String f () {
        return "Singleton.f()";}}

final class SingletonPattern {
    public static void main (String[] args) {
        System.out.println("SingletonPattern.java");

        assert Singleton.only()     == Singleton.only();
        assert Singleton.only().f() == "Singleton.f()";

        System.out.println("Done.");}}
