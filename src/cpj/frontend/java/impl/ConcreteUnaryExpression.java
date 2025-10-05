package cpj.frontend.java.impl;

import cpj.frontend.java.*;

public class ConcreteUnaryExpression implements UnaryExpression {
    private final Expression operand;
    private final String operator;
    private final Type type;

    public ConcreteUnaryExpression(Expression operand, String operator, Type type) {
        this.operand = operand;
        this.operator = operator;
        this.type = type;
    }

    @Override
    public Type getType() {
        return type;
    }

    @Override
    public Expression getOperand() {
        return operand;
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