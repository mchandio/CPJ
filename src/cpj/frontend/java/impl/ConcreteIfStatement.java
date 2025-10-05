package cpj.frontend.java.impl;

import cpj.frontend.java.*;

public class ConcreteIfStatement implements IfStatement {
    private final Expression condition;
    private final Statement thenBranch;
    private final Statement elseBranch;

    public ConcreteIfStatement(Expression condition, Statement thenBranch, Statement elseBranch) {
        this.condition = condition;
        this.thenBranch = thenBranch;
        this.elseBranch = elseBranch;
    }

    @Override
    public Expression getCondition() {
        return condition;
    }

    @Override
    public Statement getThenBranch() {
        return thenBranch;
    }

    @Override
    public Statement getElseBranch() {
        return elseBranch;
    }

    @Override
    public void accept(StatementVisitor visitor) {
        visitor.visit(this);
    }
}