package cpj.frontend.java.impl;

import cpj.frontend.java.*;

public class ConcreteForStatement implements ForStatement {
    private final Statement initialization;
    private final Expression condition;
    private final Statement update;
    private final Statement body;

    public ConcreteForStatement(Statement initialization, Expression condition, Statement update, Statement body) {
        this.initialization = initialization;
        this.condition = condition;
        this.update = update;
        this.body = body;
    }

    @Override
    public Statement getInitialization() {
        return initialization;
    }

    @Override
    public Expression getCondition() {
        return condition;
    }

    @Override
    public Statement getUpdate() {
        return update;
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