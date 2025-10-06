// Generated from CPJ.g4 by ANTLR 4.13.1
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
	 * Enter a parse tree produced by the {@code LambdaExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterLambdaExpr(CPJParser.LambdaExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LambdaExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitLambdaExpr(CPJParser.LambdaExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code BitAndExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterBitAndExpr(CPJParser.BitAndExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code BitAndExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitBitAndExpr(CPJParser.BitAndExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code RelationalExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterRelationalExpr(CPJParser.RelationalExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code RelationalExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitRelationalExpr(CPJParser.RelationalExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AssignmentExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentExpr(CPJParser.AssignmentExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AssignmentExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentExpr(CPJParser.AssignmentExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code DotExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterDotExpr(CPJParser.DotExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code DotExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitDotExpr(CPJParser.DotExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code BitOrExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterBitOrExpr(CPJParser.BitOrExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code BitOrExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitBitOrExpr(CPJParser.BitOrExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code UnaryExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterUnaryExpr(CPJParser.UnaryExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code UnaryExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitUnaryExpr(CPJParser.UnaryExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LogicalAndExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterLogicalAndExpr(CPJParser.LogicalAndExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LogicalAndExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitLogicalAndExpr(CPJParser.LogicalAndExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code IndexExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterIndexExpr(CPJParser.IndexExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code IndexExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitIndexExpr(CPJParser.IndexExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PostfixExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterPostfixExpr(CPJParser.PostfixExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PostfixExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitPostfixExpr(CPJParser.PostfixExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PowerExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterPowerExpr(CPJParser.PowerExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PowerExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitPowerExpr(CPJParser.PowerExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MultiplicativeExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterMultiplicativeExpr(CPJParser.MultiplicativeExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MultiplicativeExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitMultiplicativeExpr(CPJParser.MultiplicativeExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LogicalOrExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterLogicalOrExpr(CPJParser.LogicalOrExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LogicalOrExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitLogicalOrExpr(CPJParser.LogicalOrExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AwaitExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAwaitExpr(CPJParser.AwaitExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AwaitExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAwaitExpr(CPJParser.AwaitExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code EqualityExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterEqualityExpr(CPJParser.EqualityExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code EqualityExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitEqualityExpr(CPJParser.EqualityExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AdditiveExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAdditiveExpr(CPJParser.AdditiveExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AdditiveExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAdditiveExpr(CPJParser.AdditiveExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code NewExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterNewExpr(CPJParser.NewExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code NewExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitNewExpr(CPJParser.NewExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code CastExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterCastExpr(CPJParser.CastExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CastExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitCastExpr(CPJParser.CastExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PrimaryExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterPrimaryExpr(CPJParser.PrimaryExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PrimaryExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitPrimaryExpr(CPJParser.PrimaryExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code CallExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterCallExpr(CPJParser.CallExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CallExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitCallExpr(CPJParser.CallExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ElvisExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterElvisExpr(CPJParser.ElvisExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ElvisExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitElvisExpr(CPJParser.ElvisExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ShiftExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterShiftExpr(CPJParser.ShiftExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ShiftExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitShiftExpr(CPJParser.ShiftExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code BitXorExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterBitXorExpr(CPJParser.BitXorExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code BitXorExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitBitXorExpr(CPJParser.BitXorExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code TernaryExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterTernaryExpr(CPJParser.TernaryExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code TernaryExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitTernaryExpr(CPJParser.TernaryExprContext ctx);
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
	 * Enter a parse tree produced by the {@code VoidType}
	 * labeled alternative in {@link CPJParser#typeRef}.
	 * @param ctx the parse tree
	 */
	void enterVoidType(CPJParser.VoidTypeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code VoidType}
	 * labeled alternative in {@link CPJParser#typeRef}.
	 * @param ctx the parse tree
	 */
	void exitVoidType(CPJParser.VoidTypeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ArrayType}
	 * labeled alternative in {@link CPJParser#typeRef}.
	 * @param ctx the parse tree
	 */
	void enterArrayType(CPJParser.ArrayTypeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ArrayType}
	 * labeled alternative in {@link CPJParser#typeRef}.
	 * @param ctx the parse tree
	 */
	void exitArrayType(CPJParser.ArrayTypeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code WildcardType}
	 * labeled alternative in {@link CPJParser#typeRef}.
	 * @param ctx the parse tree
	 */
	void enterWildcardType(CPJParser.WildcardTypeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code WildcardType}
	 * labeled alternative in {@link CPJParser#typeRef}.
	 * @param ctx the parse tree
	 */
	void exitWildcardType(CPJParser.WildcardTypeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code GenericType}
	 * labeled alternative in {@link CPJParser#typeRef}.
	 * @param ctx the parse tree
	 */
	void enterGenericType(CPJParser.GenericTypeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code GenericType}
	 * labeled alternative in {@link CPJParser#typeRef}.
	 * @param ctx the parse tree
	 */
	void exitGenericType(CPJParser.GenericTypeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code FunctionType}
	 * labeled alternative in {@link CPJParser#typeRef}.
	 * @param ctx the parse tree
	 */
	void enterFunctionType(CPJParser.FunctionTypeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code FunctionType}
	 * labeled alternative in {@link CPJParser#typeRef}.
	 * @param ctx the parse tree
	 */
	void exitFunctionType(CPJParser.FunctionTypeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PrimitiveTypeRef}
	 * labeled alternative in {@link CPJParser#typeRef}.
	 * @param ctx the parse tree
	 */
	void enterPrimitiveTypeRef(CPJParser.PrimitiveTypeRefContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PrimitiveTypeRef}
	 * labeled alternative in {@link CPJParser#typeRef}.
	 * @param ctx the parse tree
	 */
	void exitPrimitiveTypeRef(CPJParser.PrimitiveTypeRefContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ClassType}
	 * labeled alternative in {@link CPJParser#typeRef}.
	 * @param ctx the parse tree
	 */
	void enterClassType(CPJParser.ClassTypeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ClassType}
	 * labeled alternative in {@link CPJParser#typeRef}.
	 * @param ctx the parse tree
	 */
	void exitClassType(CPJParser.ClassTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#primitiveType}.
	 * @param ctx the parse tree
	 */
	void enterPrimitiveType(CPJParser.PrimitiveTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#primitiveType}.
	 * @param ctx the parse tree
	 */
	void exitPrimitiveType(CPJParser.PrimitiveTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#classDef}.
	 * @param ctx the parse tree
	 */
	void enterClassDef(CPJParser.ClassDefContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#classDef}.
	 * @param ctx the parse tree
	 */
	void exitClassDef(CPJParser.ClassDefContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#interfaceDef}.
	 * @param ctx the parse tree
	 */
	void enterInterfaceDef(CPJParser.InterfaceDefContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#interfaceDef}.
	 * @param ctx the parse tree
	 */
	void exitInterfaceDef(CPJParser.InterfaceDefContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#enumDef}.
	 * @param ctx the parse tree
	 */
	void enterEnumDef(CPJParser.EnumDefContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#enumDef}.
	 * @param ctx the parse tree
	 */
	void exitEnumDef(CPJParser.EnumDefContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#modifier}.
	 * @param ctx the parse tree
	 */
	void enterModifier(CPJParser.ModifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#modifier}.
	 * @param ctx the parse tree
	 */
	void exitModifier(CPJParser.ModifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#typeParameter}.
	 * @param ctx the parse tree
	 */
	void enterTypeParameter(CPJParser.TypeParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#typeParameter}.
	 * @param ctx the parse tree
	 */
	void exitTypeParameter(CPJParser.TypeParameterContext ctx);
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
	 * Enter a parse tree produced by {@link CPJParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(CPJParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(CPJParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#importStmt}.
	 * @param ctx the parse tree
	 */
	void enterImportStmt(CPJParser.ImportStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#importStmt}.
	 * @param ctx the parse tree
	 */
	void exitImportStmt(CPJParser.ImportStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#importNames}.
	 * @param ctx the parse tree
	 */
	void enterImportNames(CPJParser.ImportNamesContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#importNames}.
	 * @param ctx the parse tree
	 */
	void exitImportNames(CPJParser.ImportNamesContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void enterIfStmt(CPJParser.IfStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void exitIfStmt(CPJParser.IfStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#test}.
	 * @param ctx the parse tree
	 */
	void enterTest(CPJParser.TestContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#test}.
	 * @param ctx the parse tree
	 */
	void exitTest(CPJParser.TestContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#forStmt}.
	 * @param ctx the parse tree
	 */
	void enterForStmt(CPJParser.ForStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#forStmt}.
	 * @param ctx the parse tree
	 */
	void exitForStmt(CPJParser.ForStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#asyncForStmt}.
	 * @param ctx the parse tree
	 */
	void enterAsyncForStmt(CPJParser.AsyncForStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#asyncForStmt}.
	 * @param ctx the parse tree
	 */
	void exitAsyncForStmt(CPJParser.AsyncForStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#forControl}.
	 * @param ctx the parse tree
	 */
	void enterForControl(CPJParser.ForControlContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#forControl}.
	 * @param ctx the parse tree
	 */
	void exitForControl(CPJParser.ForControlContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#whileStmt}.
	 * @param ctx the parse tree
	 */
	void enterWhileStmt(CPJParser.WhileStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#whileStmt}.
	 * @param ctx the parse tree
	 */
	void exitWhileStmt(CPJParser.WhileStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#doWhileStmt}.
	 * @param ctx the parse tree
	 */
	void enterDoWhileStmt(CPJParser.DoWhileStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#doWhileStmt}.
	 * @param ctx the parse tree
	 */
	void exitDoWhileStmt(CPJParser.DoWhileStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#tryStmt}.
	 * @param ctx the parse tree
	 */
	void enterTryStmt(CPJParser.TryStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#tryStmt}.
	 * @param ctx the parse tree
	 */
	void exitTryStmt(CPJParser.TryStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#catchClause}.
	 * @param ctx the parse tree
	 */
	void enterCatchClause(CPJParser.CatchClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#catchClause}.
	 * @param ctx the parse tree
	 */
	void exitCatchClause(CPJParser.CatchClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#catchType}.
	 * @param ctx the parse tree
	 */
	void enterCatchType(CPJParser.CatchTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#catchType}.
	 * @param ctx the parse tree
	 */
	void exitCatchType(CPJParser.CatchTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#finallyBlock}.
	 * @param ctx the parse tree
	 */
	void enterFinallyBlock(CPJParser.FinallyBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#finallyBlock}.
	 * @param ctx the parse tree
	 */
	void exitFinallyBlock(CPJParser.FinallyBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#switchStmt}.
	 * @param ctx the parse tree
	 */
	void enterSwitchStmt(CPJParser.SwitchStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#switchStmt}.
	 * @param ctx the parse tree
	 */
	void exitSwitchStmt(CPJParser.SwitchStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#switchBlock}.
	 * @param ctx the parse tree
	 */
	void enterSwitchBlock(CPJParser.SwitchBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#switchBlock}.
	 * @param ctx the parse tree
	 */
	void exitSwitchBlock(CPJParser.SwitchBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#withStmt}.
	 * @param ctx the parse tree
	 */
	void enterWithStmt(CPJParser.WithStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#withStmt}.
	 * @param ctx the parse tree
	 */
	void exitWithStmt(CPJParser.WithStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#assertStmt}.
	 * @param ctx the parse tree
	 */
	void enterAssertStmt(CPJParser.AssertStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#assertStmt}.
	 * @param ctx the parse tree
	 */
	void exitAssertStmt(CPJParser.AssertStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#yieldStmt}.
	 * @param ctx the parse tree
	 */
	void enterYieldStmt(CPJParser.YieldStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#yieldStmt}.
	 * @param ctx the parse tree
	 */
	void exitYieldStmt(CPJParser.YieldStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#globalStmt}.
	 * @param ctx the parse tree
	 */
	void enterGlobalStmt(CPJParser.GlobalStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#globalStmt}.
	 * @param ctx the parse tree
	 */
	void exitGlobalStmt(CPJParser.GlobalStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#nonlocalStmt}.
	 * @param ctx the parse tree
	 */
	void enterNonlocalStmt(CPJParser.NonlocalStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#nonlocalStmt}.
	 * @param ctx the parse tree
	 */
	void exitNonlocalStmt(CPJParser.NonlocalStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#returnStmt}.
	 * @param ctx the parse tree
	 */
	void enterReturnStmt(CPJParser.ReturnStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#returnStmt}.
	 * @param ctx the parse tree
	 */
	void exitReturnStmt(CPJParser.ReturnStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#throwStmt}.
	 * @param ctx the parse tree
	 */
	void enterThrowStmt(CPJParser.ThrowStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#throwStmt}.
	 * @param ctx the parse tree
	 */
	void exitThrowStmt(CPJParser.ThrowStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#breakStmt}.
	 * @param ctx the parse tree
	 */
	void enterBreakStmt(CPJParser.BreakStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#breakStmt}.
	 * @param ctx the parse tree
	 */
	void exitBreakStmt(CPJParser.BreakStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#continueStmt}.
	 * @param ctx the parse tree
	 */
	void enterContinueStmt(CPJParser.ContinueStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#continueStmt}.
	 * @param ctx the parse tree
	 */
	void exitContinueStmt(CPJParser.ContinueStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#passStmt}.
	 * @param ctx the parse tree
	 */
	void enterPassStmt(CPJParser.PassStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#passStmt}.
	 * @param ctx the parse tree
	 */
	void exitPassStmt(CPJParser.PassStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#deleteStmt}.
	 * @param ctx the parse tree
	 */
	void enterDeleteStmt(CPJParser.DeleteStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#deleteStmt}.
	 * @param ctx the parse tree
	 */
	void exitDeleteStmt(CPJParser.DeleteStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#raiseStmt}.
	 * @param ctx the parse tree
	 */
	void enterRaiseStmt(CPJParser.RaiseStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#raiseStmt}.
	 * @param ctx the parse tree
	 */
	void exitRaiseStmt(CPJParser.RaiseStmtContext ctx);
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
	 * Enter a parse tree produced by {@link CPJParser#primary}.
	 * @param ctx the parse tree
	 */
	void enterPrimary(CPJParser.PrimaryContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#primary}.
	 * @param ctx the parse tree
	 */
	void exitPrimary(CPJParser.PrimaryContext ctx);
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
	 * Enter a parse tree produced by {@link CPJParser#exportStmt}.
	 * @param ctx the parse tree
	 */
	void enterExportStmt(CPJParser.ExportStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#exportStmt}.
	 * @param ctx the parse tree
	 */
	void exitExportStmt(CPJParser.ExportStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#exportList}.
	 * @param ctx the parse tree
	 */
	void enterExportList(CPJParser.ExportListContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#exportList}.
	 * @param ctx the parse tree
	 */
	void exitExportList(CPJParser.ExportListContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#parExpr}.
	 * @param ctx the parse tree
	 */
	void enterParExpr(CPJParser.ParExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#parExpr}.
	 * @param ctx the parse tree
	 */
	void exitParExpr(CPJParser.ParExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#variableDecl}.
	 * @param ctx the parse tree
	 */
	void enterVariableDecl(CPJParser.VariableDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#variableDecl}.
	 * @param ctx the parse tree
	 */
	void exitVariableDecl(CPJParser.VariableDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#classBody}.
	 * @param ctx the parse tree
	 */
	void enterClassBody(CPJParser.ClassBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#classBody}.
	 * @param ctx the parse tree
	 */
	void exitClassBody(CPJParser.ClassBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#classMember}.
	 * @param ctx the parse tree
	 */
	void enterClassMember(CPJParser.ClassMemberContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#classMember}.
	 * @param ctx the parse tree
	 */
	void exitClassMember(CPJParser.ClassMemberContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#interfaceBody}.
	 * @param ctx the parse tree
	 */
	void enterInterfaceBody(CPJParser.InterfaceBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#interfaceBody}.
	 * @param ctx the parse tree
	 */
	void exitInterfaceBody(CPJParser.InterfaceBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#interfaceMember}.
	 * @param ctx the parse tree
	 */
	void enterInterfaceMember(CPJParser.InterfaceMemberContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#interfaceMember}.
	 * @param ctx the parse tree
	 */
	void exitInterfaceMember(CPJParser.InterfaceMemberContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#abstractMethodDecl}.
	 * @param ctx the parse tree
	 */
	void enterAbstractMethodDecl(CPJParser.AbstractMethodDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#abstractMethodDecl}.
	 * @param ctx the parse tree
	 */
	void exitAbstractMethodDecl(CPJParser.AbstractMethodDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#defaultMethodDecl}.
	 * @param ctx the parse tree
	 */
	void enterDefaultMethodDecl(CPJParser.DefaultMethodDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#defaultMethodDecl}.
	 * @param ctx the parse tree
	 */
	void exitDefaultMethodDecl(CPJParser.DefaultMethodDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#constructorDecl}.
	 * @param ctx the parse tree
	 */
	void enterConstructorDecl(CPJParser.ConstructorDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#constructorDecl}.
	 * @param ctx the parse tree
	 */
	void exitConstructorDecl(CPJParser.ConstructorDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#methodDecl}.
	 * @param ctx the parse tree
	 */
	void enterMethodDecl(CPJParser.MethodDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#methodDecl}.
	 * @param ctx the parse tree
	 */
	void exitMethodDecl(CPJParser.MethodDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#fieldDecl}.
	 * @param ctx the parse tree
	 */
	void enterFieldDecl(CPJParser.FieldDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#fieldDecl}.
	 * @param ctx the parse tree
	 */
	void exitFieldDecl(CPJParser.FieldDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#enumConstants}.
	 * @param ctx the parse tree
	 */
	void enterEnumConstants(CPJParser.EnumConstantsContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#enumConstants}.
	 * @param ctx the parse tree
	 */
	void exitEnumConstants(CPJParser.EnumConstantsContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#enumConstant}.
	 * @param ctx the parse tree
	 */
	void enterEnumConstant(CPJParser.EnumConstantContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#enumConstant}.
	 * @param ctx the parse tree
	 */
	void exitEnumConstant(CPJParser.EnumConstantContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#enumBodyDeclarations}.
	 * @param ctx the parse tree
	 */
	void enterEnumBodyDeclarations(CPJParser.EnumBodyDeclarationsContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#enumBodyDeclarations}.
	 * @param ctx the parse tree
	 */
	void exitEnumBodyDeclarations(CPJParser.EnumBodyDeclarationsContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#forInit}.
	 * @param ctx the parse tree
	 */
	void enterForInit(CPJParser.ForInitContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#forInit}.
	 * @param ctx the parse tree
	 */
	void exitForInit(CPJParser.ForInitContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#forUpdate}.
	 * @param ctx the parse tree
	 */
	void enterForUpdate(CPJParser.ForUpdateContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#forUpdate}.
	 * @param ctx the parse tree
	 */
	void exitForUpdate(CPJParser.ForUpdateContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#creator}.
	 * @param ctx the parse tree
	 */
	void enterCreator(CPJParser.CreatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#creator}.
	 * @param ctx the parse tree
	 */
	void exitCreator(CPJParser.CreatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#nonArrayCreator}.
	 * @param ctx the parse tree
	 */
	void enterNonArrayCreator(CPJParser.NonArrayCreatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#nonArrayCreator}.
	 * @param ctx the parse tree
	 */
	void exitNonArrayCreator(CPJParser.NonArrayCreatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#arrayCreator}.
	 * @param ctx the parse tree
	 */
	void enterArrayCreator(CPJParser.ArrayCreatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#arrayCreator}.
	 * @param ctx the parse tree
	 */
	void exitArrayCreator(CPJParser.ArrayCreatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#functionLiteral}.
	 * @param ctx the parse tree
	 */
	void enterFunctionLiteral(CPJParser.FunctionLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#functionLiteral}.
	 * @param ctx the parse tree
	 */
	void exitFunctionLiteral(CPJParser.FunctionLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#asyncStmt}.
	 * @param ctx the parse tree
	 */
	void enterAsyncStmt(CPJParser.AsyncStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#asyncStmt}.
	 * @param ctx the parse tree
	 */
	void exitAsyncStmt(CPJParser.AsyncStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#arrayLiteral}.
	 * @param ctx the parse tree
	 */
	void enterArrayLiteral(CPJParser.ArrayLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#arrayLiteral}.
	 * @param ctx the parse tree
	 */
	void exitArrayLiteral(CPJParser.ArrayLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#dictionaryLiteral}.
	 * @param ctx the parse tree
	 */
	void enterDictionaryLiteral(CPJParser.DictionaryLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#dictionaryLiteral}.
	 * @param ctx the parse tree
	 */
	void exitDictionaryLiteral(CPJParser.DictionaryLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#keyValue}.
	 * @param ctx the parse tree
	 */
	void enterKeyValue(CPJParser.KeyValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#keyValue}.
	 * @param ctx the parse tree
	 */
	void exitKeyValue(CPJParser.KeyValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#qualifiedName}.
	 * @param ctx the parse tree
	 */
	void enterQualifiedName(CPJParser.QualifiedNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#qualifiedName}.
	 * @param ctx the parse tree
	 */
	void exitQualifiedName(CPJParser.QualifiedNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CPJParser#variableModifier}.
	 * @param ctx the parse tree
	 */
	void enterVariableModifier(CPJParser.VariableModifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link CPJParser#variableModifier}.
	 * @param ctx the parse tree
	 */
	void exitVariableModifier(CPJParser.VariableModifierContext ctx);
}