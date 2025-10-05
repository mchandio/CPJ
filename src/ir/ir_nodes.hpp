#pragma once

#include <string>
#include <vector>
#include <memory>
#include <variant>
#include <unordered_map>

namespace cpj
{
    namespace ir
    {

        // Forward declarations
        class Type;
        class Expression;
        class Statement;
        class Function;
        class Module;

        // IR Types
        class Type
        {
        public:
            enum class Kind
            {
                VOID,
                BOOL,
                INT,
                FLOAT,
                STRING,
                ARRAY,
                STRUCT,
                FUNCTION,
                CLASS
            };

            Type(Kind kind) : kind_(kind) {}
            virtual ~Type() = default;
            Kind getKind() const { return kind_; }

        private:
            Kind kind_;
        };

        // IR Expressions
        class Expression
        {
        public:
            enum class Kind
            {
                LITERAL,
                IDENTIFIER,
                BINARY_OP,
                UNARY_OP,
                CALL,
                MEMBER_ACCESS,
                ARRAY_ACCESS
            };

            Expression(Kind kind) : kind_(kind) {}
            virtual ~Expression() = default;
            Kind getKind() const { return kind_; }

            virtual std::shared_ptr<Type> getType() const = 0;

        private:
            Kind kind_;
        };

        // IR Statements
        class Statement
        {
        public:
            enum class Kind
            {
                EXPRESSION,
                DECLARATION, // Variable, class, namespace, etc. declarations
                ASSIGNMENT,
                IF,
                WHILE,
                FOR,
                RETURN,
                BLOCK,
                USING // Using statements/directives
            };

            Statement(Kind kind) : kind_(kind) {}
            virtual ~Statement() = default;
            Kind getKind() const { return kind_; }

        private:
            Kind kind_;
        };

        // IR Function
        // Forward declarations for new nodes
        class NamespaceDeclaration;
        class UsingDeclaration;
        class TemplateDeclaration;

        class Function
        {
        public:
            Function(std::string name,
                     std::shared_ptr<Type> returnType,
                     std::vector<std::pair<std::string, std::shared_ptr<Type>>> params)
                : name_(std::move(name)), returnType_(std::move(returnType)), parameters_(std::move(params)) {}

            const std::string &getName() const { return name_; }
            std::shared_ptr<Type> getReturnType() const { return returnType_; }
            const auto &getParameters() const { return parameters_; }

            void setBody(std::vector<std::shared_ptr<Statement>> body)
            {
                body_ = std::move(body);
            }

        private:
            std::string name_;
            std::shared_ptr<Type> returnType_;
            std::vector<std::pair<std::string, std::shared_ptr<Type>>> parameters_;
            std::vector<std::shared_ptr<Statement>> body_;
        };

        // Additional declarations for C++ language support
        class NamespaceDeclaration : public Declaration
        {
        public:
            std::string name;
            std::vector<std::shared_ptr<Declaration>> declarations;
        };

        class UsingDeclaration : public Declaration
        {
        public:
            std::string name;   // The alias name or namespace prefix
            std::string target; // The qualified name being used/aliased
            bool isNamespace;   // true for "using namespace", false for "using alias = target"
        };

        struct TemplateParameter
        {
            bool isTypename; // true for typename/class parameters
            std::string name;
        };

        class TemplateDeclaration : public Declaration
        {
        public:
            std::vector<TemplateParameter> parameters;
            std::shared_ptr<Declaration> declaration;
        };

        // IR Module
        class Module
        {
        public:
            explicit Module(std::string name) : name_(std::move(name)) {}

            void addFunction(std::shared_ptr<Function> function)
            {
                functions_[function->getName()] = function;
            }

            std::shared_ptr<Function> getFunction(const std::string &name) const
            {
                auto it = functions_.find(name);
                return it != functions_.end() ? it->second : nullptr;
            }

            const std::string &getName() const { return name_; }

        private:
            std::string name_;
            std::unordered_map<std::string, std::shared_ptr<Function>> functions_;
        };

        // Specific Expression Types
        class LiteralExpr : public Expression
        {
        public:
            using LiteralValue = std::variant<bool, int64_t, double, std::string>;

            LiteralExpr(LiteralValue value, std::shared_ptr<Type> type)
                : Expression(Kind::LITERAL), value_(std::move(value)), type_(std::move(type)) {}

