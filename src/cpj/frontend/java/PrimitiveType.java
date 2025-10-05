package cpj.frontend.java;

public interface PrimitiveType extends Type {
    boolean isNumeric();

    boolean isIntegral();

    boolean isFloatingPoint();
}