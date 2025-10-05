package cpj.frontend.java;

public interface Expression {
    Type getType();

    void accept(ExpressionVisitor visitor);
}