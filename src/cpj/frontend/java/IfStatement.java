package cpj.frontend.java;

public interface IfStatement extends Statement {
    Expression getCondition();

    Statement getThenBranch();

    Statement getElseBranch();
}