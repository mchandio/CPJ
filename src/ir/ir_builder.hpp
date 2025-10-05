#pragma once

#include "ir_nodes.hpp"
#include <stack>
#include <memory>
#include <stdexcept>

namespace cpj
{
    namespace ir
    {

        class IRBuilder
        {
        public:
            IRBuilder() : currentModule_(nullptr) {}

            // Module management
            void createModule(const std::string &name)
            {
                currentModule_ = std::make_shared<Module>(name);
            }

            std::shared_ptr<Module> getCurrentModule() const
            {
                return currentModule_;
            }

            // Function building
            void startFunction(const std::string &name,
                               std::shared_ptr<Type> returnType,
                               std::vector<std::pair<std::string, std::shared_ptr<Type>>> params)
            {
                if (!currentModule_)
                {
                    throw std::runtime_error("No active module");
                }

                currentFunction_ = std::make_shared<Function>(name, returnType, params);
                currentBlock_.clear();
            }

            void finishFunction()
            {
                if (!currentFunction_)
                {
                    throw std::runtime_error("No active function");
                }

                currentFunction_->setBody(currentBlock_);
                currentModule_->addFunction(currentFunction_);
                currentFunction_ = nullptr;
                currentBlock_.clear();
            }

            // Expression building
            std::shared_ptr<Expression> createLiteral(const typename LiteralExpr::LiteralValue &value,
                                                      std::shared_ptr<Type> type)
            {
                return std::make_shared<LiteralExpr>(value, type);
            }

            std::shared_ptr<Expression> createBinaryOp(BinaryOpExpr::Op op,
                                                       std::shared_ptr<Expression> left,
                                                       std::shared_ptr<Expression> right,
                                                       std::shared_ptr<Type> type)
            {
                return std::make_shared<BinaryOpExpr>(op, left, right, type);
            }

            // Statement building
            void createReturn(std::shared_ptr<Expression> value)
            {
                if (!currentFunction_)
                {
                    throw std::runtime_error("No active function");
                }

                auto stmt = std::make_shared<ReturnStmt>(value);
                currentBlock_.push_back(stmt);
            }

            void startIf(std::shared_ptr<Expression> condition)
            {
                ifStack_.push({condition, {}, {}});
            }

            void startElse()
            {
                if (ifStack_.empty())
                {
                    throw std::runtime_error("No active if statement");
                }
                inElseBlock_ = true;
            }

            void finishIf()
            {
                if (ifStack_.empty())
                {
                    throw std::runtime_error("No active if statement");
                }

                auto [condition, thenBody, elseBody] = ifStack_.top();
                ifStack_.pop();

                auto stmt = std::make_shared<IfStmt>(condition, thenBody, elseBody);
                currentBlock_.push_back(stmt);
                inElseBlock_ = false;
            }

            void addStatement(std::shared_ptr<Statement> stmt)
            {
                if (!currentFunction_)
                {
                    throw std::runtime_error("No active function");
                }

                if (!ifStack_.empty())
                {
                    auto &current = ifStack_.top();
                    if (inElseBlock_)
                    {
                        std::get<2>(current).push_back(stmt);
                    }
                    else
                    {
                        std::get<1>(current).push_back(stmt);
                    }
                }
                else
                {
                    currentBlock_.push_back(stmt);
                }
            }

        private:
            std::shared_ptr<Module> currentModule_;
            std::shared_ptr<Function> currentFunction_;
            std::vector<std::shared_ptr<Statement>> currentBlock_;
            std::stack<std::tuple<std::shared_ptr<Expression>,
                                  std::vector<std::shared_ptr<Statement>>,
                                  std::vector<std::shared_ptr<Statement>>>>
                ifStack_;
            bool inElseBlock_ = false;
        };

    } // namespace ir
} // namespace cpj