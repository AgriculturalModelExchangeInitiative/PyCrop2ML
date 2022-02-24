// Generated from c:\Users\midingoy\Documents\pycropml_pheno\src\pycropml\transpiler\antlr_py\grammars\CMake.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class CMakeParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, Identifier=3, Unquoted_argument=4, Escape_sequence=5, 
		Quoted_argument=6, Bracket_argument=7, Bracket_comment=8, Line_comment=9, 
		Newline=10, Space=11;
	public static final int
		RULE_file_c = 0, RULE_command_invocation = 1, RULE_single_argument = 2, 
		RULE_compound_argument = 3;
	private static String[] makeRuleNames() {
		return new String[] {
			"file_c", "command_invocation", "single_argument", "compound_argument"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, "Identifier", "Unquoted_argument", "Escape_sequence", 
			"Quoted_argument", "Bracket_argument", "Bracket_comment", "Line_comment", 
			"Newline", "Space"
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
	public String getGrammarFileName() { return "CMake.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public CMakeParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class File_cContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(CMakeParser.EOF, 0); }
		public List<Command_invocationContext> command_invocation() {
			return getRuleContexts(Command_invocationContext.class);
		}
		public Command_invocationContext command_invocation(int i) {
			return getRuleContext(Command_invocationContext.class,i);
		}
		public File_cContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_file_c; }
	}

	public final File_cContext file_c() throws RecognitionException {
		File_cContext _localctx = new File_cContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_file_c);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(11);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==Identifier) {
				{
				{
				setState(8);
				command_invocation();
				}
				}
				setState(13);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(14);
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

	public static class Command_invocationContext extends ParserRuleContext {
		public TerminalNode Identifier() { return getToken(CMakeParser.Identifier, 0); }
		public List<Single_argumentContext> single_argument() {
			return getRuleContexts(Single_argumentContext.class);
		}
		public Single_argumentContext single_argument(int i) {
			return getRuleContext(Single_argumentContext.class,i);
		}
		public List<Compound_argumentContext> compound_argument() {
			return getRuleContexts(Compound_argumentContext.class);
		}
		public Compound_argumentContext compound_argument(int i) {
			return getRuleContext(Compound_argumentContext.class,i);
		}
		public Command_invocationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_command_invocation; }
	}

	public final Command_invocationContext command_invocation() throws RecognitionException {
		Command_invocationContext _localctx = new Command_invocationContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_command_invocation);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(16);
			match(Identifier);
			setState(17);
			match(T__0);
			setState(22);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << Identifier) | (1L << Unquoted_argument) | (1L << Quoted_argument) | (1L << Bracket_argument))) != 0)) {
				{
				setState(20);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case Identifier:
				case Unquoted_argument:
				case Quoted_argument:
				case Bracket_argument:
					{
					setState(18);
					single_argument();
					}
					break;
				case T__0:
					{
					setState(19);
					compound_argument();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(24);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(25);
			match(T__1);
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

	public static class Single_argumentContext extends ParserRuleContext {
		public TerminalNode Identifier() { return getToken(CMakeParser.Identifier, 0); }
		public TerminalNode Unquoted_argument() { return getToken(CMakeParser.Unquoted_argument, 0); }
		public TerminalNode Bracket_argument() { return getToken(CMakeParser.Bracket_argument, 0); }
		public TerminalNode Quoted_argument() { return getToken(CMakeParser.Quoted_argument, 0); }
		public Single_argumentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_single_argument; }
	}

	public final Single_argumentContext single_argument() throws RecognitionException {
		Single_argumentContext _localctx = new Single_argumentContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_single_argument);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(27);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Identifier) | (1L << Unquoted_argument) | (1L << Quoted_argument) | (1L << Bracket_argument))) != 0)) ) {
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

	public static class Compound_argumentContext extends ParserRuleContext {
		public List<Single_argumentContext> single_argument() {
			return getRuleContexts(Single_argumentContext.class);
		}
		public Single_argumentContext single_argument(int i) {
			return getRuleContext(Single_argumentContext.class,i);
		}
		public List<Compound_argumentContext> compound_argument() {
			return getRuleContexts(Compound_argumentContext.class);
		}
		public Compound_argumentContext compound_argument(int i) {
			return getRuleContext(Compound_argumentContext.class,i);
		}
		public Compound_argumentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_compound_argument; }
	}

	public final Compound_argumentContext compound_argument() throws RecognitionException {
		Compound_argumentContext _localctx = new Compound_argumentContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_compound_argument);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(29);
			match(T__0);
			setState(34);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << Identifier) | (1L << Unquoted_argument) | (1L << Quoted_argument) | (1L << Bracket_argument))) != 0)) {
				{
				setState(32);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case Identifier:
				case Unquoted_argument:
				case Quoted_argument:
				case Bracket_argument:
					{
					setState(30);
					single_argument();
					}
					break;
				case T__0:
					{
					setState(31);
					compound_argument();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(36);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(37);
			match(T__1);
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r*\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\3\2\7\2\f\n\2\f\2\16\2\17\13\2\3\2\3\2\3\3\3\3\3\3"+
		"\3\3\7\3\27\n\3\f\3\16\3\32\13\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5\7\5#\n\5"+
		"\f\5\16\5&\13\5\3\5\3\5\3\5\2\2\6\2\4\6\b\2\3\4\2\5\6\b\t\2*\2\r\3\2\2"+
		"\2\4\22\3\2\2\2\6\35\3\2\2\2\b\37\3\2\2\2\n\f\5\4\3\2\13\n\3\2\2\2\f\17"+
		"\3\2\2\2\r\13\3\2\2\2\r\16\3\2\2\2\16\20\3\2\2\2\17\r\3\2\2\2\20\21\7"+
		"\2\2\3\21\3\3\2\2\2\22\23\7\5\2\2\23\30\7\3\2\2\24\27\5\6\4\2\25\27\5"+
		"\b\5\2\26\24\3\2\2\2\26\25\3\2\2\2\27\32\3\2\2\2\30\26\3\2\2\2\30\31\3"+
		"\2\2\2\31\33\3\2\2\2\32\30\3\2\2\2\33\34\7\4\2\2\34\5\3\2\2\2\35\36\t"+
		"\2\2\2\36\7\3\2\2\2\37$\7\3\2\2 #\5\6\4\2!#\5\b\5\2\" \3\2\2\2\"!\3\2"+
		"\2\2#&\3\2\2\2$\"\3\2\2\2$%\3\2\2\2%\'\3\2\2\2&$\3\2\2\2\'(\7\4\2\2(\t"+
		"\3\2\2\2\7\r\26\30\"$";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}