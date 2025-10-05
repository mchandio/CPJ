package cpj.frontend.java;

public interface ForStatement extends Statement {
    Statement getInitialization();

    Expression getCondition();

    Statement getUpdate();

    Statement getBody();
}