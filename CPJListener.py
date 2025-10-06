# Generated from CPJ.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CPJParser import CPJParser
else:
    from CPJParser import CPJParser

# This class defines a complete listener for a parse tree produced by CPJParser.
class CPJListener(ParseTreeListener):

    # Enter a parse tree produced by CPJParser#program.
    def enterProgram(self, ctx:CPJParser.ProgramContext):
        pass

    # Exit a parse tree produced by CPJParser#program.
    def exitProgram(self, ctx:CPJParser.ProgramContext):
        pass


    # Enter a parse tree produced by CPJParser#statement.
    def enterStatement(self, ctx:CPJParser.StatementContext):
        pass

    # Exit a parse tree produced by CPJParser#statement.
    def exitStatement(self, ctx:CPJParser.StatementContext):
        pass


    # Enter a parse tree produced by CPJParser#typeDef.
    def enterTypeDef(self, ctx:CPJParser.TypeDefContext):
        pass

    # Exit a parse tree produced by CPJParser#typeDef.
    def exitTypeDef(self, ctx:CPJParser.TypeDefContext):
        pass


    # Enter a parse tree produced by CPJParser#typeField.
    def enterTypeField(self, ctx:CPJParser.TypeFieldContext):
        pass

    # Exit a parse tree produced by CPJParser#typeField.
    def exitTypeField(self, ctx:CPJParser.TypeFieldContext):
        pass


    # Enter a parse tree produced by CPJParser#typeRef.
    def enterTypeRef(self, ctx:CPJParser.TypeRefContext):
        pass

    # Exit a parse tree produced by CPJParser#typeRef.
    def exitTypeRef(self, ctx:CPJParser.TypeRefContext):
        pass


    # Enter a parse tree produced by CPJParser#funcDef.
    def enterFuncDef(self, ctx:CPJParser.FuncDefContext):
        pass

    # Exit a parse tree produced by CPJParser#funcDef.
    def exitFuncDef(self, ctx:CPJParser.FuncDefContext):
        pass


    # Enter a parse tree produced by CPJParser#paramList.
    def enterParamList(self, ctx:CPJParser.ParamListContext):
        pass

    # Exit a parse tree produced by CPJParser#paramList.
    def exitParamList(self, ctx:CPJParser.ParamListContext):
        pass


    # Enter a parse tree produced by CPJParser#param.
    def enterParam(self, ctx:CPJParser.ParamContext):
        pass

    # Exit a parse tree produced by CPJParser#param.
    def exitParam(self, ctx:CPJParser.ParamContext):
        pass


    # Enter a parse tree produced by CPJParser#suite.
    def enterSuite(self, ctx:CPJParser.SuiteContext):
        pass

    # Exit a parse tree produced by CPJParser#suite.
    def exitSuite(self, ctx:CPJParser.SuiteContext):
        pass


    # Enter a parse tree produced by CPJParser#block.
    def enterBlock(self, ctx:CPJParser.BlockContext):
        pass

    # Exit a parse tree produced by CPJParser#block.
    def exitBlock(self, ctx:CPJParser.BlockContext):
        pass


    # Enter a parse tree produced by CPJParser#exprStmt.
    def enterExprStmt(self, ctx:CPJParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by CPJParser#exprStmt.
    def exitExprStmt(self, ctx:CPJParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by CPJParser#expr.
    def enterExpr(self, ctx:CPJParser.ExprContext):
        pass

    # Exit a parse tree produced by CPJParser#expr.
    def exitExpr(self, ctx:CPJParser.ExprContext):
        pass


    # Enter a parse tree produced by CPJParser#primary.
    def enterPrimary(self, ctx:CPJParser.PrimaryContext):
        pass

    # Exit a parse tree produced by CPJParser#primary.
    def exitPrimary(self, ctx:CPJParser.PrimaryContext):
        pass


    # Enter a parse tree produced by CPJParser#argList.
    def enterArgList(self, ctx:CPJParser.ArgListContext):
        pass

    # Exit a parse tree produced by CPJParser#argList.
    def exitArgList(self, ctx:CPJParser.ArgListContext):
        pass


    # Enter a parse tree produced by CPJParser#guiBlock.
    def enterGuiBlock(self, ctx:CPJParser.GuiBlockContext):
        pass

    # Exit a parse tree produced by CPJParser#guiBlock.
    def exitGuiBlock(self, ctx:CPJParser.GuiBlockContext):
        pass


    # Enter a parse tree produced by CPJParser#eventHandler.
    def enterEventHandler(self, ctx:CPJParser.EventHandlerContext):
        pass

    # Exit a parse tree produced by CPJParser#eventHandler.
    def exitEventHandler(self, ctx:CPJParser.EventHandlerContext):
        pass



del CPJParser