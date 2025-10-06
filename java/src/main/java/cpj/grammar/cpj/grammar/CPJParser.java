// Generated from cpj/grammar/CPJ.g4 by ANTLR 4.13.2
package cpj.grammar.cpj.grammar;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class CPJParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, TYPE_KW=4, ARROW=5, ON=6, FROM=7, DO=8, NEWLINE=9, 
		INDENT=10, DEDENT=11, LPAREN=12, RPAREN=13, COLON=14, COMMA=15, LBRACE=16, 
		RBRACE=17, DOT=18, PLUS=19, MINUS=20, STAR=21, DIV=22, MOD=23, POW=24, 
		TILDE=25, LT=26, GT=27, LE=28, GE=29, EQ=30, NEQ=31, LSHIFT=32, RSHIFT=33, 
		BITOR=34, BITXOR=35, BITAND=36, DEF=37, GUI_CAP=38, GUI_KW=39, TYPES_KW=40, 
		ADD_TEXT=41, ADD_BTN=42, ADD_CHECK=43, ADD_SLIDER=44, OR=45, AND=46, IN=47, 
		IS=48, TRUE=49, FALSE=50, NULL=51, Float=52, Integer=53, StringLiteral=54, 
		Identifier=55, COMMENT=56, WS=57;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_eventHandler = 2, RULE_typeDef = 3, 
		RULE_typeFieldList = 4, RULE_typeField = 5, RULE_funcDef = 6, RULE_paramList = 7, 
		RULE_param = 8, RULE_suite = 9, RULE_simpleStmt = 10, RULE_exprStmt = 11, 
		RULE_guiBlock = 12, RULE_guiBody = 13, RULE_guiProp = 14, RULE_typesLine = 15, 
		RULE_typesTokens = 16, RULE_typesDict = 17, RULE_typeEntries = 18, RULE_typeLine = 19, 
		RULE_typeEntry = 20, RULE_widgetStmt = 21, RULE_args = 22, RULE_arg = 23, 
		RULE_exprNoNewline = 24, RULE_expression = 25, RULE_lambdaExpr = 26, RULE_logicalOr = 27, 
		RULE_logicalAnd = 28, RULE_equality = 29, RULE_comparison = 30, RULE_bitwiseOr = 31, 
		RULE_bitwiseXor = 32, RULE_bitwiseAnd = 33, RULE_shift = 34, RULE_sum = 35, 
		RULE_term = 36, RULE_factor = 37, RULE_power = 38, RULE_atom = 39, RULE_argList = 40, 
		RULE_callStmt = 41, RULE_dottedName = 42, RULE_literal = 43;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "eventHandler", "typeDef", "typeFieldList", "typeField", 
			"funcDef", "paramList", "param", "suite", "simpleStmt", "exprStmt", "guiBlock", 
			"guiBody", "guiProp", "typesLine", "typesTokens", "typesDict", "typeEntries", 
			"typeLine", "typeEntry", "widgetStmt", "args", "arg", "exprNoNewline", 
			"expression", "lambdaExpr", "logicalOr", "logicalAnd", "equality", "comparison", 
			"bitwiseOr", "bitwiseXor", "bitwiseAnd", "shift", "sum", "term", "factor", 
			"power", "atom", "argList", "callStmt", "dottedName", "literal"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'='", "'or'", "'and'", null, "'->'", null, null, null, null, "'<INDENT>'", 
			"'<DEDENT>'", "'('", "')'", "':'", "','", "'{'", "'}'", "'.'", "'+'", 
			"'-'", "'*'", "'/'", "'%'", "'**'", "'~'", "'<'", "'>'", "'<='", "'>='", 
			"'=='", "'!='", "'<<'", "'>>'", "'|'", "'^'", "'&'", null, "'GUI'", null, 
			null, "'addTextField'", "'addButton'", "'addCheckBox'", "'addSlider'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, "TYPE_KW", "ARROW", "ON", "FROM", "DO", "NEWLINE", 
			"INDENT", "DEDENT", "LPAREN", "RPAREN", "COLON", "COMMA", "LBRACE", "RBRACE", 
			"DOT", "PLUS", "MINUS", "STAR", "DIV", "MOD", "POW", "TILDE", "LT", "GT", 
			"LE", "GE", "EQ", "NEQ", "LSHIFT", "RSHIFT", "BITOR", "BITXOR", "BITAND", 
			"DEF", "GUI_CAP", "GUI_KW", "TYPES_KW", "ADD_TEXT", "ADD_BTN", "ADD_CHECK", 
			"ADD_SLIDER", "OR", "AND", "IN", "IS", "TRUE", "FALSE", "NULL", "Float", 
			"Integer", "StringLiteral", "Identifier", "COMMENT", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "CPJ.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public CPJParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(CPJParser.EOF, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(CPJParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(CPJParser.NEWLINE, i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitProgram(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitProgram(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(92);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 71495606192312912L) != 0)) {
				{
				setState(90);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case TYPE_KW:
				case ON:
				case LPAREN:
				case PLUS:
				case MINUS:
				case TILDE:
				case DEF:
				case GUI_CAP:
				case GUI_KW:
				case TRUE:
				case FALSE:
				case NULL:
				case Float:
				case Integer:
				case StringLiteral:
				case Identifier:
					{
					setState(88);
					statement();
					}
					break;
				case NEWLINE:
					{
					setState(89);
					match(NEWLINE);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(94);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(95);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public GuiBlockContext guiBlock() {
			return getRuleContext(GuiBlockContext.class,0);
		}
		public FuncDefContext funcDef() {
			return getRuleContext(FuncDefContext.class,0);
		}
		public TypeDefContext typeDef() {
			return getRuleContext(TypeDefContext.class,0);
		}
		public EventHandlerContext eventHandler() {
			return getRuleContext(EventHandlerContext.class,0);
		}
		public ExprStmtContext exprStmt() {
			return getRuleContext(ExprStmtContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(102);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case GUI_CAP:
			case GUI_KW:
				enterOuterAlt(_localctx, 1);
				{
				setState(97);
				guiBlock();
				}
				break;
			case DEF:
				enterOuterAlt(_localctx, 2);
				{
				setState(98);
				funcDef();
				}
				break;
			case TYPE_KW:
				enterOuterAlt(_localctx, 3);
				{
				setState(99);
				typeDef();
				}
				break;
			case ON:
				enterOuterAlt(_localctx, 4);
				{
				setState(100);
				eventHandler();
				}
				break;
			case LPAREN:
			case PLUS:
			case MINUS:
			case TILDE:
			case TRUE:
			case FALSE:
			case NULL:
			case Float:
			case Integer:
			case StringLiteral:
			case Identifier:
				enterOuterAlt(_localctx, 5);
				{
				setState(101);
				exprStmt();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EventHandlerContext extends ParserRuleContext {
		public Token eventName;
		public Token source;
		public TerminalNode ON() { return getToken(CPJParser.ON, 0); }
		public TerminalNode DO() { return getToken(CPJParser.DO, 0); }
		public TerminalNode COLON() { return getToken(CPJParser.COLON, 0); }
		public TerminalNode NEWLINE() { return getToken(CPJParser.NEWLINE, 0); }
		public SuiteContext suite() {
			return getRuleContext(SuiteContext.class,0);
		}
		public List<TerminalNode> Identifier() { return getTokens(CPJParser.Identifier); }
		public TerminalNode Identifier(int i) {
			return getToken(CPJParser.Identifier, i);
		}
		public TerminalNode FROM() { return getToken(CPJParser.FROM, 0); }
		public EventHandlerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_eventHandler; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterEventHandler(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitEventHandler(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitEventHandler(this);
			else return visitor.visitChildren(this);
		}
	}

	public final EventHandlerContext eventHandler() throws RecognitionException {
		EventHandlerContext _localctx = new EventHandlerContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_eventHandler);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(104);
			match(ON);
			setState(105);
			((EventHandlerContext)_localctx).eventName = match(Identifier);
			setState(108);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==FROM) {
				{
				setState(106);
				match(FROM);
				setState(107);
				((EventHandlerContext)_localctx).source = match(Identifier);
				}
			}

			setState(110);
			match(DO);
			setState(111);
			match(COLON);
			setState(112);
			match(NEWLINE);
			setState(113);
			suite();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeDefContext extends ParserRuleContext {
		public TerminalNode TYPE_KW() { return getToken(CPJParser.TYPE_KW, 0); }
		public TerminalNode Identifier() { return getToken(CPJParser.Identifier, 0); }
		public TerminalNode LBRACE() { return getToken(CPJParser.LBRACE, 0); }
		public TypeFieldListContext typeFieldList() {
			return getRuleContext(TypeFieldListContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(CPJParser.RBRACE, 0); }
		public List<TerminalNode> NEWLINE() { return getTokens(CPJParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(CPJParser.NEWLINE, i);
		}
		public TypeDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeDef; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterTypeDef(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitTypeDef(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitTypeDef(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TypeDefContext typeDef() throws RecognitionException {
		TypeDefContext _localctx = new TypeDefContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_typeDef);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			match(TYPE_KW);
			setState(116);
			match(Identifier);
			setState(117);
			match(LBRACE);
			setState(118);
			typeFieldList();
			setState(119);
			match(RBRACE);
			setState(123);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(120);
					match(NEWLINE);
					}
					} 
				}
				setState(125);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeFieldListContext extends ParserRuleContext {
		public List<TypeFieldContext> typeField() {
			return getRuleContexts(TypeFieldContext.class);
		}
		public TypeFieldContext typeField(int i) {
			return getRuleContext(TypeFieldContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(CPJParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(CPJParser.COMMA, i);
		}
		public TypeFieldListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeFieldList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterTypeFieldList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitTypeFieldList(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitTypeFieldList(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TypeFieldListContext typeFieldList() throws RecognitionException {
		TypeFieldListContext _localctx = new TypeFieldListContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_typeFieldList);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(126);
			typeField();
			setState(131);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(127);
					match(COMMA);
					setState(128);
					typeField();
					}
					} 
				}
				setState(133);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			}
			setState(135);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(134);
				match(COMMA);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeFieldContext extends ParserRuleContext {
		public List<TerminalNode> Identifier() { return getTokens(CPJParser.Identifier); }
		public TerminalNode Identifier(int i) {
			return getToken(CPJParser.Identifier, i);
		}
		public TerminalNode COLON() { return getToken(CPJParser.COLON, 0); }
		public TypeFieldContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeField; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterTypeField(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitTypeField(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitTypeField(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TypeFieldContext typeField() throws RecognitionException {
		TypeFieldContext _localctx = new TypeFieldContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_typeField);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(137);
			match(Identifier);
			setState(138);
			match(COLON);
			setState(139);
			match(Identifier);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FuncDefContext extends ParserRuleContext {
		public TerminalNode DEF() { return getToken(CPJParser.DEF, 0); }
		public List<TerminalNode> Identifier() { return getTokens(CPJParser.Identifier); }
		public TerminalNode Identifier(int i) {
			return getToken(CPJParser.Identifier, i);
		}
		public TerminalNode LPAREN() { return getToken(CPJParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(CPJParser.RPAREN, 0); }
		public TerminalNode COLON() { return getToken(CPJParser.COLON, 0); }
		public TerminalNode NEWLINE() { return getToken(CPJParser.NEWLINE, 0); }
		public SuiteContext suite() {
			return getRuleContext(SuiteContext.class,0);
		}
		public ParamListContext paramList() {
			return getRuleContext(ParamListContext.class,0);
		}
		public TerminalNode ARROW() { return getToken(CPJParser.ARROW, 0); }
		public FuncDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcDef; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterFuncDef(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitFuncDef(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitFuncDef(this);
			else return visitor.visitChildren(this);
		}
	}

	public final FuncDefContext funcDef() throws RecognitionException {
		FuncDefContext _localctx = new FuncDefContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_funcDef);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(141);
			match(DEF);
			setState(142);
			match(Identifier);
			setState(143);
			match(LPAREN);
			setState(145);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Identifier) {
				{
				setState(144);
				paramList();
				}
			}

			setState(147);
			match(RPAREN);
			setState(150);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ARROW) {
				{
				setState(148);
				match(ARROW);
				setState(149);
				match(Identifier);
				}
			}

			setState(152);
			match(COLON);
			setState(156);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NEWLINE:
				{
				setState(153);
				match(NEWLINE);
				setState(154);
				suite();
				}
				break;
			case INDENT:
			case LPAREN:
			case PLUS:
			case MINUS:
			case TILDE:
			case TRUE:
			case FALSE:
			case NULL:
			case Float:
			case Integer:
			case StringLiteral:
			case Identifier:
				{
				setState(155);
				suite();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParamListContext extends ParserRuleContext {
		public List<ParamContext> param() {
			return getRuleContexts(ParamContext.class);
		}
		public ParamContext param(int i) {
			return getRuleContext(ParamContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(CPJParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(CPJParser.COMMA, i);
		}
		public ParamListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paramList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterParamList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitParamList(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitParamList(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ParamListContext paramList() throws RecognitionException {
		ParamListContext _localctx = new ParamListContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_paramList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(158);
			param();
			setState(163);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(159);
				match(COMMA);
				setState(160);
				param();
				}
				}
				setState(165);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParamContext extends ParserRuleContext {
		public List<TerminalNode> Identifier() { return getTokens(CPJParser.Identifier); }
		public TerminalNode Identifier(int i) {
			return getToken(CPJParser.Identifier, i);
		}
		public TerminalNode COLON() { return getToken(CPJParser.COLON, 0); }
		public ParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterParam(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitParam(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitParam(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ParamContext param() throws RecognitionException {
		ParamContext _localctx = new ParamContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_param);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(166);
			match(Identifier);
			setState(169);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COLON) {
				{
				setState(167);
				match(COLON);
				setState(168);
				match(Identifier);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SuiteContext extends ParserRuleContext {
		public TerminalNode INDENT() { return getToken(CPJParser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(CPJParser.DEDENT, 0); }
		public List<TerminalNode> NEWLINE() { return getTokens(CPJParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(CPJParser.NEWLINE, i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public SimpleStmtContext simpleStmt() {
			return getRuleContext(SimpleStmtContext.class,0);
		}
		public SuiteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_suite; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterSuite(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitSuite(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitSuite(this);
			else return visitor.visitChildren(this);
		}
	}

	public final SuiteContext suite() throws RecognitionException {
		SuiteContext _localctx = new SuiteContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_suite);
		int _la;
		try {
			setState(186);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INDENT:
				enterOuterAlt(_localctx, 1);
				{
				setState(171);
				match(INDENT);
				setState(175);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==NEWLINE) {
					{
					{
					setState(172);
					match(NEWLINE);
					}
					}
					setState(177);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(179); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(178);
					statement();
					}
					}
					setState(181); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 71495606192312400L) != 0) );
				setState(183);
				match(DEDENT);
				}
				break;
			case LPAREN:
			case PLUS:
			case MINUS:
			case TILDE:
			case TRUE:
			case FALSE:
			case NULL:
			case Float:
			case Integer:
			case StringLiteral:
			case Identifier:
				enterOuterAlt(_localctx, 2);
				{
				setState(185);
				simpleStmt();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SimpleStmtContext extends ParserRuleContext {
		public ExprStmtContext exprStmt() {
			return getRuleContext(ExprStmtContext.class,0);
		}
		public SimpleStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_simpleStmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterSimpleStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitSimpleStmt(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitSimpleStmt(this);
			else return visitor.visitChildren(this);
		}
	}

	public final SimpleStmtContext simpleStmt() throws RecognitionException {
		SimpleStmtContext _localctx = new SimpleStmtContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_simpleStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(188);
			exprStmt();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprStmtContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(CPJParser.NEWLINE, 0); }
		public ExprStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprStmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterExprStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitExprStmt(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitExprStmt(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ExprStmtContext exprStmt() throws RecognitionException {
		ExprStmtContext _localctx = new ExprStmtContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_exprStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(190);
			expression();
			setState(191);
			match(NEWLINE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GuiBlockContext extends ParserRuleContext {
		public TerminalNode GUI_KW() { return getToken(CPJParser.GUI_KW, 0); }
		public TerminalNode Identifier() { return getToken(CPJParser.Identifier, 0); }
		public TerminalNode COLON() { return getToken(CPJParser.COLON, 0); }
		public List<TerminalNode> NEWLINE() { return getTokens(CPJParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(CPJParser.NEWLINE, i);
		}
		public TerminalNode INDENT() { return getToken(CPJParser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(CPJParser.DEDENT, 0); }
		public List<GuiBodyContext> guiBody() {
			return getRuleContexts(GuiBodyContext.class);
		}
		public GuiBodyContext guiBody(int i) {
			return getRuleContext(GuiBodyContext.class,i);
		}
		public List<EventHandlerContext> eventHandler() {
			return getRuleContexts(EventHandlerContext.class);
		}
		public EventHandlerContext eventHandler(int i) {
			return getRuleContext(EventHandlerContext.class,i);
		}
		public TerminalNode GUI_CAP() { return getToken(CPJParser.GUI_CAP, 0); }
		public TerminalNode LBRACE() { return getToken(CPJParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(CPJParser.RBRACE, 0); }
		public GuiBlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_guiBlock; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterGuiBlock(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitGuiBlock(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitGuiBlock(this);
			else return visitor.visitChildren(this);
		}
	}

	public final GuiBlockContext guiBlock() throws RecognitionException {
		GuiBlockContext _localctx = new GuiBlockContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_guiBlock);
		int _la;
		try {
			int _alt;
			setState(229);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case GUI_KW:
				enterOuterAlt(_localctx, 1);
				{
				setState(193);
				match(GUI_KW);
				setState(194);
				match(Identifier);
				setState(195);
				match(COLON);
				setState(196);
				match(NEWLINE);
				setState(197);
				match(INDENT);
				setState(200); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					setState(200);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case NEWLINE:
					case LPAREN:
					case PLUS:
					case MINUS:
					case TILDE:
					case TYPES_KW:
					case ADD_TEXT:
					case ADD_BTN:
					case ADD_CHECK:
					case ADD_SLIDER:
					case TRUE:
					case FALSE:
					case NULL:
					case Float:
					case Integer:
					case StringLiteral:
					case Identifier:
						{
						setState(198);
						guiBody();
						}
						break;
					case ON:
						{
						setState(199);
						eventHandler();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					}
					setState(202); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 71528728980099648L) != 0) );
				setState(204);
				match(DEDENT);
				}
				break;
			case GUI_CAP:
				enterOuterAlt(_localctx, 2);
				{
				setState(206);
				match(GUI_CAP);
				setState(207);
				match(LBRACE);
				setState(211);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==NEWLINE) {
					{
					{
					setState(208);
					match(NEWLINE);
					}
					}
					setState(213);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(214);
				match(INDENT);
				setState(217); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					setState(217);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case NEWLINE:
					case LPAREN:
					case PLUS:
					case MINUS:
					case TILDE:
					case TYPES_KW:
					case ADD_TEXT:
					case ADD_BTN:
					case ADD_CHECK:
					case ADD_SLIDER:
					case TRUE:
					case FALSE:
					case NULL:
					case Float:
					case Integer:
					case StringLiteral:
					case Identifier:
						{
						setState(215);
						guiBody();
						}
						break;
					case ON:
						{
						setState(216);
						eventHandler();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					}
					setState(219); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 71528728980099648L) != 0) );
				setState(221);
				match(DEDENT);
				setState(222);
				match(RBRACE);
				setState(226);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(223);
						match(NEWLINE);
						}
						} 
					}
					setState(228);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GuiBodyContext extends ParserRuleContext {
		public TypesLineContext typesLine() {
			return getRuleContext(TypesLineContext.class,0);
		}
		public WidgetStmtContext widgetStmt() {
			return getRuleContext(WidgetStmtContext.class,0);
		}
		public CallStmtContext callStmt() {
			return getRuleContext(CallStmtContext.class,0);
		}
		public GuiPropContext guiProp() {
			return getRuleContext(GuiPropContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(CPJParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(CPJParser.NEWLINE, i);
		}
		public GuiBodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_guiBody; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterGuiBody(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitGuiBody(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitGuiBody(this);
			else return visitor.visitChildren(this);
		}
	}

	public final GuiBodyContext guiBody() throws RecognitionException {
		GuiBodyContext _localctx = new GuiBodyContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_guiBody);
		try {
			int _alt;
			setState(244);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(231);
				typesLine();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(232);
				widgetStmt();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(233);
				callStmt();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(234);
				guiProp();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(235);
				expression();
				setState(237);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
				case 1:
					{
					setState(236);
					match(NEWLINE);
					}
					break;
				}
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(240); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(239);
						match(NEWLINE);
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(242); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GuiPropContext extends ParserRuleContext {
		public TerminalNode Identifier() { return getToken(CPJParser.Identifier, 0); }
		public TerminalNode COLON() { return getToken(CPJParser.COLON, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(CPJParser.NEWLINE, 0); }
		public GuiPropContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_guiProp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterGuiProp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitGuiProp(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitGuiProp(this);
			else return visitor.visitChildren(this);
		}
	}

	public final GuiPropContext guiProp() throws RecognitionException {
		GuiPropContext _localctx = new GuiPropContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_guiProp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(246);
			match(Identifier);
			setState(247);
			match(COLON);
			setState(248);
			expression();
			setState(249);
			match(NEWLINE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypesLineContext extends ParserRuleContext {
		public TerminalNode TYPES_KW() { return getToken(CPJParser.TYPES_KW, 0); }
		public TypesTokensContext typesTokens() {
			return getRuleContext(TypesTokensContext.class,0);
		}
		public TypesDictContext typesDict() {
			return getRuleContext(TypesDictContext.class,0);
		}
		public TypesLineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typesLine; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterTypesLine(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitTypesLine(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitTypesLine(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TypesLineContext typesLine() throws RecognitionException {
		TypesLineContext _localctx = new TypesLineContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_typesLine);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(251);
			match(TYPES_KW);
			setState(254);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Identifier:
				{
				setState(252);
				typesTokens();
				}
				break;
			case LBRACE:
				{
				setState(253);
				typesDict();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypesTokensContext extends ParserRuleContext {
		public TerminalNode NEWLINE() { return getToken(CPJParser.NEWLINE, 0); }
		public List<TerminalNode> Identifier() { return getTokens(CPJParser.Identifier); }
		public TerminalNode Identifier(int i) {
			return getToken(CPJParser.Identifier, i);
		}
		public List<TerminalNode> COLON() { return getTokens(CPJParser.COLON); }
		public TerminalNode COLON(int i) {
			return getToken(CPJParser.COLON, i);
		}
		public TypesTokensContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typesTokens; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterTypesTokens(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitTypesTokens(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitTypesTokens(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TypesTokensContext typesTokens() throws RecognitionException {
		TypesTokensContext _localctx = new TypesTokensContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_typesTokens);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(262); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(262);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,26,_ctx) ) {
				case 1:
					{
					setState(256);
					match(Identifier);
					setState(257);
					match(COLON);
					setState(258);
					match(Identifier);
					}
					break;
				case 2:
					{
					setState(259);
					match(Identifier);
					setState(260);
					match(T__0);
					setState(261);
					match(Identifier);
					}
					break;
				}
				}
				setState(264); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==Identifier );
			setState(266);
			match(NEWLINE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypesDictContext extends ParserRuleContext {
		public TerminalNode LBRACE() { return getToken(CPJParser.LBRACE, 0); }
		public TypeEntriesContext typeEntries() {
			return getRuleContext(TypeEntriesContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(CPJParser.RBRACE, 0); }
		public List<TerminalNode> NEWLINE() { return getTokens(CPJParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(CPJParser.NEWLINE, i);
		}
		public TerminalNode INDENT() { return getToken(CPJParser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(CPJParser.DEDENT, 0); }
		public List<TypeLineContext> typeLine() {
			return getRuleContexts(TypeLineContext.class);
		}
		public TypeLineContext typeLine(int i) {
			return getRuleContext(TypeLineContext.class,i);
		}
		public TypesDictContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typesDict; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterTypesDict(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitTypesDict(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitTypesDict(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TypesDictContext typesDict() throws RecognitionException {
		TypesDictContext _localctx = new TypesDictContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_typesDict);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(268);
			match(LBRACE);
			setState(290);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case StringLiteral:
			case Identifier:
				{
				setState(269);
				typeEntries();
				setState(270);
				match(RBRACE);
				setState(271);
				match(NEWLINE);
				}
				break;
			case NEWLINE:
				{
				setState(273);
				match(NEWLINE);
				setState(274);
				match(INDENT);
				setState(278);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==NEWLINE) {
					{
					{
					setState(275);
					match(NEWLINE);
					}
					}
					setState(280);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(282); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(281);
					typeLine();
					}
					}
					setState(284); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==StringLiteral || _la==Identifier );
				setState(286);
				match(DEDENT);
				setState(287);
				match(RBRACE);
				setState(288);
				match(NEWLINE);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeEntriesContext extends ParserRuleContext {
		public List<TypeEntryContext> typeEntry() {
			return getRuleContexts(TypeEntryContext.class);
		}
		public TypeEntryContext typeEntry(int i) {
			return getRuleContext(TypeEntryContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(CPJParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(CPJParser.COMMA, i);
		}
		public TypeEntriesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeEntries; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterTypeEntries(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitTypeEntries(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitTypeEntries(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TypeEntriesContext typeEntries() throws RecognitionException {
		TypeEntriesContext _localctx = new TypeEntriesContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_typeEntries);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(292);
			typeEntry();
			setState(297);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,31,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(293);
					match(COMMA);
					setState(294);
					typeEntry();
					}
					} 
				}
				setState(299);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,31,_ctx);
			}
			setState(301);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(300);
				match(COMMA);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeLineContext extends ParserRuleContext {
		public TypeEntryContext typeEntry() {
			return getRuleContext(TypeEntryContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(CPJParser.NEWLINE, 0); }
		public TerminalNode COMMA() { return getToken(CPJParser.COMMA, 0); }
		public TypeLineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeLine; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterTypeLine(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitTypeLine(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitTypeLine(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TypeLineContext typeLine() throws RecognitionException {
		TypeLineContext _localctx = new TypeLineContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_typeLine);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(303);
			typeEntry();
			setState(305);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(304);
				match(COMMA);
				}
			}

			setState(307);
			match(NEWLINE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeEntryContext extends ParserRuleContext {
		public TerminalNode COLON() { return getToken(CPJParser.COLON, 0); }
		public List<TerminalNode> StringLiteral() { return getTokens(CPJParser.StringLiteral); }
		public TerminalNode StringLiteral(int i) {
			return getToken(CPJParser.StringLiteral, i);
		}
		public List<TerminalNode> Identifier() { return getTokens(CPJParser.Identifier); }
		public TerminalNode Identifier(int i) {
			return getToken(CPJParser.Identifier, i);
		}
		public TypeEntryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeEntry; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterTypeEntry(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitTypeEntry(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitTypeEntry(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TypeEntryContext typeEntry() throws RecognitionException {
		TypeEntryContext _localctx = new TypeEntryContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_typeEntry);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(309);
			_la = _input.LA(1);
			if ( !(_la==StringLiteral || _la==Identifier) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(310);
			match(COLON);
			setState(311);
			_la = _input.LA(1);
			if ( !(_la==StringLiteral || _la==Identifier) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WidgetStmtContext extends ParserRuleContext {
		public TerminalNode ADD_TEXT() { return getToken(CPJParser.ADD_TEXT, 0); }
		public TerminalNode LPAREN() { return getToken(CPJParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(CPJParser.RPAREN, 0); }
		public ArgsContext args() {
			return getRuleContext(ArgsContext.class,0);
		}
		public TerminalNode ADD_BTN() { return getToken(CPJParser.ADD_BTN, 0); }
		public TerminalNode ADD_CHECK() { return getToken(CPJParser.ADD_CHECK, 0); }
		public TerminalNode ADD_SLIDER() { return getToken(CPJParser.ADD_SLIDER, 0); }
		public WidgetStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_widgetStmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterWidgetStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitWidgetStmt(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitWidgetStmt(this);
			else return visitor.visitChildren(this);
		}
	}

	public final WidgetStmtContext widgetStmt() throws RecognitionException {
		WidgetStmtContext _localctx = new WidgetStmtContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_widgetStmt);
		int _la;
		try {
			setState(337);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ADD_TEXT:
				enterOuterAlt(_localctx, 1);
				{
				setState(313);
				match(ADD_TEXT);
				setState(314);
				match(LPAREN);
				setState(316);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 71494644119638016L) != 0)) {
					{
					setState(315);
					args();
					}
				}

				setState(318);
				match(RPAREN);
				}
				break;
			case ADD_BTN:
				enterOuterAlt(_localctx, 2);
				{
				setState(319);
				match(ADD_BTN);
				setState(320);
				match(LPAREN);
				setState(322);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 71494644119638016L) != 0)) {
					{
					setState(321);
					args();
					}
				}

				setState(324);
				match(RPAREN);
				}
				break;
			case ADD_CHECK:
				enterOuterAlt(_localctx, 3);
				{
				setState(325);
				match(ADD_CHECK);
				setState(326);
				match(LPAREN);
				setState(328);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 71494644119638016L) != 0)) {
					{
					setState(327);
					args();
					}
				}

				setState(330);
				match(RPAREN);
				}
				break;
			case ADD_SLIDER:
				enterOuterAlt(_localctx, 4);
				{
				setState(331);
				match(ADD_SLIDER);
				setState(332);
				match(LPAREN);
				setState(334);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 71494644119638016L) != 0)) {
					{
					setState(333);
					args();
					}
				}

				setState(336);
				match(RPAREN);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgsContext extends ParserRuleContext {
		public List<ArgContext> arg() {
			return getRuleContexts(ArgContext.class);
		}
		public ArgContext arg(int i) {
			return getRuleContext(ArgContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(CPJParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(CPJParser.COMMA, i);
		}
		public ArgsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_args; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterArgs(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitArgs(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitArgs(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ArgsContext args() throws RecognitionException {
		ArgsContext _localctx = new ArgsContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_args);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(339);
			arg();
			setState(344);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(340);
				match(COMMA);
				setState(341);
				arg();
				}
				}
				setState(346);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgContext extends ParserRuleContext {
		public TerminalNode StringLiteral() { return getToken(CPJParser.StringLiteral, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ArgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arg; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterArg(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitArg(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitArg(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ArgContext arg() throws RecognitionException {
		ArgContext _localctx = new ArgContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_arg);
		try {
			setState(349);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,40,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(347);
				match(StringLiteral);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(348);
				expression();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprNoNewlineContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ExprNoNewlineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprNoNewline; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterExprNoNewline(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitExprNoNewline(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitExprNoNewline(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ExprNoNewlineContext exprNoNewline() throws RecognitionException {
		ExprNoNewlineContext _localctx = new ExprNoNewlineContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_exprNoNewline);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(351);
			expression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public LambdaExprContext lambdaExpr() {
			return getRuleContext(LambdaExprContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitExpression(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitExpression(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(353);
			lambdaExpr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LambdaExprContext extends ParserRuleContext {
		public LogicalOrContext logicalOr() {
			return getRuleContext(LogicalOrContext.class,0);
		}
		public LambdaExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lambdaExpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterLambdaExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitLambdaExpr(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitLambdaExpr(this);
			else return visitor.visitChildren(this);
		}
	}

	public final LambdaExprContext lambdaExpr() throws RecognitionException {
		LambdaExprContext _localctx = new LambdaExprContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_lambdaExpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(355);
			logicalOr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LogicalOrContext extends ParserRuleContext {
		public List<LogicalAndContext> logicalAnd() {
			return getRuleContexts(LogicalAndContext.class);
		}
		public LogicalAndContext logicalAnd(int i) {
			return getRuleContext(LogicalAndContext.class,i);
		}
		public LogicalOrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logicalOr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterLogicalOr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitLogicalOr(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitLogicalOr(this);
			else return visitor.visitChildren(this);
		}
	}

	public final LogicalOrContext logicalOr() throws RecognitionException {
		LogicalOrContext _localctx = new LogicalOrContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_logicalOr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(357);
			logicalAnd();
			setState(362);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__1) {
				{
				{
				setState(358);
				match(T__1);
				setState(359);
				logicalAnd();
				}
				}
				setState(364);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LogicalAndContext extends ParserRuleContext {
		public List<EqualityContext> equality() {
			return getRuleContexts(EqualityContext.class);
		}
		public EqualityContext equality(int i) {
			return getRuleContext(EqualityContext.class,i);
		}
		public LogicalAndContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logicalAnd; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterLogicalAnd(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitLogicalAnd(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitLogicalAnd(this);
			else return visitor.visitChildren(this);
		}
	}

	public final LogicalAndContext logicalAnd() throws RecognitionException {
		LogicalAndContext _localctx = new LogicalAndContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_logicalAnd);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(365);
			equality();
			setState(370);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__2) {
				{
				{
				setState(366);
				match(T__2);
				setState(367);
				equality();
				}
				}
				setState(372);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EqualityContext extends ParserRuleContext {
		public List<ComparisonContext> comparison() {
			return getRuleContexts(ComparisonContext.class);
		}
		public ComparisonContext comparison(int i) {
			return getRuleContext(ComparisonContext.class,i);
		}
		public List<TerminalNode> EQ() { return getTokens(CPJParser.EQ); }
		public TerminalNode EQ(int i) {
			return getToken(CPJParser.EQ, i);
		}
		public List<TerminalNode> NEQ() { return getTokens(CPJParser.NEQ); }
		public TerminalNode NEQ(int i) {
			return getToken(CPJParser.NEQ, i);
		}
		public EqualityContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_equality; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterEquality(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitEquality(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitEquality(this);
			else return visitor.visitChildren(this);
		}
	}

	public final EqualityContext equality() throws RecognitionException {
		EqualityContext _localctx = new EqualityContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_equality);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(373);
			comparison();
			setState(378);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==EQ || _la==NEQ) {
				{
				{
				setState(374);
				_la = _input.LA(1);
				if ( !(_la==EQ || _la==NEQ) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(375);
				comparison();
				}
				}
				setState(380);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ComparisonContext extends ParserRuleContext {
		public List<BitwiseOrContext> bitwiseOr() {
			return getRuleContexts(BitwiseOrContext.class);
		}
		public BitwiseOrContext bitwiseOr(int i) {
			return getRuleContext(BitwiseOrContext.class,i);
		}
		public List<TerminalNode> LT() { return getTokens(CPJParser.LT); }
		public TerminalNode LT(int i) {
			return getToken(CPJParser.LT, i);
		}
		public List<TerminalNode> GT() { return getTokens(CPJParser.GT); }
		public TerminalNode GT(int i) {
			return getToken(CPJParser.GT, i);
		}
		public List<TerminalNode> LE() { return getTokens(CPJParser.LE); }
		public TerminalNode LE(int i) {
			return getToken(CPJParser.LE, i);
		}
		public List<TerminalNode> GE() { return getTokens(CPJParser.GE); }
		public TerminalNode GE(int i) {
			return getToken(CPJParser.GE, i);
		}
		public List<TerminalNode> IN() { return getTokens(CPJParser.IN); }
		public TerminalNode IN(int i) {
			return getToken(CPJParser.IN, i);
		}
		public List<TerminalNode> IS() { return getTokens(CPJParser.IS); }
		public TerminalNode IS(int i) {
			return getToken(CPJParser.IS, i);
		}
		public ComparisonContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparison; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterComparison(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitComparison(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitComparison(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ComparisonContext comparison() throws RecognitionException {
		ComparisonContext _localctx = new ComparisonContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_comparison);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(381);
			bitwiseOr();
			setState(386);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 422213471698944L) != 0)) {
				{
				{
				setState(382);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 422213471698944L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(383);
				bitwiseOr();
				}
				}
				setState(388);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BitwiseOrContext extends ParserRuleContext {
		public List<BitwiseXorContext> bitwiseXor() {
			return getRuleContexts(BitwiseXorContext.class);
		}
		public BitwiseXorContext bitwiseXor(int i) {
			return getRuleContext(BitwiseXorContext.class,i);
		}
		public List<TerminalNode> BITOR() { return getTokens(CPJParser.BITOR); }
		public TerminalNode BITOR(int i) {
			return getToken(CPJParser.BITOR, i);
		}
		public BitwiseOrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bitwiseOr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterBitwiseOr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitBitwiseOr(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitBitwiseOr(this);
			else return visitor.visitChildren(this);
		}
	}

	public final BitwiseOrContext bitwiseOr() throws RecognitionException {
		BitwiseOrContext _localctx = new BitwiseOrContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_bitwiseOr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(389);
			bitwiseXor();
			setState(394);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==BITOR) {
				{
				{
				setState(390);
				match(BITOR);
				setState(391);
				bitwiseXor();
				}
				}
				setState(396);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BitwiseXorContext extends ParserRuleContext {
		public List<BitwiseAndContext> bitwiseAnd() {
			return getRuleContexts(BitwiseAndContext.class);
		}
		public BitwiseAndContext bitwiseAnd(int i) {
			return getRuleContext(BitwiseAndContext.class,i);
		}
		public List<TerminalNode> BITXOR() { return getTokens(CPJParser.BITXOR); }
		public TerminalNode BITXOR(int i) {
			return getToken(CPJParser.BITXOR, i);
		}
		public BitwiseXorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bitwiseXor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterBitwiseXor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitBitwiseXor(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitBitwiseXor(this);
			else return visitor.visitChildren(this);
		}
	}

	public final BitwiseXorContext bitwiseXor() throws RecognitionException {
		BitwiseXorContext _localctx = new BitwiseXorContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_bitwiseXor);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(397);
			bitwiseAnd();
			setState(402);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==BITXOR) {
				{
				{
				setState(398);
				match(BITXOR);
				setState(399);
				bitwiseAnd();
				}
				}
				setState(404);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BitwiseAndContext extends ParserRuleContext {
		public List<ShiftContext> shift() {
			return getRuleContexts(ShiftContext.class);
		}
		public ShiftContext shift(int i) {
			return getRuleContext(ShiftContext.class,i);
		}
		public List<TerminalNode> BITAND() { return getTokens(CPJParser.BITAND); }
		public TerminalNode BITAND(int i) {
			return getToken(CPJParser.BITAND, i);
		}
		public BitwiseAndContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bitwiseAnd; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterBitwiseAnd(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitBitwiseAnd(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitBitwiseAnd(this);
			else return visitor.visitChildren(this);
		}
	}

	public final BitwiseAndContext bitwiseAnd() throws RecognitionException {
		BitwiseAndContext _localctx = new BitwiseAndContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_bitwiseAnd);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(405);
			shift();
			setState(410);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==BITAND) {
				{
				{
				setState(406);
				match(BITAND);
				setState(407);
				shift();
				}
				}
				setState(412);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ShiftContext extends ParserRuleContext {
		public List<SumContext> sum() {
			return getRuleContexts(SumContext.class);
		}
		public SumContext sum(int i) {
			return getRuleContext(SumContext.class,i);
		}
		public List<TerminalNode> LSHIFT() { return getTokens(CPJParser.LSHIFT); }
		public TerminalNode LSHIFT(int i) {
			return getToken(CPJParser.LSHIFT, i);
		}
		public List<TerminalNode> RSHIFT() { return getTokens(CPJParser.RSHIFT); }
		public TerminalNode RSHIFT(int i) {
			return getToken(CPJParser.RSHIFT, i);
		}
		public ShiftContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_shift; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterShift(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitShift(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitShift(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ShiftContext shift() throws RecognitionException {
		ShiftContext _localctx = new ShiftContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_shift);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(413);
			sum();
			setState(418);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==LSHIFT || _la==RSHIFT) {
				{
				{
				setState(414);
				_la = _input.LA(1);
				if ( !(_la==LSHIFT || _la==RSHIFT) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(415);
				sum();
				}
				}
				setState(420);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SumContext extends ParserRuleContext {
		public List<TermContext> term() {
			return getRuleContexts(TermContext.class);
		}
		public TermContext term(int i) {
			return getRuleContext(TermContext.class,i);
		}
		public List<TerminalNode> PLUS() { return getTokens(CPJParser.PLUS); }
		public TerminalNode PLUS(int i) {
			return getToken(CPJParser.PLUS, i);
		}
		public List<TerminalNode> MINUS() { return getTokens(CPJParser.MINUS); }
		public TerminalNode MINUS(int i) {
			return getToken(CPJParser.MINUS, i);
		}
		public SumContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sum; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterSum(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitSum(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitSum(this);
			else return visitor.visitChildren(this);
		}
	}

	public final SumContext sum() throws RecognitionException {
		SumContext _localctx = new SumContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_sum);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(421);
			term();
			setState(426);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,49,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(422);
					_la = _input.LA(1);
					if ( !(_la==PLUS || _la==MINUS) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(423);
					term();
					}
					} 
				}
				setState(428);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,49,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TermContext extends ParserRuleContext {
		public List<FactorContext> factor() {
			return getRuleContexts(FactorContext.class);
		}
		public FactorContext factor(int i) {
			return getRuleContext(FactorContext.class,i);
		}
		public List<TerminalNode> STAR() { return getTokens(CPJParser.STAR); }
		public TerminalNode STAR(int i) {
			return getToken(CPJParser.STAR, i);
		}
		public List<TerminalNode> DIV() { return getTokens(CPJParser.DIV); }
		public TerminalNode DIV(int i) {
			return getToken(CPJParser.DIV, i);
		}
		public List<TerminalNode> MOD() { return getTokens(CPJParser.MOD); }
		public TerminalNode MOD(int i) {
			return getToken(CPJParser.MOD, i);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterTerm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitTerm(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitTerm(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_term);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(429);
			factor();
			setState(434);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 14680064L) != 0)) {
				{
				{
				setState(430);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 14680064L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(431);
				factor();
				}
				}
				setState(436);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FactorContext extends ParserRuleContext {
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public TerminalNode PLUS() { return getToken(CPJParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(CPJParser.MINUS, 0); }
		public TerminalNode TILDE() { return getToken(CPJParser.TILDE, 0); }
		public PowerContext power() {
			return getRuleContext(PowerContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterFactor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitFactor(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitFactor(this);
			else return visitor.visitChildren(this);
		}
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_factor);
		int _la;
		try {
			setState(440);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PLUS:
			case MINUS:
			case TILDE:
				enterOuterAlt(_localctx, 1);
				{
				setState(437);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 35127296L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(438);
				factor();
				}
				break;
			case LPAREN:
			case TRUE:
			case FALSE:
			case NULL:
			case Float:
			case Integer:
			case StringLiteral:
			case Identifier:
				enterOuterAlt(_localctx, 2);
				{
				setState(439);
				power();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PowerContext extends ParserRuleContext {
		public AtomContext atom() {
			return getRuleContext(AtomContext.class,0);
		}
		public TerminalNode POW() { return getToken(CPJParser.POW, 0); }
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public PowerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_power; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterPower(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitPower(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitPower(this);
			else return visitor.visitChildren(this);
		}
	}

	public final PowerContext power() throws RecognitionException {
		PowerContext _localctx = new PowerContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_power);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(442);
			atom();
			setState(445);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==POW) {
				{
				setState(443);
				match(POW);
				setState(444);
				factor();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AtomContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(CPJParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(CPJParser.RPAREN, 0); }
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public DottedNameContext dottedName() {
			return getRuleContext(DottedNameContext.class,0);
		}
		public ArgListContext argList() {
			return getRuleContext(ArgListContext.class,0);
		}
		public AtomContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atom; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterAtom(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitAtom(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitAtom(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AtomContext atom() throws RecognitionException {
		AtomContext _localctx = new AtomContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_atom);
		int _la;
		try {
			setState(460);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LPAREN:
				enterOuterAlt(_localctx, 1);
				{
				setState(447);
				match(LPAREN);
				setState(448);
				expression();
				setState(449);
				match(RPAREN);
				}
				break;
			case TRUE:
			case FALSE:
			case NULL:
			case Float:
			case Integer:
			case StringLiteral:
				enterOuterAlt(_localctx, 2);
				{
				setState(451);
				literal();
				}
				break;
			case Identifier:
				enterOuterAlt(_localctx, 3);
				{
				setState(452);
				dottedName();
				setState(458);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,54,_ctx) ) {
				case 1:
					{
					setState(453);
					match(LPAREN);
					setState(455);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 71494644119638016L) != 0)) {
						{
						setState(454);
						argList();
						}
					}

					setState(457);
					match(RPAREN);
					}
					break;
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgListContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(CPJParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(CPJParser.COMMA, i);
		}
		public ArgListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterArgList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitArgList(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitArgList(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ArgListContext argList() throws RecognitionException {
		ArgListContext _localctx = new ArgListContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_argList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(462);
			expression();
			setState(467);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(463);
				match(COMMA);
				setState(464);
				expression();
				}
				}
				setState(469);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CallStmtContext extends ParserRuleContext {
		public DottedNameContext dottedName() {
			return getRuleContext(DottedNameContext.class,0);
		}
		public TerminalNode LPAREN() { return getToken(CPJParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(CPJParser.RPAREN, 0); }
		public ArgListContext argList() {
			return getRuleContext(ArgListContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(CPJParser.NEWLINE, 0); }
		public TerminalNode INDENT() { return getToken(CPJParser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(CPJParser.DEDENT, 0); }
		public CallStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_callStmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterCallStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitCallStmt(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitCallStmt(this);
			else return visitor.visitChildren(this);
		}
	}

	public final CallStmtContext callStmt() throws RecognitionException {
		CallStmtContext _localctx = new CallStmtContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_callStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(470);
			dottedName();
			setState(471);
			match(LPAREN);
			setState(473);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 71494644119638016L) != 0)) {
				{
				setState(472);
				argList();
				}
			}

			setState(475);
			match(RPAREN);
			setState(477);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,58,_ctx) ) {
			case 1:
				{
				setState(476);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 3584L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DottedNameContext extends ParserRuleContext {
		public List<TerminalNode> Identifier() { return getTokens(CPJParser.Identifier); }
		public TerminalNode Identifier(int i) {
			return getToken(CPJParser.Identifier, i);
		}
		public List<TerminalNode> DOT() { return getTokens(CPJParser.DOT); }
		public TerminalNode DOT(int i) {
			return getToken(CPJParser.DOT, i);
		}
		public DottedNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dottedName; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterDottedName(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitDottedName(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitDottedName(this);
			else return visitor.visitChildren(this);
		}
	}

	public final DottedNameContext dottedName() throws RecognitionException {
		DottedNameContext _localctx = new DottedNameContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_dottedName);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(479);
			match(Identifier);
			setState(484);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==DOT) {
				{
				{
				setState(480);
				match(DOT);
				setState(481);
				match(Identifier);
				}
				}
				setState(486);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LiteralContext extends ParserRuleContext {
		public TerminalNode Integer() { return getToken(CPJParser.Integer, 0); }
		public TerminalNode Float() { return getToken(CPJParser.Float, 0); }
		public TerminalNode StringLiteral() { return getToken(CPJParser.StringLiteral, 0); }
		public TerminalNode TRUE() { return getToken(CPJParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(CPJParser.FALSE, 0); }
		public TerminalNode NULL() { return getToken(CPJParser.NULL, 0); }
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).enterLiteral(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CPJListener ) ((CPJListener)listener).exitLiteral(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof CPJVisitor ) return ((CPJVisitor<? extends T>)visitor).visitLiteral(this);
			else return visitor.visitChildren(this);
		}
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(487);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 35465847065542656L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u00019\u01ea\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007!\u0002\"\u0007\"\u0002"+
		"#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007&\u0002\'\u0007\'\u0002"+
		"(\u0007(\u0002)\u0007)\u0002*\u0007*\u0002+\u0007+\u0001\u0000\u0001\u0000"+
		"\u0005\u0000[\b\u0000\n\u0000\f\u0000^\t\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001"+
		"g\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002"+
		"m\b\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0005\u0003z\b\u0003\n\u0003\f\u0003}\t\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0005\u0004\u0082\b\u0004\n\u0004\f\u0004\u0085\t\u0004\u0001"+
		"\u0004\u0003\u0004\u0088\b\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006\u0092"+
		"\b\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006\u0097\b\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006\u009d\b\u0006"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0005\u0007\u00a2\b\u0007\n\u0007"+
		"\f\u0007\u00a5\t\u0007\u0001\b\u0001\b\u0001\b\u0003\b\u00aa\b\b\u0001"+
		"\t\u0001\t\u0005\t\u00ae\b\t\n\t\f\t\u00b1\t\t\u0001\t\u0004\t\u00b4\b"+
		"\t\u000b\t\f\t\u00b5\u0001\t\u0001\t\u0001\t\u0003\t\u00bb\b\t\u0001\n"+
		"\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001"+
		"\f\u0001\f\u0001\f\u0001\f\u0004\f\u00c9\b\f\u000b\f\f\f\u00ca\u0001\f"+
		"\u0001\f\u0001\f\u0001\f\u0001\f\u0005\f\u00d2\b\f\n\f\f\f\u00d5\t\f\u0001"+
		"\f\u0001\f\u0001\f\u0004\f\u00da\b\f\u000b\f\f\f\u00db\u0001\f\u0001\f"+
		"\u0001\f\u0005\f\u00e1\b\f\n\f\f\f\u00e4\t\f\u0003\f\u00e6\b\f\u0001\r"+
		"\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0003\r\u00ee\b\r\u0001\r\u0004"+
		"\r\u00f1\b\r\u000b\r\f\r\u00f2\u0003\r\u00f5\b\r\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0003\u000f\u00ff\b\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0004\u0010\u0107\b\u0010\u000b\u0010\f\u0010"+
		"\u0108\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0005\u0011\u0115"+
		"\b\u0011\n\u0011\f\u0011\u0118\t\u0011\u0001\u0011\u0004\u0011\u011b\b"+
		"\u0011\u000b\u0011\f\u0011\u011c\u0001\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0003\u0011\u0123\b\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0005"+
		"\u0012\u0128\b\u0012\n\u0012\f\u0012\u012b\t\u0012\u0001\u0012\u0003\u0012"+
		"\u012e\b\u0012\u0001\u0013\u0001\u0013\u0003\u0013\u0132\b\u0013\u0001"+
		"\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0003\u0015\u013d\b\u0015\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0003\u0015\u0143\b\u0015\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0003\u0015\u0149\b\u0015\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0003\u0015\u014f\b\u0015\u0001\u0015\u0003"+
		"\u0015\u0152\b\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0005\u0016\u0157"+
		"\b\u0016\n\u0016\f\u0016\u015a\t\u0016\u0001\u0017\u0001\u0017\u0003\u0017"+
		"\u015e\b\u0017\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019\u0001\u001a"+
		"\u0001\u001a\u0001\u001b\u0001\u001b\u0001\u001b\u0005\u001b\u0169\b\u001b"+
		"\n\u001b\f\u001b\u016c\t\u001b\u0001\u001c\u0001\u001c\u0001\u001c\u0005"+
		"\u001c\u0171\b\u001c\n\u001c\f\u001c\u0174\t\u001c\u0001\u001d\u0001\u001d"+
		"\u0001\u001d\u0005\u001d\u0179\b\u001d\n\u001d\f\u001d\u017c\t\u001d\u0001"+
		"\u001e\u0001\u001e\u0001\u001e\u0005\u001e\u0181\b\u001e\n\u001e\f\u001e"+
		"\u0184\t\u001e\u0001\u001f\u0001\u001f\u0001\u001f\u0005\u001f\u0189\b"+
		"\u001f\n\u001f\f\u001f\u018c\t\u001f\u0001 \u0001 \u0001 \u0005 \u0191"+
		"\b \n \f \u0194\t \u0001!\u0001!\u0001!\u0005!\u0199\b!\n!\f!\u019c\t"+
		"!\u0001\"\u0001\"\u0001\"\u0005\"\u01a1\b\"\n\"\f\"\u01a4\t\"\u0001#\u0001"+
		"#\u0001#\u0005#\u01a9\b#\n#\f#\u01ac\t#\u0001$\u0001$\u0001$\u0005$\u01b1"+
		"\b$\n$\f$\u01b4\t$\u0001%\u0001%\u0001%\u0003%\u01b9\b%\u0001&\u0001&"+
		"\u0001&\u0003&\u01be\b&\u0001\'\u0001\'\u0001\'\u0001\'\u0001\'\u0001"+
		"\'\u0001\'\u0001\'\u0003\'\u01c8\b\'\u0001\'\u0003\'\u01cb\b\'\u0003\'"+
		"\u01cd\b\'\u0001(\u0001(\u0001(\u0005(\u01d2\b(\n(\f(\u01d5\t(\u0001)"+
		"\u0001)\u0001)\u0003)\u01da\b)\u0001)\u0001)\u0003)\u01de\b)\u0001*\u0001"+
		"*\u0001*\u0005*\u01e3\b*\n*\f*\u01e6\t*\u0001+\u0001+\u0001+\u0000\u0000"+
		",\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a"+
		"\u001c\u001e \"$&(*,.02468:<>@BDFHJLNPRTV\u0000\t\u0001\u000067\u0001"+
		"\u0000\u001e\u001f\u0002\u0000\u001a\u001d/0\u0001\u0000 !\u0001\u0000"+
		"\u0013\u0014\u0001\u0000\u0015\u0017\u0002\u0000\u0013\u0014\u0019\u0019"+
		"\u0001\u0000\t\u000b\u0001\u000016\u0203\u0000\\\u0001\u0000\u0000\u0000"+
		"\u0002f\u0001\u0000\u0000\u0000\u0004h\u0001\u0000\u0000\u0000\u0006s"+
		"\u0001\u0000\u0000\u0000\b~\u0001\u0000\u0000\u0000\n\u0089\u0001\u0000"+
		"\u0000\u0000\f\u008d\u0001\u0000\u0000\u0000\u000e\u009e\u0001\u0000\u0000"+
		"\u0000\u0010\u00a6\u0001\u0000\u0000\u0000\u0012\u00ba\u0001\u0000\u0000"+
		"\u0000\u0014\u00bc\u0001\u0000\u0000\u0000\u0016\u00be\u0001\u0000\u0000"+
		"\u0000\u0018\u00e5\u0001\u0000\u0000\u0000\u001a\u00f4\u0001\u0000\u0000"+
		"\u0000\u001c\u00f6\u0001\u0000\u0000\u0000\u001e\u00fb\u0001\u0000\u0000"+
		"\u0000 \u0106\u0001\u0000\u0000\u0000\"\u010c\u0001\u0000\u0000\u0000"+
		"$\u0124\u0001\u0000\u0000\u0000&\u012f\u0001\u0000\u0000\u0000(\u0135"+
		"\u0001\u0000\u0000\u0000*\u0151\u0001\u0000\u0000\u0000,\u0153\u0001\u0000"+
		"\u0000\u0000.\u015d\u0001\u0000\u0000\u00000\u015f\u0001\u0000\u0000\u0000"+
		"2\u0161\u0001\u0000\u0000\u00004\u0163\u0001\u0000\u0000\u00006\u0165"+
		"\u0001\u0000\u0000\u00008\u016d\u0001\u0000\u0000\u0000:\u0175\u0001\u0000"+
		"\u0000\u0000<\u017d\u0001\u0000\u0000\u0000>\u0185\u0001\u0000\u0000\u0000"+
		"@\u018d\u0001\u0000\u0000\u0000B\u0195\u0001\u0000\u0000\u0000D\u019d"+
		"\u0001\u0000\u0000\u0000F\u01a5\u0001\u0000\u0000\u0000H\u01ad\u0001\u0000"+
		"\u0000\u0000J\u01b8\u0001\u0000\u0000\u0000L\u01ba\u0001\u0000\u0000\u0000"+
		"N\u01cc\u0001\u0000\u0000\u0000P\u01ce\u0001\u0000\u0000\u0000R\u01d6"+
		"\u0001\u0000\u0000\u0000T\u01df\u0001\u0000\u0000\u0000V\u01e7\u0001\u0000"+
		"\u0000\u0000X[\u0003\u0002\u0001\u0000Y[\u0005\t\u0000\u0000ZX\u0001\u0000"+
		"\u0000\u0000ZY\u0001\u0000\u0000\u0000[^\u0001\u0000\u0000\u0000\\Z\u0001"+
		"\u0000\u0000\u0000\\]\u0001\u0000\u0000\u0000]_\u0001\u0000\u0000\u0000"+
		"^\\\u0001\u0000\u0000\u0000_`\u0005\u0000\u0000\u0001`\u0001\u0001\u0000"+
		"\u0000\u0000ag\u0003\u0018\f\u0000bg\u0003\f\u0006\u0000cg\u0003\u0006"+
		"\u0003\u0000dg\u0003\u0004\u0002\u0000eg\u0003\u0016\u000b\u0000fa\u0001"+
		"\u0000\u0000\u0000fb\u0001\u0000\u0000\u0000fc\u0001\u0000\u0000\u0000"+
		"fd\u0001\u0000\u0000\u0000fe\u0001\u0000\u0000\u0000g\u0003\u0001\u0000"+
		"\u0000\u0000hi\u0005\u0006\u0000\u0000il\u00057\u0000\u0000jk\u0005\u0007"+
		"\u0000\u0000km\u00057\u0000\u0000lj\u0001\u0000\u0000\u0000lm\u0001\u0000"+
		"\u0000\u0000mn\u0001\u0000\u0000\u0000no\u0005\b\u0000\u0000op\u0005\u000e"+
		"\u0000\u0000pq\u0005\t\u0000\u0000qr\u0003\u0012\t\u0000r\u0005\u0001"+
		"\u0000\u0000\u0000st\u0005\u0004\u0000\u0000tu\u00057\u0000\u0000uv\u0005"+
		"\u0010\u0000\u0000vw\u0003\b\u0004\u0000w{\u0005\u0011\u0000\u0000xz\u0005"+
		"\t\u0000\u0000yx\u0001\u0000\u0000\u0000z}\u0001\u0000\u0000\u0000{y\u0001"+
		"\u0000\u0000\u0000{|\u0001\u0000\u0000\u0000|\u0007\u0001\u0000\u0000"+
		"\u0000}{\u0001\u0000\u0000\u0000~\u0083\u0003\n\u0005\u0000\u007f\u0080"+
		"\u0005\u000f\u0000\u0000\u0080\u0082\u0003\n\u0005\u0000\u0081\u007f\u0001"+
		"\u0000\u0000\u0000\u0082\u0085\u0001\u0000\u0000\u0000\u0083\u0081\u0001"+
		"\u0000\u0000\u0000\u0083\u0084\u0001\u0000\u0000\u0000\u0084\u0087\u0001"+
		"\u0000\u0000\u0000\u0085\u0083\u0001\u0000\u0000\u0000\u0086\u0088\u0005"+
		"\u000f\u0000\u0000\u0087\u0086\u0001\u0000\u0000\u0000\u0087\u0088\u0001"+
		"\u0000\u0000\u0000\u0088\t\u0001\u0000\u0000\u0000\u0089\u008a\u00057"+
		"\u0000\u0000\u008a\u008b\u0005\u000e\u0000\u0000\u008b\u008c\u00057\u0000"+
		"\u0000\u008c\u000b\u0001\u0000\u0000\u0000\u008d\u008e\u0005%\u0000\u0000"+
		"\u008e\u008f\u00057\u0000\u0000\u008f\u0091\u0005\f\u0000\u0000\u0090"+
		"\u0092\u0003\u000e\u0007\u0000\u0091\u0090\u0001\u0000\u0000\u0000\u0091"+
		"\u0092\u0001\u0000\u0000\u0000\u0092\u0093\u0001\u0000\u0000\u0000\u0093"+
		"\u0096\u0005\r\u0000\u0000\u0094\u0095\u0005\u0005\u0000\u0000\u0095\u0097"+
		"\u00057\u0000\u0000\u0096\u0094\u0001\u0000\u0000\u0000\u0096\u0097\u0001"+
		"\u0000\u0000\u0000\u0097\u0098\u0001\u0000\u0000\u0000\u0098\u009c\u0005"+
		"\u000e\u0000\u0000\u0099\u009a\u0005\t\u0000\u0000\u009a\u009d\u0003\u0012"+
		"\t\u0000\u009b\u009d\u0003\u0012\t\u0000\u009c\u0099\u0001\u0000\u0000"+
		"\u0000\u009c\u009b\u0001\u0000\u0000\u0000\u009d\r\u0001\u0000\u0000\u0000"+
		"\u009e\u00a3\u0003\u0010\b\u0000\u009f\u00a0\u0005\u000f\u0000\u0000\u00a0"+
		"\u00a2\u0003\u0010\b\u0000\u00a1\u009f\u0001\u0000\u0000\u0000\u00a2\u00a5"+
		"\u0001\u0000\u0000\u0000\u00a3\u00a1\u0001\u0000\u0000\u0000\u00a3\u00a4"+
		"\u0001\u0000\u0000\u0000\u00a4\u000f\u0001\u0000\u0000\u0000\u00a5\u00a3"+
		"\u0001\u0000\u0000\u0000\u00a6\u00a9\u00057\u0000\u0000\u00a7\u00a8\u0005"+
		"\u000e\u0000\u0000\u00a8\u00aa\u00057\u0000\u0000\u00a9\u00a7\u0001\u0000"+
		"\u0000\u0000\u00a9\u00aa\u0001\u0000\u0000\u0000\u00aa\u0011\u0001\u0000"+
		"\u0000\u0000\u00ab\u00af\u0005\n\u0000\u0000\u00ac\u00ae\u0005\t\u0000"+
		"\u0000\u00ad\u00ac\u0001\u0000\u0000\u0000\u00ae\u00b1\u0001\u0000\u0000"+
		"\u0000\u00af\u00ad\u0001\u0000\u0000\u0000\u00af\u00b0\u0001\u0000\u0000"+
		"\u0000\u00b0\u00b3\u0001\u0000\u0000\u0000\u00b1\u00af\u0001\u0000\u0000"+
		"\u0000\u00b2\u00b4\u0003\u0002\u0001\u0000\u00b3\u00b2\u0001\u0000\u0000"+
		"\u0000\u00b4\u00b5\u0001\u0000\u0000\u0000\u00b5\u00b3\u0001\u0000\u0000"+
		"\u0000\u00b5\u00b6\u0001\u0000\u0000\u0000\u00b6\u00b7\u0001\u0000\u0000"+
		"\u0000\u00b7\u00b8\u0005\u000b\u0000\u0000\u00b8\u00bb\u0001\u0000\u0000"+
		"\u0000\u00b9\u00bb\u0003\u0014\n\u0000\u00ba\u00ab\u0001\u0000\u0000\u0000"+
		"\u00ba\u00b9\u0001\u0000\u0000\u0000\u00bb\u0013\u0001\u0000\u0000\u0000"+
		"\u00bc\u00bd\u0003\u0016\u000b\u0000\u00bd\u0015\u0001\u0000\u0000\u0000"+
		"\u00be\u00bf\u00032\u0019\u0000\u00bf\u00c0\u0005\t\u0000\u0000\u00c0"+
		"\u0017\u0001\u0000\u0000\u0000\u00c1\u00c2\u0005\'\u0000\u0000\u00c2\u00c3"+
		"\u00057\u0000\u0000\u00c3\u00c4\u0005\u000e\u0000\u0000\u00c4\u00c5\u0005"+
		"\t\u0000\u0000\u00c5\u00c8\u0005\n\u0000\u0000\u00c6\u00c9\u0003\u001a"+
		"\r\u0000\u00c7\u00c9\u0003\u0004\u0002\u0000\u00c8\u00c6\u0001\u0000\u0000"+
		"\u0000\u00c8\u00c7\u0001\u0000\u0000\u0000\u00c9\u00ca\u0001\u0000\u0000"+
		"\u0000\u00ca\u00c8\u0001\u0000\u0000\u0000\u00ca\u00cb\u0001\u0000\u0000"+
		"\u0000\u00cb\u00cc\u0001\u0000\u0000\u0000\u00cc\u00cd\u0005\u000b\u0000"+
		"\u0000\u00cd\u00e6\u0001\u0000\u0000\u0000\u00ce\u00cf\u0005&\u0000\u0000"+
		"\u00cf\u00d3\u0005\u0010\u0000\u0000\u00d0\u00d2\u0005\t\u0000\u0000\u00d1"+
		"\u00d0\u0001\u0000\u0000\u0000\u00d2\u00d5\u0001\u0000\u0000\u0000\u00d3"+
		"\u00d1\u0001\u0000\u0000\u0000\u00d3\u00d4\u0001\u0000\u0000\u0000\u00d4"+
		"\u00d6\u0001\u0000\u0000\u0000\u00d5\u00d3\u0001\u0000\u0000\u0000\u00d6"+
		"\u00d9\u0005\n\u0000\u0000\u00d7\u00da\u0003\u001a\r\u0000\u00d8\u00da"+
		"\u0003\u0004\u0002\u0000\u00d9\u00d7\u0001\u0000\u0000\u0000\u00d9\u00d8"+
		"\u0001\u0000\u0000\u0000\u00da\u00db\u0001\u0000\u0000\u0000\u00db\u00d9"+
		"\u0001\u0000\u0000\u0000\u00db\u00dc\u0001\u0000\u0000\u0000\u00dc\u00dd"+
		"\u0001\u0000\u0000\u0000\u00dd\u00de\u0005\u000b\u0000\u0000\u00de\u00e2"+
		"\u0005\u0011\u0000\u0000\u00df\u00e1\u0005\t\u0000\u0000\u00e0\u00df\u0001"+
		"\u0000\u0000\u0000\u00e1\u00e4\u0001\u0000\u0000\u0000\u00e2\u00e0\u0001"+
		"\u0000\u0000\u0000\u00e2\u00e3\u0001\u0000\u0000\u0000\u00e3\u00e6\u0001"+
		"\u0000\u0000\u0000\u00e4\u00e2\u0001\u0000\u0000\u0000\u00e5\u00c1\u0001"+
		"\u0000\u0000\u0000\u00e5\u00ce\u0001\u0000\u0000\u0000\u00e6\u0019\u0001"+
		"\u0000\u0000\u0000\u00e7\u00f5\u0003\u001e\u000f\u0000\u00e8\u00f5\u0003"+
		"*\u0015\u0000\u00e9\u00f5\u0003R)\u0000\u00ea\u00f5\u0003\u001c\u000e"+
		"\u0000\u00eb\u00ed\u00032\u0019\u0000\u00ec\u00ee\u0005\t\u0000\u0000"+
		"\u00ed\u00ec\u0001\u0000\u0000\u0000\u00ed\u00ee\u0001\u0000\u0000\u0000"+
		"\u00ee\u00f5\u0001\u0000\u0000\u0000\u00ef\u00f1\u0005\t\u0000\u0000\u00f0"+
		"\u00ef\u0001\u0000\u0000\u0000\u00f1\u00f2\u0001\u0000\u0000\u0000\u00f2"+
		"\u00f0\u0001\u0000\u0000\u0000\u00f2\u00f3\u0001\u0000\u0000\u0000\u00f3"+
		"\u00f5\u0001\u0000\u0000\u0000\u00f4\u00e7\u0001\u0000\u0000\u0000\u00f4"+
		"\u00e8\u0001\u0000\u0000\u0000\u00f4\u00e9\u0001\u0000\u0000\u0000\u00f4"+
		"\u00ea\u0001\u0000\u0000\u0000\u00f4\u00eb\u0001\u0000\u0000\u0000\u00f4"+
		"\u00f0\u0001\u0000\u0000\u0000\u00f5\u001b\u0001\u0000\u0000\u0000\u00f6"+
		"\u00f7\u00057\u0000\u0000\u00f7\u00f8\u0005\u000e\u0000\u0000\u00f8\u00f9"+
		"\u00032\u0019\u0000\u00f9\u00fa\u0005\t\u0000\u0000\u00fa\u001d\u0001"+
		"\u0000\u0000\u0000\u00fb\u00fe\u0005(\u0000\u0000\u00fc\u00ff\u0003 \u0010"+
		"\u0000\u00fd\u00ff\u0003\"\u0011\u0000\u00fe\u00fc\u0001\u0000\u0000\u0000"+
		"\u00fe\u00fd\u0001\u0000\u0000\u0000\u00ff\u001f\u0001\u0000\u0000\u0000"+
		"\u0100\u0101\u00057\u0000\u0000\u0101\u0102\u0005\u000e\u0000\u0000\u0102"+
		"\u0107\u00057\u0000\u0000\u0103\u0104\u00057\u0000\u0000\u0104\u0105\u0005"+
		"\u0001\u0000\u0000\u0105\u0107\u00057\u0000\u0000\u0106\u0100\u0001\u0000"+
		"\u0000\u0000\u0106\u0103\u0001\u0000\u0000\u0000\u0107\u0108\u0001\u0000"+
		"\u0000\u0000\u0108\u0106\u0001\u0000\u0000\u0000\u0108\u0109\u0001\u0000"+
		"\u0000\u0000\u0109\u010a\u0001\u0000\u0000\u0000\u010a\u010b\u0005\t\u0000"+
		"\u0000\u010b!\u0001\u0000\u0000\u0000\u010c\u0122\u0005\u0010\u0000\u0000"+
		"\u010d\u010e\u0003$\u0012\u0000\u010e\u010f\u0005\u0011\u0000\u0000\u010f"+
		"\u0110\u0005\t\u0000\u0000\u0110\u0123\u0001\u0000\u0000\u0000\u0111\u0112"+
		"\u0005\t\u0000\u0000\u0112\u0116\u0005\n\u0000\u0000\u0113\u0115\u0005"+
		"\t\u0000\u0000\u0114\u0113\u0001\u0000\u0000\u0000\u0115\u0118\u0001\u0000"+
		"\u0000\u0000\u0116\u0114\u0001\u0000\u0000\u0000\u0116\u0117\u0001\u0000"+
		"\u0000\u0000\u0117\u011a\u0001\u0000\u0000\u0000\u0118\u0116\u0001\u0000"+
		"\u0000\u0000\u0119\u011b\u0003&\u0013\u0000\u011a\u0119\u0001\u0000\u0000"+
		"\u0000\u011b\u011c\u0001\u0000\u0000\u0000\u011c\u011a\u0001\u0000\u0000"+
		"\u0000\u011c\u011d\u0001\u0000\u0000\u0000\u011d\u011e\u0001\u0000\u0000"+
		"\u0000\u011e\u011f\u0005\u000b\u0000\u0000\u011f\u0120\u0005\u0011\u0000"+
		"\u0000\u0120\u0121\u0005\t\u0000\u0000\u0121\u0123\u0001\u0000\u0000\u0000"+
		"\u0122\u010d\u0001\u0000\u0000\u0000\u0122\u0111\u0001\u0000\u0000\u0000"+
		"\u0123#\u0001\u0000\u0000\u0000\u0124\u0129\u0003(\u0014\u0000\u0125\u0126"+
		"\u0005\u000f\u0000\u0000\u0126\u0128\u0003(\u0014\u0000\u0127\u0125\u0001"+
		"\u0000\u0000\u0000\u0128\u012b\u0001\u0000\u0000\u0000\u0129\u0127\u0001"+
		"\u0000\u0000\u0000\u0129\u012a\u0001\u0000\u0000\u0000\u012a\u012d\u0001"+
		"\u0000\u0000\u0000\u012b\u0129\u0001\u0000\u0000\u0000\u012c\u012e\u0005"+
		"\u000f\u0000\u0000\u012d\u012c\u0001\u0000\u0000\u0000\u012d\u012e\u0001"+
		"\u0000\u0000\u0000\u012e%\u0001\u0000\u0000\u0000\u012f\u0131\u0003(\u0014"+
		"\u0000\u0130\u0132\u0005\u000f\u0000\u0000\u0131\u0130\u0001\u0000\u0000"+
		"\u0000\u0131\u0132\u0001\u0000\u0000\u0000\u0132\u0133\u0001\u0000\u0000"+
		"\u0000\u0133\u0134\u0005\t\u0000\u0000\u0134\'\u0001\u0000\u0000\u0000"+
		"\u0135\u0136\u0007\u0000\u0000\u0000\u0136\u0137\u0005\u000e\u0000\u0000"+
		"\u0137\u0138\u0007\u0000\u0000\u0000\u0138)\u0001\u0000\u0000\u0000\u0139"+
		"\u013a\u0005)\u0000\u0000\u013a\u013c\u0005\f\u0000\u0000\u013b\u013d"+
		"\u0003,\u0016\u0000\u013c\u013b\u0001\u0000\u0000\u0000\u013c\u013d\u0001"+
		"\u0000\u0000\u0000\u013d\u013e\u0001\u0000\u0000\u0000\u013e\u0152\u0005"+
		"\r\u0000\u0000\u013f\u0140\u0005*\u0000\u0000\u0140\u0142\u0005\f\u0000"+
		"\u0000\u0141\u0143\u0003,\u0016\u0000\u0142\u0141\u0001\u0000\u0000\u0000"+
		"\u0142\u0143\u0001\u0000\u0000\u0000\u0143\u0144\u0001\u0000\u0000\u0000"+
		"\u0144\u0152\u0005\r\u0000\u0000\u0145\u0146\u0005+\u0000\u0000\u0146"+
		"\u0148\u0005\f\u0000\u0000\u0147\u0149\u0003,\u0016\u0000\u0148\u0147"+
		"\u0001\u0000\u0000\u0000\u0148\u0149\u0001\u0000\u0000\u0000\u0149\u014a"+
		"\u0001\u0000\u0000\u0000\u014a\u0152\u0005\r\u0000\u0000\u014b\u014c\u0005"+
		",\u0000\u0000\u014c\u014e\u0005\f\u0000\u0000\u014d\u014f\u0003,\u0016"+
		"\u0000\u014e\u014d\u0001\u0000\u0000\u0000\u014e\u014f\u0001\u0000\u0000"+
		"\u0000\u014f\u0150\u0001\u0000\u0000\u0000\u0150\u0152\u0005\r\u0000\u0000"+
		"\u0151\u0139\u0001\u0000\u0000\u0000\u0151\u013f\u0001\u0000\u0000\u0000"+
		"\u0151\u0145\u0001\u0000\u0000\u0000\u0151\u014b\u0001\u0000\u0000\u0000"+
		"\u0152+\u0001\u0000\u0000\u0000\u0153\u0158\u0003.\u0017\u0000\u0154\u0155"+
		"\u0005\u000f\u0000\u0000\u0155\u0157\u0003.\u0017\u0000\u0156\u0154\u0001"+
		"\u0000\u0000\u0000\u0157\u015a\u0001\u0000\u0000\u0000\u0158\u0156\u0001"+
		"\u0000\u0000\u0000\u0158\u0159\u0001\u0000\u0000\u0000\u0159-\u0001\u0000"+
		"\u0000\u0000\u015a\u0158\u0001\u0000\u0000\u0000\u015b\u015e\u00056\u0000"+
		"\u0000\u015c\u015e\u00032\u0019\u0000\u015d\u015b\u0001\u0000\u0000\u0000"+
		"\u015d\u015c\u0001\u0000\u0000\u0000\u015e/\u0001\u0000\u0000\u0000\u015f"+
		"\u0160\u00032\u0019\u0000\u01601\u0001\u0000\u0000\u0000\u0161\u0162\u0003"+
		"4\u001a\u0000\u01623\u0001\u0000\u0000\u0000\u0163\u0164\u00036\u001b"+
		"\u0000\u01645\u0001\u0000\u0000\u0000\u0165\u016a\u00038\u001c\u0000\u0166"+
		"\u0167\u0005\u0002\u0000\u0000\u0167\u0169\u00038\u001c\u0000\u0168\u0166"+
		"\u0001\u0000\u0000\u0000\u0169\u016c\u0001\u0000\u0000\u0000\u016a\u0168"+
		"\u0001\u0000\u0000\u0000\u016a\u016b\u0001\u0000\u0000\u0000\u016b7\u0001"+
		"\u0000\u0000\u0000\u016c\u016a\u0001\u0000\u0000\u0000\u016d\u0172\u0003"+
		":\u001d\u0000\u016e\u016f\u0005\u0003\u0000\u0000\u016f\u0171\u0003:\u001d"+
		"\u0000\u0170\u016e\u0001\u0000\u0000\u0000\u0171\u0174\u0001\u0000\u0000"+
		"\u0000\u0172\u0170\u0001\u0000\u0000\u0000\u0172\u0173\u0001\u0000\u0000"+
		"\u0000\u01739\u0001\u0000\u0000\u0000\u0174\u0172\u0001\u0000\u0000\u0000"+
		"\u0175\u017a\u0003<\u001e\u0000\u0176\u0177\u0007\u0001\u0000\u0000\u0177"+
		"\u0179\u0003<\u001e\u0000\u0178\u0176\u0001\u0000\u0000\u0000\u0179\u017c"+
		"\u0001\u0000\u0000\u0000\u017a\u0178\u0001\u0000\u0000\u0000\u017a\u017b"+
		"\u0001\u0000\u0000\u0000\u017b;\u0001\u0000\u0000\u0000\u017c\u017a\u0001"+
		"\u0000\u0000\u0000\u017d\u0182\u0003>\u001f\u0000\u017e\u017f\u0007\u0002"+
		"\u0000\u0000\u017f\u0181\u0003>\u001f\u0000\u0180\u017e\u0001\u0000\u0000"+
		"\u0000\u0181\u0184\u0001\u0000\u0000\u0000\u0182\u0180\u0001\u0000\u0000"+
		"\u0000\u0182\u0183\u0001\u0000\u0000\u0000\u0183=\u0001\u0000\u0000\u0000"+
		"\u0184\u0182\u0001\u0000\u0000\u0000\u0185\u018a\u0003@ \u0000\u0186\u0187"+
		"\u0005\"\u0000\u0000\u0187\u0189\u0003@ \u0000\u0188\u0186\u0001\u0000"+
		"\u0000\u0000\u0189\u018c\u0001\u0000\u0000\u0000\u018a\u0188\u0001\u0000"+
		"\u0000\u0000\u018a\u018b\u0001\u0000\u0000\u0000\u018b?\u0001\u0000\u0000"+
		"\u0000\u018c\u018a\u0001\u0000\u0000\u0000\u018d\u0192\u0003B!\u0000\u018e"+
		"\u018f\u0005#\u0000\u0000\u018f\u0191\u0003B!\u0000\u0190\u018e\u0001"+
		"\u0000\u0000\u0000\u0191\u0194\u0001\u0000\u0000\u0000\u0192\u0190\u0001"+
		"\u0000\u0000\u0000\u0192\u0193\u0001\u0000\u0000\u0000\u0193A\u0001\u0000"+
		"\u0000\u0000\u0194\u0192\u0001\u0000\u0000\u0000\u0195\u019a\u0003D\""+
		"\u0000\u0196\u0197\u0005$\u0000\u0000\u0197\u0199\u0003D\"\u0000\u0198"+
		"\u0196\u0001\u0000\u0000\u0000\u0199\u019c\u0001\u0000\u0000\u0000\u019a"+
		"\u0198\u0001\u0000\u0000\u0000\u019a\u019b\u0001\u0000\u0000\u0000\u019b"+
		"C\u0001\u0000\u0000\u0000\u019c\u019a\u0001\u0000\u0000\u0000\u019d\u01a2"+
		"\u0003F#\u0000\u019e\u019f\u0007\u0003\u0000\u0000\u019f\u01a1\u0003F"+
		"#\u0000\u01a0\u019e\u0001\u0000\u0000\u0000\u01a1\u01a4\u0001\u0000\u0000"+
		"\u0000\u01a2\u01a0\u0001\u0000\u0000\u0000\u01a2\u01a3\u0001\u0000\u0000"+
		"\u0000\u01a3E\u0001\u0000\u0000\u0000\u01a4\u01a2\u0001\u0000\u0000\u0000"+
		"\u01a5\u01aa\u0003H$\u0000\u01a6\u01a7\u0007\u0004\u0000\u0000\u01a7\u01a9"+
		"\u0003H$\u0000\u01a8\u01a6\u0001\u0000\u0000\u0000\u01a9\u01ac\u0001\u0000"+
		"\u0000\u0000\u01aa\u01a8\u0001\u0000\u0000\u0000\u01aa\u01ab\u0001\u0000"+
		"\u0000\u0000\u01abG\u0001\u0000\u0000\u0000\u01ac\u01aa\u0001\u0000\u0000"+
		"\u0000\u01ad\u01b2\u0003J%\u0000\u01ae\u01af\u0007\u0005\u0000\u0000\u01af"+
		"\u01b1\u0003J%\u0000\u01b0\u01ae\u0001\u0000\u0000\u0000\u01b1\u01b4\u0001"+
		"\u0000\u0000\u0000\u01b2\u01b0\u0001\u0000\u0000\u0000\u01b2\u01b3\u0001"+
		"\u0000\u0000\u0000\u01b3I\u0001\u0000\u0000\u0000\u01b4\u01b2\u0001\u0000"+
		"\u0000\u0000\u01b5\u01b6\u0007\u0006\u0000\u0000\u01b6\u01b9\u0003J%\u0000"+
		"\u01b7\u01b9\u0003L&\u0000\u01b8\u01b5\u0001\u0000\u0000\u0000\u01b8\u01b7"+
		"\u0001\u0000\u0000\u0000\u01b9K\u0001\u0000\u0000\u0000\u01ba\u01bd\u0003"+
		"N\'\u0000\u01bb\u01bc\u0005\u0018\u0000\u0000\u01bc\u01be\u0003J%\u0000"+
		"\u01bd\u01bb\u0001\u0000\u0000\u0000\u01bd\u01be\u0001\u0000\u0000\u0000"+
		"\u01beM\u0001\u0000\u0000\u0000\u01bf\u01c0\u0005\f\u0000\u0000\u01c0"+
		"\u01c1\u00032\u0019\u0000\u01c1\u01c2\u0005\r\u0000\u0000\u01c2\u01cd"+
		"\u0001\u0000\u0000\u0000\u01c3\u01cd\u0003V+\u0000\u01c4\u01ca\u0003T"+
		"*\u0000\u01c5\u01c7\u0005\f\u0000\u0000\u01c6\u01c8\u0003P(\u0000\u01c7"+
		"\u01c6\u0001\u0000\u0000\u0000\u01c7\u01c8\u0001\u0000\u0000\u0000\u01c8"+
		"\u01c9\u0001\u0000\u0000\u0000\u01c9\u01cb\u0005\r\u0000\u0000\u01ca\u01c5"+
		"\u0001\u0000\u0000\u0000\u01ca\u01cb\u0001\u0000\u0000\u0000\u01cb\u01cd"+
		"\u0001\u0000\u0000\u0000\u01cc\u01bf\u0001\u0000\u0000\u0000\u01cc\u01c3"+
		"\u0001\u0000\u0000\u0000\u01cc\u01c4\u0001\u0000\u0000\u0000\u01cdO\u0001"+
		"\u0000\u0000\u0000\u01ce\u01d3\u00032\u0019\u0000\u01cf\u01d0\u0005\u000f"+
		"\u0000\u0000\u01d0\u01d2\u00032\u0019\u0000\u01d1\u01cf\u0001\u0000\u0000"+
		"\u0000\u01d2\u01d5\u0001\u0000\u0000\u0000\u01d3\u01d1\u0001\u0000\u0000"+
		"\u0000\u01d3\u01d4\u0001\u0000\u0000\u0000\u01d4Q\u0001\u0000\u0000\u0000"+
		"\u01d5\u01d3\u0001\u0000\u0000\u0000\u01d6\u01d7\u0003T*\u0000\u01d7\u01d9"+
		"\u0005\f\u0000\u0000\u01d8\u01da\u0003P(\u0000\u01d9\u01d8\u0001\u0000"+
		"\u0000\u0000\u01d9\u01da\u0001\u0000\u0000\u0000\u01da\u01db\u0001\u0000"+
		"\u0000\u0000\u01db\u01dd\u0005\r\u0000\u0000\u01dc\u01de\u0007\u0007\u0000"+
		"\u0000\u01dd\u01dc\u0001\u0000\u0000\u0000\u01dd\u01de\u0001\u0000\u0000"+
		"\u0000\u01deS\u0001\u0000\u0000\u0000\u01df\u01e4\u00057\u0000\u0000\u01e0"+
		"\u01e1\u0005\u0012\u0000\u0000\u01e1\u01e3\u00057\u0000\u0000\u01e2\u01e0"+
		"\u0001\u0000\u0000\u0000\u01e3\u01e6\u0001\u0000\u0000\u0000\u01e4\u01e2"+
		"\u0001\u0000\u0000\u0000\u01e4\u01e5\u0001\u0000\u0000\u0000\u01e5U\u0001"+
		"\u0000\u0000\u0000\u01e6\u01e4\u0001\u0000\u0000\u0000\u01e7\u01e8\u0007"+
		"\b\u0000\u0000\u01e8W\u0001\u0000\u0000\u0000<Z\\fl{\u0083\u0087\u0091"+
		"\u0096\u009c\u00a3\u00a9\u00af\u00b5\u00ba\u00c8\u00ca\u00d3\u00d9\u00db"+
		"\u00e2\u00e5\u00ed\u00f2\u00f4\u00fe\u0106\u0108\u0116\u011c\u0122\u0129"+
		"\u012d\u0131\u013c\u0142\u0148\u014e\u0151\u0158\u015d\u016a\u0172\u017a"+
		"\u0182\u018a\u0192\u019a\u01a2\u01aa\u01b2\u01b8\u01bd\u01c7\u01ca\u01cc"+
		"\u01d3\u01d9\u01dd\u01e4";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}