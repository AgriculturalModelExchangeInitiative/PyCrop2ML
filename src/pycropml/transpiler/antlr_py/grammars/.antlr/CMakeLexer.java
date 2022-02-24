// Generated from c:\Users\midingoy\Documents\pycropml_pheno\src\pycropml\transpiler\antlr_py\grammars\CMake.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class CMakeLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, Identifier=3, Unquoted_argument=4, Escape_sequence=5, 
		Quoted_argument=6, Bracket_argument=7, Bracket_comment=8, Line_comment=9, 
		Newline=10, Space=11;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "Identifier", "Unquoted_argument", "Escape_sequence", 
			"Escape_identity", "Escape_encoded", "Escape_semicolon", "Quoted_argument", 
			"Quoted_cont", "Bracket_argument", "Bracket_arg_nested", "Bracket_comment", 
			"Line_comment", "Newline", "Space"
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


	public CMakeLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "CMake.g4"; }

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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r\u00af\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2"+
		"\3\3\3\3\3\4\3\4\7\4*\n\4\f\4\16\4-\13\4\3\5\3\5\6\5\61\n\5\r\5\16\5\62"+
		"\3\6\3\6\3\6\5\68\n\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\5\bC\n\b\3\t"+
		"\3\t\3\t\3\n\3\n\3\n\3\n\7\nL\n\n\f\n\16\nO\13\n\3\n\3\n\3\13\3\13\3\13"+
		"\5\13V\n\13\3\13\5\13Y\n\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\7"+
		"\re\n\r\f\r\16\rh\13\r\3\r\5\rk\n\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16"+
		"\3\16\3\17\3\17\3\17\3\17\7\17y\n\17\f\17\16\17|\13\17\3\17\3\17\7\17"+
		"\u0080\n\17\f\17\16\17\u0083\13\17\3\17\3\17\7\17\u0087\n\17\f\17\16\17"+
		"\u008a\13\17\3\17\3\17\7\17\u008e\n\17\f\17\16\17\u0091\13\17\5\17\u0093"+
		"\n\17\3\17\3\17\5\17\u0097\n\17\3\17\5\17\u009a\n\17\3\17\3\17\3\20\3"+
		"\20\5\20\u00a0\n\20\3\20\6\20\u00a3\n\20\r\20\16\20\u00a4\3\20\3\20\3"+
		"\21\6\21\u00aa\n\21\r\21\16\21\u00ab\3\21\3\21\3f\2\22\3\3\5\4\7\5\t\6"+
		"\13\7\r\2\17\2\21\2\23\b\25\2\27\t\31\2\33\n\35\13\37\f!\r\3\2\f\5\2C"+
		"\\aac|\6\2\62;C\\aac|\b\2\13\f\17\17\"\"$%*+^^\6\2\62;==C\\c|\4\2$$^^"+
		"\6\2\f\f\17\17??]]\4\2\f\f\17\17\5\2\f\f\17\17]]\3\3\f\f\4\2\13\13\"\""+
		"\2\u00c4\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2"+
		"\2\23\3\2\2\2\2\27\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3"+
		"\2\2\2\3#\3\2\2\2\5%\3\2\2\2\7\'\3\2\2\2\t\60\3\2\2\2\13\67\3\2\2\2\r"+
		"9\3\2\2\2\17B\3\2\2\2\21D\3\2\2\2\23G\3\2\2\2\25R\3\2\2\2\27Z\3\2\2\2"+
		"\31j\3\2\2\2\33l\3\2\2\2\35t\3\2\2\2\37\u00a2\3\2\2\2!\u00a9\3\2\2\2#"+
		"$\7*\2\2$\4\3\2\2\2%&\7+\2\2&\6\3\2\2\2\'+\t\2\2\2(*\t\3\2\2)(\3\2\2\2"+
		"*-\3\2\2\2+)\3\2\2\2+,\3\2\2\2,\b\3\2\2\2-+\3\2\2\2.\61\n\4\2\2/\61\5"+
		"\13\6\2\60.\3\2\2\2\60/\3\2\2\2\61\62\3\2\2\2\62\60\3\2\2\2\62\63\3\2"+
		"\2\2\63\n\3\2\2\2\648\5\r\7\2\658\5\17\b\2\668\5\21\t\2\67\64\3\2\2\2"+
		"\67\65\3\2\2\2\67\66\3\2\2\28\f\3\2\2\29:\7^\2\2:;\n\5\2\2;\16\3\2\2\2"+
		"<=\7^\2\2=C\7v\2\2>?\7^\2\2?C\7t\2\2@A\7^\2\2AC\7p\2\2B<\3\2\2\2B>\3\2"+
		"\2\2B@\3\2\2\2C\20\3\2\2\2DE\7^\2\2EF\7=\2\2F\22\3\2\2\2GM\7$\2\2HL\n"+
		"\6\2\2IL\5\13\6\2JL\5\25\13\2KH\3\2\2\2KI\3\2\2\2KJ\3\2\2\2LO\3\2\2\2"+
		"MK\3\2\2\2MN\3\2\2\2NP\3\2\2\2OM\3\2\2\2PQ\7$\2\2Q\24\3\2\2\2RX\7^\2\2"+
		"SU\7\17\2\2TV\7\f\2\2UT\3\2\2\2UV\3\2\2\2VY\3\2\2\2WY\7\f\2\2XS\3\2\2"+
		"\2XW\3\2\2\2Y\26\3\2\2\2Z[\7]\2\2[\\\5\31\r\2\\]\7_\2\2]\30\3\2\2\2^_"+
		"\7?\2\2_`\5\31\r\2`a\7?\2\2ak\3\2\2\2bf\7]\2\2ce\13\2\2\2dc\3\2\2\2eh"+
		"\3\2\2\2fg\3\2\2\2fd\3\2\2\2gi\3\2\2\2hf\3\2\2\2ik\7_\2\2j^\3\2\2\2jb"+
		"\3\2\2\2k\32\3\2\2\2lm\7%\2\2mn\7]\2\2no\3\2\2\2op\5\31\r\2pq\7_\2\2q"+
		"r\3\2\2\2rs\b\16\2\2s\34\3\2\2\2t\u0092\7%\2\2u\u0093\3\2\2\2vz\7]\2\2"+
		"wy\7?\2\2xw\3\2\2\2y|\3\2\2\2zx\3\2\2\2z{\3\2\2\2{\u0093\3\2\2\2|z\3\2"+
		"\2\2}\u0081\7]\2\2~\u0080\7?\2\2\177~\3\2\2\2\u0080\u0083\3\2\2\2\u0081"+
		"\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0084\3\2\2\2\u0083\u0081\3\2\2"+
		"\2\u0084\u0088\n\7\2\2\u0085\u0087\n\b\2\2\u0086\u0085\3\2\2\2\u0087\u008a"+
		"\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u0093\3\2\2\2\u008a"+
		"\u0088\3\2\2\2\u008b\u008f\n\t\2\2\u008c\u008e\n\b\2\2\u008d\u008c\3\2"+
		"\2\2\u008e\u0091\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090"+
		"\u0093\3\2\2\2\u0091\u008f\3\2\2\2\u0092u\3\2\2\2\u0092v\3\2\2\2\u0092"+
		"}\3\2\2\2\u0092\u008b\3\2\2\2\u0093\u0099\3\2\2\2\u0094\u0096\7\17\2\2"+
		"\u0095\u0097\7\f\2\2\u0096\u0095\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u009a"+
		"\3\2\2\2\u0098\u009a\t\n\2\2\u0099\u0094\3\2\2\2\u0099\u0098\3\2\2\2\u009a"+
		"\u009b\3\2\2\2\u009b\u009c\b\17\2\2\u009c\36\3\2\2\2\u009d\u009f\7\17"+
		"\2\2\u009e\u00a0\7\f\2\2\u009f\u009e\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0"+
		"\u00a3\3\2\2\2\u00a1\u00a3\7\f\2\2\u00a2\u009d\3\2\2\2\u00a2\u00a1\3\2"+
		"\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5"+
		"\u00a6\3\2\2\2\u00a6\u00a7\b\20\2\2\u00a7 \3\2\2\2\u00a8\u00aa\t\13\2"+
		"\2\u00a9\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00ac"+
		"\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00ae\b\21\2\2\u00ae\"\3\2\2\2\31\2"+
		"+\60\62\67BKMUXfjz\u0081\u0088\u008f\u0092\u0096\u0099\u009f\u00a2\u00a4"+
		"\u00ab\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}