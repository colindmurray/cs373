// ----------------------
// SingletonPattern2.java
// ----------------------

class Eager {
    private static final Eager _only = new Eager();

    private Eager ()
        {}

    public static Eager only () {
        return _only;}

    public String f () {
        return "Eager.f()";}}

class Lazy {
    private static Lazy _only;

    private Lazy ()
        {}

    public static Lazy only () {
        if (Lazy._only == null)
            Lazy._only = new Lazy();
        return Lazy._only;}

    public String f () {
        return "Lazy.f()";}}

final class SingletonPattern2 {
    public static void main (String[] args) {
        System.out.println("SingletonPattern2.java");

        assert Eager.only()     == Eager.only();
        assert Eager.only().f() == "Eager.f()";

        assert Lazy.only()     == Lazy.only();
        assert Lazy.only().f() == "Lazy.f()";

        System.out.println("Done.");}}
