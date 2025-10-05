package cpj.frontend.java.impl;

import cpj.frontend.java.*;

public class ConcreteBinaryExpression implements BinaryExpression {
    private final Expression left;
    private final Expression right;
    private final String operator;
    private final Type type;

    public ConcreteBinaryExpression(Expression left, Expression right, String operator, Type type) {
        this.left = left;
        this.right = right;
        this.operator = operator;
        this.type = type;
    }

    @Override
    public Type getType() {
        return type;
    }

    @Override
    public Expression getLeft() {
        return left;
    }

    @Override
    public Expression getRight() {
        return right;
    }

    @Override
    public String getOperator() {
        return operator;
    }

    @Override
    public void accept(ExpressionVisitor visitor) {
        visitor.visit(this);
    }
}