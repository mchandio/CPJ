package cpj.frontend.java;

public interface WhileStatement extends Statement {
    Expression getCondition();

    Statement getBody();
}