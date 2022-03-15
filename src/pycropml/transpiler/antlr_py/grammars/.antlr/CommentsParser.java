// Generated from c:\Users\midingoy\Documents\pycropml_pheno\src\pycropml\transpiler\antlr_py\grammars\Comments.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class CommentsParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, Identifier=3, Symbol=4, Ws=5;
	public static final int
		RULE_documentation = 0, RULE_documentationContent = 1, RULE_comment_line = 2;
	private static String[] makeRuleNames() {
		return new String[] {
			"documentation", "documentationContent", "comment_line"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'!%%Cyml Comments Begin%%'", "'!%%Cyml Comments End%%'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, "Identifier", "Symbol", "Ws"
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
	public String getGrammarFileName() { return "Comments.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public CommentsParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class DocumentationContext extends ParserRuleContext {
		public DocumentationContentContext documentationContent() {
			return getRuleContext(DocumentationContentContext.class,0);
		}
		public TerminalNode EOF() { return getToken(CommentsParser.EOF, 0); }
		public DocumentationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_documentation; }
	}

	public final DocumentationContext documentation() throws RecognitionException {
		DocumentationContext _localctx = new DocumentationContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_documentation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(6);
			match(T__0);
			setState(7);
			documentationContent();
			setState(8);
			match(T__1);
			setState(9);
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

	public static class DocumentationContentContext extends ParserRuleContext {
		public List<Comment_lineContext> comment_line() {
			return getRuleContexts(Comment_lineContext.class);
		}
		public Comment_lineContext comment_line(int i) {
			return getRuleContext(Comment_lineContext.class,i);
		}
		public DocumentationContentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_documentationContent; }
	}

	public final DocumentationContentContext documentationContent() throws RecognitionException {
		DocumentationContentContext _localctx = new DocumentationContentContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_documentationContent);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(12); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(11);
				comment_line();
				}
				}
				setState(14); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==Symbol );
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

	public static class Comment_lineContext extends ParserRuleContext {
		public TerminalNode Symbol() { return getToken(CommentsParser.Symbol, 0); }
		public TerminalNode Identifier() { return getToken(CommentsParser.Identifier, 0); }
		public Comment_lineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comment_line; }
	}

	public final Comment_lineContext comment_line() throws RecognitionException {
		Comment_lineContext _localctx = new Comment_lineContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_comment_line);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(16);
			match(Symbol);
			setState(17);
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

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\7\26\4\2\t\2\4\3"+
		"\t\3\4\4\t\4\3\2\3\2\3\2\3\2\3\2\3\3\6\3\17\n\3\r\3\16\3\20\3\4\3\4\3"+
		"\4\3\4\2\2\5\2\4\6\2\2\2\23\2\b\3\2\2\2\4\16\3\2\2\2\6\22\3\2\2\2\b\t"+
		"\7\3\2\2\t\n\5\4\3\2\n\13\7\4\2\2\13\f\7\2\2\3\f\3\3\2\2\2\r\17\5\6\4"+
		"\2\16\r\3\2\2\2\17\20\3\2\2\2\20\16\3\2\2\2\20\21\3\2\2\2\21\5\3\2\2\2"+
		"\22\23\7\6\2\2\23\24\7\5\2\2\24\7\3\2\2\2\3\20";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}