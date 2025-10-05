# Generated from grammar/CPJ.g4 by ANTLR 4.13.2
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


    # Enter a parse tree produced by CPJParser#suite.
    def enterSuite(self, ctx:CPJParser.SuiteContext):
        pass

    # Exit a parse tree produced by CPJParser#suite.
    def exitSuite(self, ctx:CPJParser.SuiteContext):
        pass


    # Enter a parse tree produced by CPJParser#simpleStmt.
    def enterSimpleStmt(self, ctx:CPJParser.SimpleStmtContext):
        pass

    # Exit a parse tree produced by CPJParser#simpleStmt.
    def exitSimpleStmt(self, ctx:CPJParser.SimpleStmtContext):
        pass


    # Enter a parse tree produced by CPJParser#exprStmt.
    def enterExprStmt(self, ctx:CPJParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by CPJParser#exprStmt.
    def exitExprStmt(self, ctx:CPJParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by CPJParser#guiBlock.
    def enterGuiBlock(self, ctx:CPJParser.GuiBlockContext):
        pass

    # Exit a parse tree produced by CPJParser#guiBlock.
    def exitGuiBlock(self, ctx:CPJParser.GuiBlockContext):
        pass


    # Enter a parse tree produced by CPJParser#guiBody.
    def enterGuiBody(self, ctx:CPJParser.GuiBodyContext):
        pass

    # Exit a parse tree produced by CPJParser#guiBody.
    def exitGuiBody(self, ctx:CPJParser.GuiBodyContext):
        pass


    # Enter a parse tree produced by CPJParser#guiProp.
    def enterGuiProp(self, ctx:CPJParser.GuiPropContext):
        pass

    # Exit a parse tree produced by CPJParser#guiProp.
    def exitGuiProp(self, ctx:CPJParser.GuiPropContext):
        pass


    # Enter a parse tree produced by CPJParser#typesLine.
    def enterTypesLine(self, ctx:CPJParser.TypesLineContext):
        pass

    # Exit a parse tree produced by CPJParser#typesLine.
    def exitTypesLine(self, ctx:CPJParser.TypesLineContext):
        pass


    # Enter a parse tree produced by CPJParser#typesTokens.
    def enterTypesTokens(self, ctx:CPJParser.TypesTokensContext):
        pass

    # Exit a parse tree produced by CPJParser#typesTokens.
    def exitTypesTokens(self, ctx:CPJParser.TypesTokensContext):
        pass


    # Enter a parse tree produced by CPJParser#typesDict.
    def enterTypesDict(self, ctx:CPJParser.TypesDictContext):
        pass

    # Exit a parse tree produced by CPJParser#typesDict.
    def exitTypesDict(self, ctx:CPJParser.TypesDictContext):
        pass


    # Enter a parse tree produced by CPJParser#typeEntries.
    def enterTypeEntries(self, ctx:CPJParser.TypeEntriesContext):
        pass

    # Exit a parse tree produced by CPJParser#typeEntries.
    def exitTypeEntries(self, ctx:CPJParser.TypeEntriesContext):
        pass


    # Enter a parse tree produced by CPJParser#typeLine.
    def enterTypeLine(self, ctx:CPJParser.TypeLineContext):
        pass

    # Exit a parse tree produced by CPJParser#typeLine.
    def exitTypeLine(self, ctx:CPJParser.TypeLineContext):
        pass


    # Enter a parse tree produced by CPJParser#typeEntry.
    def enterTypeEntry(self, ctx:CPJParser.TypeEntryContext):
        pass

    # Exit a parse tree produced by CPJParser#typeEntry.
    def exitTypeEntry(self, ctx:CPJParser.TypeEntryContext):
        pass


    # Enter a parse tree produced by CPJParser#widgetStmt.
    def enterWidgetStmt(self, ctx:CPJParser.WidgetStmtContext):
        pass

    # Exit a parse tree produced by CPJParser#widgetStmt.
    def exitWidgetStmt(self, ctx:CPJParser.WidgetStmtContext):
        pass


    # Enter a parse tree produced by CPJParser#args.
    def enterArgs(self, ctx:CPJParser.ArgsContext):
        pass

    # Exit a parse tree produced by CPJParser#args.
    def exitArgs(self, ctx:CPJParser.ArgsContext):
        pass


    # Enter a parse tree produced by CPJParser#arg.
    def enterArg(self, ctx:CPJParser.ArgContext):
        pass

    # Exit a parse tree produced by CPJParser#arg.
    def exitArg(self, ctx:CPJParser.ArgContext):
        pass


    # Enter a parse tree produced by CPJParser#exprNoNewline.
    def enterExprNoNewline(self, ctx:CPJParser.ExprNoNewlineContext):
        pass

    # Exit a parse tree produced by CPJParser#exprNoNewline.
    def exitExprNoNewline(self, ctx:CPJParser.ExprNoNewlineContext):
        pass


    # Enter a parse tree produced by CPJParser#expression.
    def enterExpression(self, ctx:CPJParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CPJParser#expression.
    def exitExpression(self, ctx:CPJParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CPJParser#lambdaExpr.
    def enterLambdaExpr(self, ctx:CPJParser.LambdaExprContext):
        pass

    # Exit a parse tree produced by CPJParser#lambdaExpr.
    def exitLambdaExpr(self, ctx:CPJParser.LambdaExprContext):
        pass


    # Enter a parse tree produced by CPJParser#logicalOr.
    def enterLogicalOr(self, ctx:CPJParser.LogicalOrContext):
        pass

    # Exit a parse tree produced by CPJParser#logicalOr.
    def exitLogicalOr(self, ctx:CPJParser.LogicalOrContext):
        pass


    # Enter a parse tree produced by CPJParser#logicalAnd.
    def enterLogicalAnd(self, ctx:CPJParser.LogicalAndContext):
        pass

    # Exit a parse tree produced by CPJParser#logicalAnd.
    def exitLogicalAnd(self, ctx:CPJParser.LogicalAndContext):
        pass


    # Enter a parse tree produced by CPJParser#equality.
    def enterEquality(self, ctx:CPJParser.EqualityContext):
        pass

    # Exit a parse tree produced by CPJParser#equality.
    def exitEquality(self, ctx:CPJParser.EqualityContext):
        pass


    # Enter a parse tree produced by CPJParser#comparison.
    def enterComparison(self, ctx:CPJParser.ComparisonContext):
        pass

    # Exit a parse tree produced by CPJParser#comparison.
    def exitComparison(self, ctx:CPJParser.ComparisonContext):
        pass


    # Enter a parse tree produced by CPJParser#bitwiseOr.
    def enterBitwiseOr(self, ctx:CPJParser.BitwiseOrContext):
        pass

    # Exit a parse tree produced by CPJParser#bitwiseOr.
    def exitBitwiseOr(self, ctx:CPJParser.BitwiseOrContext):
        pass


    # Enter a parse tree produced by CPJParser#bitwiseXor.
    def enterBitwiseXor(self, ctx:CPJParser.BitwiseXorContext):
        pass

    # Exit a parse tree produced by CPJParser#bitwiseXor.
    def exitBitwiseXor(self, ctx:CPJParser.BitwiseXorContext):
        pass


    # Enter a parse tree produced by CPJParser#bitwiseAnd.
    def enterBitwiseAnd(self, ctx:CPJParser.BitwiseAndContext):
        pass

    # Exit a parse tree produced by CPJParser#bitwiseAnd.
    def exitBitwiseAnd(self, ctx:CPJParser.BitwiseAndContext):
        pass


    # Enter a parse tree produced by CPJParser#shift.
    def enterShift(self, ctx:CPJParser.ShiftContext):
        pass

    # Exit a parse tree produced by CPJParser#shift.
    def exitShift(self, ctx:CPJParser.ShiftContext):
        pass


    # Enter a parse tree produced by CPJParser#sum.
    def enterSum(self, ctx:CPJParser.SumContext):
        pass

    # Exit a parse tree produced by CPJParser#sum.
    def exitSum(self, ctx:CPJParser.SumContext):
        pass


    # Enter a parse tree produced by CPJParser#term.
    def enterTerm(self, ctx:CPJParser.TermContext):
        pass

    # Exit a parse tree produced by CPJParser#term.
    def exitTerm(self, ctx:CPJParser.TermContext):
        pass


    # Enter a parse tree produced by CPJParser#factor.
    def enterFactor(self, ctx:CPJParser.FactorContext):
        pass

    # Exit a parse tree produced by CPJParser#factor.
    def exitFactor(self, ctx:CPJParser.FactorContext):
        pass


    # Enter a parse tree produced by CPJParser#power.
    def enterPower(self, ctx:CPJParser.PowerContext):
        pass

    # Exit a parse tree produced by CPJParser#power.
    def exitPower(self, ctx:CPJParser.PowerContext):
        pass


    # Enter a parse tree produced by CPJParser#atom.
    def enterAtom(self, ctx:CPJParser.AtomContext):
        pass

    # Exit a parse tree produced by CPJParser#atom.
    def exitAtom(self, ctx:CPJParser.AtomContext):
        pass


    # Enter a parse tree produced by CPJParser#argList.
    def enterArgList(self, ctx:CPJParser.ArgListContext):
        pass

    # Exit a parse tree produced by CPJParser#argList.
    def exitArgList(self, ctx:CPJParser.ArgListContext):
        pass


    # Enter a parse tree produced by CPJParser#callStmt.
    def enterCallStmt(self, ctx:CPJParser.CallStmtContext):
        pass

    # Exit a parse tree produced by CPJParser#callStmt.
    def exitCallStmt(self, ctx:CPJParser.CallStmtContext):
        pass


    # Enter a parse tree produced by CPJParser#dottedName.
    def enterDottedName(self, ctx:CPJParser.DottedNameContext):
        pass

    # Exit a parse tree produced by CPJParser#dottedName.
    def exitDottedName(self, ctx:CPJParser.DottedNameContext):
        pass


    # Enter a parse tree produced by CPJParser#literal.
    def enterLiteral(self, ctx:CPJParser.LiteralContext):
        pass

    # Exit a parse tree produced by CPJParser#literal.
    def exitLiteral(self, ctx:CPJParser.LiteralContext):
        pass



del CPJParser