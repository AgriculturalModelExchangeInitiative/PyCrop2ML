// Generated from c:\Users\midingoy\Documents\pycropml_pheno\src\pycropml\transpiler\antlr_py\grammars\Comments.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class CommentsLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, Identifier=3, Symbol=4, Ws=5;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "Identifier", "Symbol", "Newline", "Num", "Space", "Ws"
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


	public CommentsLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Comments.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7e\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\7\4F\n\4\f\4\16\4I\13\4\3"+
		"\5\3\5\3\5\5\5N\n\5\3\6\3\6\3\6\5\6S\n\6\3\7\3\7\3\b\6\bX\n\b\r\b\16\b"+
		"Y\3\t\6\t]\n\t\r\t\16\t^\3\t\5\tb\n\t\3\t\3\t\2\2\n\3\3\5\4\7\5\t\6\13"+
		"\2\r\2\17\2\21\7\3\2\7\5\2C\\aac|\6\2\62;C\\aac|\4\2##%%\4\2\f\f\17\17"+
		"\4\2\13\13\"\"\2g\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\21"+
		"\3\2\2\2\3\23\3\2\2\2\5,\3\2\2\2\7C\3\2\2\2\tM\3\2\2\2\13R\3\2\2\2\rT"+
		"\3\2\2\2\17W\3\2\2\2\21a\3\2\2\2\23\24\7#\2\2\24\25\7\'\2\2\25\26\7\'"+
		"\2\2\26\27\7E\2\2\27\30\7{\2\2\30\31\7o\2\2\31\32\7n\2\2\32\33\7\"\2\2"+
		"\33\34\7E\2\2\34\35\7q\2\2\35\36\7o\2\2\36\37\7o\2\2\37 \7g\2\2 !\7p\2"+
		"\2!\"\7v\2\2\"#\7u\2\2#$\7\"\2\2$%\7D\2\2%&\7g\2\2&\'\7i\2\2\'(\7k\2\2"+
		"()\7p\2\2)*\7\'\2\2*+\7\'\2\2+\4\3\2\2\2,-\7#\2\2-.\7\'\2\2./\7\'\2\2"+
		"/\60\7E\2\2\60\61\7{\2\2\61\62\7o\2\2\62\63\7n\2\2\63\64\7\"\2\2\64\65"+
		"\7E\2\2\65\66\7q\2\2\66\67\7o\2\2\678\7o\2\289\7g\2\29:\7p\2\2:;\7v\2"+
		"\2;<\7u\2\2<=\7\"\2\2=>\7G\2\2>?\7p\2\2?@\7f\2\2@A\7\'\2\2AB\7\'\2\2B"+
		"\6\3\2\2\2CG\t\2\2\2DF\t\3\2\2ED\3\2\2\2FI\3\2\2\2GE\3\2\2\2GH\3\2\2\2"+
		"H\b\3\2\2\2IG\3\2\2\2JN\t\4\2\2KL\7\61\2\2LN\7\61\2\2MJ\3\2\2\2MK\3\2"+
		"\2\2N\n\3\2\2\2OP\7\17\2\2PS\7\f\2\2QS\t\5\2\2RO\3\2\2\2RQ\3\2\2\2S\f"+
		"\3\2\2\2TU\4\62;\2U\16\3\2\2\2VX\t\6\2\2WV\3\2\2\2XY\3\2\2\2YW\3\2\2\2"+
		"YZ\3\2\2\2Z\20\3\2\2\2[]\5\17\b\2\\[\3\2\2\2]^\3\2\2\2^\\\3\2\2\2^_\3"+
		"\2\2\2_b\3\2\2\2`b\5\13\6\2a\\\3\2\2\2a`\3\2\2\2bc\3\2\2\2cd\b\t\2\2d"+
		"\22\3\2\2\2\t\2GMRY^a\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}