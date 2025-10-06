// Generated from cpj/grammar/CPJ.g4 by ANTLR 4.13.2
package cpj.grammar.cpj.grammar;
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link CPJParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface CPJVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link CPJParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(CPJParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatement(CPJParser.StatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#eventHandler}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEventHandler(CPJParser.EventHandlerContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#typeDef}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTypeDef(CPJParser.TypeDefContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#typeFieldList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTypeFieldList(CPJParser.TypeFieldListContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#typeField}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTypeField(CPJParser.TypeFieldContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#funcDef}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFuncDef(CPJParser.FuncDefContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#paramList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParamList(CPJParser.ParamListContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#param}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParam(CPJParser.ParamContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#suite}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSuite(CPJParser.SuiteContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#simpleStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSimpleStmt(CPJParser.SimpleStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#exprStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExprStmt(CPJParser.ExprStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#guiBlock}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitGuiBlock(CPJParser.GuiBlockContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#guiBody}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitGuiBody(CPJParser.GuiBodyContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#guiProp}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitGuiProp(CPJParser.GuiPropContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#typesLine}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTypesLine(CPJParser.TypesLineContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#typesTokens}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTypesTokens(CPJParser.TypesTokensContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#typesDict}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTypesDict(CPJParser.TypesDictContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#typeEntries}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTypeEntries(CPJParser.TypeEntriesContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#typeLine}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTypeLine(CPJParser.TypeLineContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#typeEntry}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTypeEntry(CPJParser.TypeEntryContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#widgetStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWidgetStmt(CPJParser.WidgetStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#args}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArgs(CPJParser.ArgsContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#arg}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArg(CPJParser.ArgContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#exprNoNewline}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExprNoNewline(CPJParser.ExprNoNewlineContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression(CPJParser.ExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#lambdaExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLambdaExpr(CPJParser.LambdaExprContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#logicalOr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLogicalOr(CPJParser.LogicalOrContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#logicalAnd}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLogicalAnd(CPJParser.LogicalAndContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#equality}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEquality(CPJParser.EqualityContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#comparison}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitComparison(CPJParser.ComparisonContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#bitwiseOr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBitwiseOr(CPJParser.BitwiseOrContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#bitwiseXor}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBitwiseXor(CPJParser.BitwiseXorContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#bitwiseAnd}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBitwiseAnd(CPJParser.BitwiseAndContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#shift}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShift(CPJParser.ShiftContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#sum}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSum(CPJParser.SumContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#term}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTerm(CPJParser.TermContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#factor}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFactor(CPJParser.FactorContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#power}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPower(CPJParser.PowerContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAtom(CPJParser.AtomContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#argList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArgList(CPJParser.ArgListContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#callStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCallStmt(CPJParser.CallStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#dottedName}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDottedName(CPJParser.DottedNameContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#literal}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLiteral(CPJParser.LiteralContext ctx);
}