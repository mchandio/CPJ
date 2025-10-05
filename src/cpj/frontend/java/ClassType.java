package cpj.frontend.java;

public interface ClassType extends Type {
    ClassType getSuperclass();

    boolean isSubclassOf(ClassType other);
}