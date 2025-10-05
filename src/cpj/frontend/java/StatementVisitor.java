package cpj.frontend.java;

public interface StatementVisitor {
    void visit(IfStatement stmt);

    void visit(WhileStatement stmt);

    void visit(ForStatement stmt);

    void visit(ReturnStatement stmt);
}