// Generated from CPJ.g4 by ANTLR 4.13.1
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
	 * Visit a parse tree produced by the {@code LambdaExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLambdaExpr(CPJParser.LambdaExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code BitAndExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBitAndExpr(CPJParser.BitAndExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code RelationalExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRelationalExpr(CPJParser.RelationalExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code AssignmentExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssignmentExpr(CPJParser.AssignmentExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code DotExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDotExpr(CPJParser.DotExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code BitOrExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBitOrExpr(CPJParser.BitOrExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code UnaryExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUnaryExpr(CPJParser.UnaryExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code LogicalAndExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLogicalAndExpr(CPJParser.LogicalAndExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code IndexExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIndexExpr(CPJParser.IndexExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code PostfixExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPostfixExpr(CPJParser.PostfixExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code PowerExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPowerExpr(CPJParser.PowerExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code MultiplicativeExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMultiplicativeExpr(CPJParser.MultiplicativeExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code LogicalOrExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLogicalOrExpr(CPJParser.LogicalOrExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code AwaitExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAwaitExpr(CPJParser.AwaitExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code EqualityExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEqualityExpr(CPJParser.EqualityExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code AdditiveExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAdditiveExpr(CPJParser.AdditiveExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code NewExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNewExpr(CPJParser.NewExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code CastExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCastExpr(CPJParser.CastExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code PrimaryExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrimaryExpr(CPJParser.PrimaryExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code CallExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCallExpr(CPJParser.CallExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ElvisExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitElvisExpr(CPJParser.ElvisExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ShiftExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShiftExpr(CPJParser.ShiftExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code BitXorExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBitXorExpr(CPJParser.BitXorExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code TernaryExpr}
	 * labeled alternative in {@link CPJParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTernaryExpr(CPJParser.TernaryExprContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#typeDef}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTypeDef(CPJParser.TypeDefContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#typeField}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTypeField(CPJParser.TypeFieldContext ctx);
	/**
	 * Visit a parse tree produced by the {@code VoidType}
	 * labeled alternative in {@link CPJParser#typeRef}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVoidType(CPJParser.VoidTypeContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ArrayType}
	 * labeled alternative in {@link CPJParser#typeRef}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArrayType(CPJParser.ArrayTypeContext ctx);
	/**
	 * Visit a parse tree produced by the {@code WildcardType}
	 * labeled alternative in {@link CPJParser#typeRef}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWildcardType(CPJParser.WildcardTypeContext ctx);
	/**
	 * Visit a parse tree produced by the {@code GenericType}
	 * labeled alternative in {@link CPJParser#typeRef}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitGenericType(CPJParser.GenericTypeContext ctx);
	/**
	 * Visit a parse tree produced by the {@code FunctionType}
	 * labeled alternative in {@link CPJParser#typeRef}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunctionType(CPJParser.FunctionTypeContext ctx);
	/**
	 * Visit a parse tree produced by the {@code PrimitiveTypeRef}
	 * labeled alternative in {@link CPJParser#typeRef}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrimitiveTypeRef(CPJParser.PrimitiveTypeRefContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ClassType}
	 * labeled alternative in {@link CPJParser#typeRef}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitClassType(CPJParser.ClassTypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#primitiveType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrimitiveType(CPJParser.PrimitiveTypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#classDef}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitClassDef(CPJParser.ClassDefContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#interfaceDef}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInterfaceDef(CPJParser.InterfaceDefContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#enumDef}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEnumDef(CPJParser.EnumDefContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#modifier}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitModifier(CPJParser.ModifierContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#typeParameter}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTypeParameter(CPJParser.TypeParameterContext ctx);
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
	 * Visit a parse tree produced by {@link CPJParser#block}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBlock(CPJParser.BlockContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#importStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitImportStmt(CPJParser.ImportStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#importNames}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitImportNames(CPJParser.ImportNamesContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#ifStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIfStmt(CPJParser.IfStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#test}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTest(CPJParser.TestContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#forStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitForStmt(CPJParser.ForStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#asyncForStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAsyncForStmt(CPJParser.AsyncForStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#forControl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitForControl(CPJParser.ForControlContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#whileStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWhileStmt(CPJParser.WhileStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#doWhileStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDoWhileStmt(CPJParser.DoWhileStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#tryStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTryStmt(CPJParser.TryStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#catchClause}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCatchClause(CPJParser.CatchClauseContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#catchType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCatchType(CPJParser.CatchTypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#finallyBlock}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFinallyBlock(CPJParser.FinallyBlockContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#switchStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSwitchStmt(CPJParser.SwitchStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#switchBlock}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSwitchBlock(CPJParser.SwitchBlockContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#withStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWithStmt(CPJParser.WithStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#assertStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssertStmt(CPJParser.AssertStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#yieldStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitYieldStmt(CPJParser.YieldStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#globalStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitGlobalStmt(CPJParser.GlobalStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#nonlocalStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNonlocalStmt(CPJParser.NonlocalStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#returnStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReturnStmt(CPJParser.ReturnStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#throwStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitThrowStmt(CPJParser.ThrowStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#breakStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBreakStmt(CPJParser.BreakStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#continueStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitContinueStmt(CPJParser.ContinueStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#passStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPassStmt(CPJParser.PassStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#deleteStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeleteStmt(CPJParser.DeleteStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#raiseStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRaiseStmt(CPJParser.RaiseStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#exprStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExprStmt(CPJParser.ExprStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#primary}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrimary(CPJParser.PrimaryContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#argList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArgList(CPJParser.ArgListContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#guiBlock}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitGuiBlock(CPJParser.GuiBlockContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#eventHandler}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEventHandler(CPJParser.EventHandlerContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#exportStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExportStmt(CPJParser.ExportStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#exportList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExportList(CPJParser.ExportListContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#parExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParExpr(CPJParser.ParExprContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#variableDecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVariableDecl(CPJParser.VariableDeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#classBody}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitClassBody(CPJParser.ClassBodyContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#classMember}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitClassMember(CPJParser.ClassMemberContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#interfaceBody}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInterfaceBody(CPJParser.InterfaceBodyContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#interfaceMember}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInterfaceMember(CPJParser.InterfaceMemberContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#abstractMethodDecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAbstractMethodDecl(CPJParser.AbstractMethodDeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#defaultMethodDecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDefaultMethodDecl(CPJParser.DefaultMethodDeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#constructorDecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitConstructorDecl(CPJParser.ConstructorDeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#methodDecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMethodDecl(CPJParser.MethodDeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#fieldDecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFieldDecl(CPJParser.FieldDeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#enumConstants}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEnumConstants(CPJParser.EnumConstantsContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#enumConstant}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEnumConstant(CPJParser.EnumConstantContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#enumBodyDeclarations}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEnumBodyDeclarations(CPJParser.EnumBodyDeclarationsContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#forInit}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitForInit(CPJParser.ForInitContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#forUpdate}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitForUpdate(CPJParser.ForUpdateContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#creator}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCreator(CPJParser.CreatorContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#nonArrayCreator}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNonArrayCreator(CPJParser.NonArrayCreatorContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#arrayCreator}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArrayCreator(CPJParser.ArrayCreatorContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#functionLiteral}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunctionLiteral(CPJParser.FunctionLiteralContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#asyncStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAsyncStmt(CPJParser.AsyncStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#arrayLiteral}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArrayLiteral(CPJParser.ArrayLiteralContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#dictionaryLiteral}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDictionaryLiteral(CPJParser.DictionaryLiteralContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#keyValue}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitKeyValue(CPJParser.KeyValueContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#qualifiedName}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitQualifiedName(CPJParser.QualifiedNameContext ctx);
	/**
	 * Visit a parse tree produced by {@link CPJParser#variableModifier}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVariableModifier(CPJParser.VariableModifierContext ctx);
}