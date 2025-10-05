package cpj.frontend.java;

public interface BinaryExpression extends Expression {
    Expression getLeft();

    Expression getRight();

    String getOperator();
}