            const LiteralValue &getValue() const { return value_; }
            std::shared_ptr<Type> getType() const override { return type_; }

        private:
            LiteralValue value_;
            std::shared_ptr<Type> type_;
        };

        class IdentifierExpr : public Expression
        {
        public:
            IdentifierExpr(std::string name)
                : Expression(Kind::IDENTIFIER), name_(std::move(name)) {}

            const std::string &getName() const { return name_; }
            std::shared_ptr<Type> getType() const override { return type_; }
            void setType(std::shared_ptr<Type> type) { type_ = std::move(type); }

        private:
            std::string name_;
            std::shared_ptr<Type> type_;
        };

        class MemberAccessExpr : public Expression
        {
        public:
            MemberAccessExpr(std::shared_ptr<Expression> object, std::string member, bool isArrow)
                : Expression(Kind::MEMBER_ACCESS), object_(std::move(object)), member_(std::move(member)), isArrow_(isArrow) {}

            std::shared_ptr<Expression> getObject() const { return object_; }
            const std::string &getMember() const { return member_; }
            bool isArrow() const { return isArrow_; }
            std::shared_ptr<Type> getType() const override { return type_; }
            void setType(std::shared_ptr<Type> type) { type_ = std::move(type); }

        private:
            std::shared_ptr<Expression> object_;
            std::string member_;
            bool isArrow_;
            std::shared_ptr<Type> type_;
        };

        class ArrayAccessExpr : public Expression
        {
        public:
            ArrayAccessExpr(std::shared_ptr<Expression> array, std::shared_ptr<Expression> index)
                : Expression(Kind::ARRAY_ACCESS), array_(std::move(array)), index_(std::move(index)) {}

            std::shared_ptr<Expression> getArray() const { return array_; }
            std::shared_ptr<Expression> getIndex() const { return index_; }
            std::shared_ptr<Type> getType() const override { return type_; }
            void setType(std::shared_ptr<Type> type) { type_ = std::move(type); }

        private:
            std::shared_ptr<Expression> array_;
            std::shared_ptr<Expression> index_;
            std::shared_ptr<Type> type_;
        };

        class CallExpr : public Expression
        {
        public:
            CallExpr(std::shared_ptr<Expression> callee)
                : Expression(Kind::CALL), callee_(std::move(callee)) {}

            std::shared_ptr<Expression> getCallee() const { return callee_; }
            std::vector<std::shared_ptr<Expression>> &getArguments() { return arguments_; }
            const std::vector<std::shared_ptr<Expression>> &getArguments() const { return arguments_; }
            std::shared_ptr<Type> getType() const override { return type_; }
            void setType(std::shared_ptr<Type> type) { type_ = std::move(type); }

        private:
            std::shared_ptr<Expression> callee_;
            std::vector<std::shared_ptr<Expression>> arguments_;
            std::shared_ptr<Type> type_;
        };

        class UnaryExpr : public Expression
        {
        public:
            UnaryExpr(UnaryOperator op, std::shared_ptr<Expression> operand, std::shared_ptr<Type> type = nullptr)
                : Expression(Kind::UNARY_OP), op_(op), operand_(std::move(operand)), type_(std::move(type)) {}

            UnaryOperator getOp() const { return op_; }
            std::shared_ptr<Expression> getOperand() const { return operand_; }
            std::shared_ptr<Type> getType() const override { return type_; }
            void setType(std::shared_ptr<Type> type) { type_ = std::move(type); }

        private:
            UnaryOperator op_;
            std::shared_ptr<Expression> operand_;
            std::shared_ptr<Type> type_;
        };

        class BinaryExpr : public Expression
        {
        public:
            BinaryExpr(BinaryOperator op, std::shared_ptr<Expression> left, std::shared_ptr<Expression> right, std::shared_ptr<Type> type = nullptr)
                : Expression(Kind::BINARY_OP), op_(op), left_(std::move(left)), right_(std::move(right)), type_(std::move(type)) {}

            BinaryOperator getOp() const { return op_; }
            std::shared_ptr<Expression> getLeft() const { return left_; }
            std::shared_ptr<Expression> getRight() const { return right_; }
            std::shared_ptr<Type> getType() const override { return type_; }
            void setType(std::shared_ptr<Type> type) { type_ = std::move(type); }

