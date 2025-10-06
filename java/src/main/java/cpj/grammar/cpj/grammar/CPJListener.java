// Generated from cpj/grammar/CPJ.g4 by ANTLR 4.13.2
package cpj.grammar.cpj.grammar;
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CPJParser}.
 */
public interface CPJListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CPJParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(CPJParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(CPJParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(CPJParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(CPJParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#eventHandler}.
	 * @param ctx the parse tree
	 */
	void enterEventHandler(CPJParser.EventHandlerContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#eventHandler}.
	 * @param ctx the parse tree
	 */
	void exitEventHandler(CPJParser.EventHandlerContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#typeDef}.
	 * @param ctx the parse tree
	 */
	void enterTypeDef(CPJParser.TypeDefContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#typeDef}.
	 * @param ctx the parse tree
	 */
	void exitTypeDef(CPJParser.TypeDefContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#typeFieldList}.
	 * @param ctx the parse tree
	 */
	void enterTypeFieldList(CPJParser.TypeFieldListContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#typeFieldList}.
	 * @param ctx the parse tree
	 */
	void exitTypeFieldList(CPJParser.TypeFieldListContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#typeField}.
	 * @param ctx the parse tree
	 */
	void enterTypeField(CPJParser.TypeFieldContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#typeField}.
	 * @param ctx the parse tree
	 */
	void exitTypeField(CPJParser.TypeFieldContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#funcDef}.
	 * @param ctx the parse tree
	 */
	void enterFuncDef(CPJParser.FuncDefContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#funcDef}.
	 * @param ctx the parse tree
	 */
	void exitFuncDef(CPJParser.FuncDefContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#paramList}.
	 * @param ctx the parse tree
	 */
	void enterParamList(CPJParser.ParamListContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#paramList}.
	 * @param ctx the parse tree
	 */
	void exitParamList(CPJParser.ParamListContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#param}.
	 * @param ctx the parse tree
	 */
	void enterParam(CPJParser.ParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#param}.
	 * @param ctx the parse tree
	 */
	void exitParam(CPJParser.ParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#suite}.
	 * @param ctx the parse tree
	 */
	void enterSuite(CPJParser.SuiteContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#suite}.
	 * @param ctx the parse tree
	 */
	void exitSuite(CPJParser.SuiteContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#simpleStmt}.
	 * @param ctx the parse tree
	 */
	void enterSimpleStmt(CPJParser.SimpleStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#simpleStmt}.
	 * @param ctx the parse tree
	 */
	void exitSimpleStmt(CPJParser.SimpleStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#exprStmt}.
	 * @param ctx the parse tree
	 */
	void enterExprStmt(CPJParser.ExprStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#exprStmt}.
	 * @param ctx the parse tree
	 */
	void exitExprStmt(CPJParser.ExprStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#guiBlock}.
	 * @param ctx the parse tree
	 */
	void enterGuiBlock(CPJParser.GuiBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#guiBlock}.
	 * @param ctx the parse tree
	 */
	void exitGuiBlock(CPJParser.GuiBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#guiBody}.
	 * @param ctx the parse tree
	 */
	void enterGuiBody(CPJParser.GuiBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#guiBody}.
	 * @param ctx the parse tree
	 */
	void exitGuiBody(CPJParser.GuiBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#guiProp}.
	 * @param ctx the parse tree
	 */
	void enterGuiProp(CPJParser.GuiPropContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#guiProp}.
	 * @param ctx the parse tree
	 */
	void exitGuiProp(CPJParser.GuiPropContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#typesLine}.
	 * @param ctx the parse tree
	 */
	void enterTypesLine(CPJParser.TypesLineContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#typesLine}.
	 * @param ctx the parse tree
	 */
	void exitTypesLine(CPJParser.TypesLineContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#typesTokens}.
	 * @param ctx the parse tree
	 */
	void enterTypesTokens(CPJParser.TypesTokensContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#typesTokens}.
	 * @param ctx the parse tree
	 */
	void exitTypesTokens(CPJParser.TypesTokensContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#typesDict}.
	 * @param ctx the parse tree
	 */
	void enterTypesDict(CPJParser.TypesDictContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#typesDict}.
	 * @param ctx the parse tree
	 */
	void exitTypesDict(CPJParser.TypesDictContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#typeEntries}.
	 * @param ctx the parse tree
	 */
	void enterTypeEntries(CPJParser.TypeEntriesContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#typeEntries}.
	 * @param ctx the parse tree
	 */
	void exitTypeEntries(CPJParser.TypeEntriesContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#typeLine}.
	 * @param ctx the parse tree
	 */
	void enterTypeLine(CPJParser.TypeLineContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#typeLine}.
	 * @param ctx the parse tree
	 */
	void exitTypeLine(CPJParser.TypeLineContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#typeEntry}.
	 * @param ctx the parse tree
	 */
	void enterTypeEntry(CPJParser.TypeEntryContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#typeEntry}.
	 * @param ctx the parse tree
	 */
	void exitTypeEntry(CPJParser.TypeEntryContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#widgetStmt}.
	 * @param ctx the parse tree
	 */
	void enterWidgetStmt(CPJParser.WidgetStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#widgetStmt}.
	 * @param ctx the parse tree
	 */
	void exitWidgetStmt(CPJParser.WidgetStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#args}.
	 * @param ctx the parse tree
	 */
	void enterArgs(CPJParser.ArgsContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#args}.
	 * @param ctx the parse tree
	 */
	void exitArgs(CPJParser.ArgsContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#arg}.
	 * @param ctx the parse tree
	 */
	void enterArg(CPJParser.ArgContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#arg}.
	 * @param ctx the parse tree
	 */
	void exitArg(CPJParser.ArgContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#exprNoNewline}.
	 * @param ctx the parse tree
	 */
	void enterExprNoNewline(CPJParser.ExprNoNewlineContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#exprNoNewline}.
	 * @param ctx the parse tree
	 */
	void exitExprNoNewline(CPJParser.ExprNoNewlineContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(CPJParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(CPJParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#lambdaExpr}.
	 * @param ctx the parse tree
	 */
	void enterLambdaExpr(CPJParser.LambdaExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#lambdaExpr}.
	 * @param ctx the parse tree
	 */
	void exitLambdaExpr(CPJParser.LambdaExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#logicalOr}.
	 * @param ctx the parse tree
	 */
	void enterLogicalOr(CPJParser.LogicalOrContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#logicalOr}.
	 * @param ctx the parse tree
	 */
	void exitLogicalOr(CPJParser.LogicalOrContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#logicalAnd}.
	 * @param ctx the parse tree
	 */
	void enterLogicalAnd(CPJParser.LogicalAndContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#logicalAnd}.
	 * @param ctx the parse tree
	 */
	void exitLogicalAnd(CPJParser.LogicalAndContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#equality}.
	 * @param ctx the parse tree
	 */
	void enterEquality(CPJParser.EqualityContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#equality}.
	 * @param ctx the parse tree
	 */
	void exitEquality(CPJParser.EqualityContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#comparison}.
	 * @param ctx the parse tree
	 */
	void enterComparison(CPJParser.ComparisonContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#comparison}.
	 * @param ctx the parse tree
	 */
	void exitComparison(CPJParser.ComparisonContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#bitwiseOr}.
	 * @param ctx the parse tree
	 */
	void enterBitwiseOr(CPJParser.BitwiseOrContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#bitwiseOr}.
	 * @param ctx the parse tree
	 */
	void exitBitwiseOr(CPJParser.BitwiseOrContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#bitwiseXor}.
	 * @param ctx the parse tree
	 */
	void enterBitwiseXor(CPJParser.BitwiseXorContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#bitwiseXor}.
	 * @param ctx the parse tree
	 */
	void exitBitwiseXor(CPJParser.BitwiseXorContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#bitwiseAnd}.
	 * @param ctx the parse tree
	 */
	void enterBitwiseAnd(CPJParser.BitwiseAndContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#bitwiseAnd}.
	 * @param ctx the parse tree
	 */
	void exitBitwiseAnd(CPJParser.BitwiseAndContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#shift}.
	 * @param ctx the parse tree
	 */
	void enterShift(CPJParser.ShiftContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#shift}.
	 * @param ctx the parse tree
	 */
	void exitShift(CPJParser.ShiftContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#sum}.
	 * @param ctx the parse tree
	 */
	void enterSum(CPJParser.SumContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#sum}.
	 * @param ctx the parse tree
	 */
	void exitSum(CPJParser.SumContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(CPJParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(CPJParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(CPJParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(CPJParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#power}.
	 * @param ctx the parse tree
	 */
	void enterPower(CPJParser.PowerContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#power}.
	 * @param ctx the parse tree
	 */
	void exitPower(CPJParser.PowerContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterAtom(CPJParser.AtomContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitAtom(CPJParser.AtomContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#argList}.
	 * @param ctx the parse tree
	 */
	void enterArgList(CPJParser.ArgListContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#argList}.
	 * @param ctx the parse tree
	 */
	void exitArgList(CPJParser.ArgListContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#callStmt}.
	 * @param ctx the parse tree
	 */
	void enterCallStmt(CPJParser.CallStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#callStmt}.
	 * @param ctx the parse tree
	 */
	void exitCallStmt(CPJParser.CallStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#dottedName}.
	 * @param ctx the parse tree
	 */
	void enterDottedName(CPJParser.DottedNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#dottedName}.
	 * @param ctx the parse tree
	 */
	void exitDottedName(CPJParser.DottedNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(CPJParser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(CPJParser.LiteralContext ctx);
}