package cpj.frontend.java.impl;

import cpj.frontend.java.*;

public class ConcreteReturnStatement implements ReturnStatement {
    private final Expression expression;

    public ConcreteReturnStatement(Expression expression) {
        this.expression = expression;
    }

    @Override
    public Expression getExpression() {
        return expression;
    }

    @Override
    public void accept(StatementVisitor visitor) {
        visitor.visit(this);
    }
}