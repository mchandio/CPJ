package cpj.frontend.java;

public interface UnaryExpression extends Expression {
    Expression getOperand();

    String getOperator();
}