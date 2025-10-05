package cpj.frontend.java;

public interface Statement {
    void accept(StatementVisitor visitor);
}