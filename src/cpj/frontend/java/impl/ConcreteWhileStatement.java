package cpj.frontend.java.impl;

import cpj.frontend.java.*;

public class ConcreteWhileStatement implements WhileStatement {
    private final Expression condition;
    private final Statement body;

    public ConcreteWhileStatement(Expression condition, Statement body) {
        this.condition = condition;
        this.body = body;
    }

    @Override
    public Expression getCondition() {
        return condition;
    }

    @Override
    public Statement getBody() {
        return body;
    }

    @Override
    public void accept(StatementVisitor visitor) {
        visitor.visit(this);
    }
}