        private:
            BinaryOperator op_;
            std::shared_ptr<Expression> left_;
            std::shared_ptr<Expression> right_;
            std::shared_ptr<Type> type_;
        };

        // Operators enums
        enum class BinaryOperator
        {
            ADD,
            SUBTRACT,
            MULTIPLY,
            DIVIDE,
            MODULO,
            BITWISE_AND,
            BITWISE_OR,
            BITWISE_XOR,
            EQUAL,
            NOT_EQUAL,
            LESS,
            LESS_EQUAL,
            GREATER,
            GREATER_EQUAL,
            LOGICAL_AND,
            LOGICAL_OR
        };

        enum class UnaryOperator
        {
            PLUS,
            MINUS,
            NOT,
            BITWISE_NOT,
            PRE_INCREMENT,
            PRE_DECREMENT,
            POST_INCREMENT,
            POST_DECREMENT,
        };
        BinaryOpExpr(Op op,
                     std::shared_ptr<Expression> left,
                     std::shared_ptr<Expression> right,
                     std::shared_ptr<Type> type)
            : Expression(Kind::BINARY_OP), op_(op), left_(std::move(left)), right_(std::move(right)), type_(std::move(type)) {}

        Op getOp() const { return op_; }
        std::shared_ptr<Expression> getLeft() const { return left_; }
        std::shared_ptr<Expression> getRight() const { return right_; }
        std::shared_ptr<Type> getType() const override { return type_; }

    private:
        Op op_;
        std::shared_ptr<Expression> left_;
        std::shared_ptr<Expression> right_;
        std::shared_ptr<Type> type_;
    };

    // Specific Statement Types
    class ReturnStmt : public Statement
    {
    public:
        explicit ReturnStmt(std::shared_ptr<Expression> value)
            : Statement(Kind::RETURN), value_(std::move(value)) {}

        std::shared_ptr<Expression> getValue() const { return value_; }

    private:
        std::shared_ptr<Expression> value_;
    };

    class IfStmt : public Statement
    {
    public:
        IfStmt(std::shared_ptr<Expression> condition,
               std::vector<std::shared_ptr<Statement>> thenBody,
               std::vector<std::shared_ptr<Statement>> elseBody)
            : Statement(Kind::IF), condition_(std::move(condition)), thenBody_(std::move(thenBody)), elseBody_(std::move(elseBody)) {}

        std::shared_ptr<Expression> getCondition() const { return condition_; }
        const auto &getThenBody() const { return thenBody_; }
        const auto &getElseBody() const { return elseBody_; }

    private:
        std::shared_ptr<Expression> condition_;
        std::vector<std::shared_ptr<Statement>> thenBody_;
        std::vector<std::shared_ptr<Statement>> elseBody_;
    };

    // Loop statements
    class WhileStatement : public Statement
    {
    public:
        WhileStatement(std::shared_ptr<Expression> cond, std::shared_ptr<Statement> body)
            : Statement(Kind::WHILE), condition_(std::move(cond)), body_(std::move(body)) {}

        std::shared_ptr<Expression> getCondition() const { return condition_; }
        std::shared_ptr<Statement> getBody() const { return body_; }

    private:
        std::shared_ptr<Expression> condition_;
        std::shared_ptr<Statement> body_;
    };

    class ForStatement : public Statement
    {
    public:
        ForStatement()
            : Statement(Kind::FOR) {}

        void setInit(std::shared_ptr<Statement> init) { init_ = std::move(init); }
        void setCondition(std::shared_ptr<Expression> cond) { condition_ = std::move(cond); }
        void setIncrement(std::shared_ptr<Expression> incr) { increment_ = std::move(incr); }
        void setBody(std::shared_ptr<Statement> body) { body_ = std::move(body); }

        std::shared_ptr<Statement> getInit() const { return init_; }
        std::shared_ptr<Expression> getCondition() const { return condition_; }
        std::shared_ptr<Expression> getIncrement() const { return increment_; }
        std::shared_ptr<Statement> getBody() const { return body_; }

    private:
        std::shared_ptr<Statement> init_; // Can be Declaration or ExpressionStatement
        std::shared_ptr<Expression> condition_;
        std::shared_ptr<Expression> increment_;
        std::shared_ptr<Statement> body_;
    };

} // namespace ir
} // namespace cpj