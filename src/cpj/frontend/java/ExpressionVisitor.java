package cpj.frontend.java;

public interface ExpressionVisitor {
    void visit(BinaryExpression expr);

    void visit(UnaryExpression expr);
}