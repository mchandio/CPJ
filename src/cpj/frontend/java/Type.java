package cpj.frontend.java;

public interface Type {
    String getName();

    boolean isAssignableFrom(Type other);
}