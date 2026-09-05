# Generated from PythonParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PythonParser import PythonParser
else:
    from PythonParser import PythonParser

# This class defines a complete listener for a parse tree produced by PythonParser.
class PythonParserListener(ParseTreeListener):

    # Enter a parse tree produced by PythonParser#root.
    def enterRoot(self, ctx:PythonParser.RootContext):
        pass

    # Exit a parse tree produced by PythonParser#root.
    def exitRoot(self, ctx:PythonParser.RootContext):
        pass


    # Enter a parse tree produced by PythonParser#single_input.
    def enterSingle_input(self, ctx:PythonParser.Single_inputContext):
        pass

    # Exit a parse tree produced by PythonParser#single_input.
    def exitSingle_input(self, ctx:PythonParser.Single_inputContext):
        pass


    # Enter a parse tree produced by PythonParser#file_input.
    def enterFile_input(self, ctx:PythonParser.File_inputContext):
        pass

    # Exit a parse tree produced by PythonParser#file_input.
    def exitFile_input(self, ctx:PythonParser.File_inputContext):
        pass


    # Enter a parse tree produced by PythonParser#eval_input.
    def enterEval_input(self, ctx:PythonParser.Eval_inputContext):
        pass

    # Exit a parse tree produced by PythonParser#eval_input.
    def exitEval_input(self, ctx:PythonParser.Eval_inputContext):
        pass


    # Enter a parse tree produced by PythonParser#stmt.
    def enterStmt(self, ctx:PythonParser.StmtContext):
        pass

    # Exit a parse tree produced by PythonParser#stmt.
    def exitStmt(self, ctx:PythonParser.StmtContext):
        pass


    # Enter a parse tree produced by PythonParser#if_stmt.
    def enterIf_stmt(self, ctx:PythonParser.If_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#if_stmt.
    def exitIf_stmt(self, ctx:PythonParser.If_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#while_stmt.
    def enterWhile_stmt(self, ctx:PythonParser.While_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#while_stmt.
    def exitWhile_stmt(self, ctx:PythonParser.While_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#for_stmt.
    def enterFor_stmt(self, ctx:PythonParser.For_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#for_stmt.
    def exitFor_stmt(self, ctx:PythonParser.For_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#try_stmt.
    def enterTry_stmt(self, ctx:PythonParser.Try_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#try_stmt.
    def exitTry_stmt(self, ctx:PythonParser.Try_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#with_stmt.
    def enterWith_stmt(self, ctx:PythonParser.With_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#with_stmt.
    def exitWith_stmt(self, ctx:PythonParser.With_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#class_or_func_def_stmt.
    def enterClass_or_func_def_stmt(self, ctx:PythonParser.Class_or_func_def_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#class_or_func_def_stmt.
    def exitClass_or_func_def_stmt(self, ctx:PythonParser.Class_or_func_def_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#suite.
    def enterSuite(self, ctx:PythonParser.SuiteContext):
        pass

    # Exit a parse tree produced by PythonParser#suite.
    def exitSuite(self, ctx:PythonParser.SuiteContext):
        pass


    # Enter a parse tree produced by PythonParser#decorator.
    def enterDecorator(self, ctx:PythonParser.DecoratorContext):
        pass

    # Exit a parse tree produced by PythonParser#decorator.
    def exitDecorator(self, ctx:PythonParser.DecoratorContext):
        pass


    # Enter a parse tree produced by PythonParser#elif_clause.
    def enterElif_clause(self, ctx:PythonParser.Elif_clauseContext):
        pass

    # Exit a parse tree produced by PythonParser#elif_clause.
    def exitElif_clause(self, ctx:PythonParser.Elif_clauseContext):
        pass


    # Enter a parse tree produced by PythonParser#else_clause.
    def enterElse_clause(self, ctx:PythonParser.Else_clauseContext):
        pass

    # Exit a parse tree produced by PythonParser#else_clause.
    def exitElse_clause(self, ctx:PythonParser.Else_clauseContext):
        pass


    # Enter a parse tree produced by PythonParser#finally_clause.
    def enterFinally_clause(self, ctx:PythonParser.Finally_clauseContext):
        pass

    # Exit a parse tree produced by PythonParser#finally_clause.
    def exitFinally_clause(self, ctx:PythonParser.Finally_clauseContext):
        pass


    # Enter a parse tree produced by PythonParser#with_item.
    def enterWith_item(self, ctx:PythonParser.With_itemContext):
        pass

    # Exit a parse tree produced by PythonParser#with_item.
    def exitWith_item(self, ctx:PythonParser.With_itemContext):
        pass


    # Enter a parse tree produced by PythonParser#except_clause.
    def enterExcept_clause(self, ctx:PythonParser.Except_clauseContext):
        pass

    # Exit a parse tree produced by PythonParser#except_clause.
    def exitExcept_clause(self, ctx:PythonParser.Except_clauseContext):
        pass


    # Enter a parse tree produced by PythonParser#classdef.
    def enterClassdef(self, ctx:PythonParser.ClassdefContext):
        pass

    # Exit a parse tree produced by PythonParser#classdef.
    def exitClassdef(self, ctx:PythonParser.ClassdefContext):
        pass


    # Enter a parse tree produced by PythonParser#funcdef.
    def enterFuncdef(self, ctx:PythonParser.FuncdefContext):
        pass

    # Exit a parse tree produced by PythonParser#funcdef.
    def exitFuncdef(self, ctx:PythonParser.FuncdefContext):
        pass


    # Enter a parse tree produced by PythonParser#typedargslist.
    def enterTypedargslist(self, ctx:PythonParser.TypedargslistContext):
        pass

    # Exit a parse tree produced by PythonParser#typedargslist.
    def exitTypedargslist(self, ctx:PythonParser.TypedargslistContext):
        pass


    # Enter a parse tree produced by PythonParser#args.
    def enterArgs(self, ctx:PythonParser.ArgsContext):
        pass

    # Exit a parse tree produced by PythonParser#args.
    def exitArgs(self, ctx:PythonParser.ArgsContext):
        pass


    # Enter a parse tree produced by PythonParser#kwargs.
    def enterKwargs(self, ctx:PythonParser.KwargsContext):
        pass

    # Exit a parse tree produced by PythonParser#kwargs.
    def exitKwargs(self, ctx:PythonParser.KwargsContext):
        pass


    # Enter a parse tree produced by PythonParser#def_parameters.
    def enterDef_parameters(self, ctx:PythonParser.Def_parametersContext):
        pass

    # Exit a parse tree produced by PythonParser#def_parameters.
    def exitDef_parameters(self, ctx:PythonParser.Def_parametersContext):
        pass


    # Enter a parse tree produced by PythonParser#def_parameter.
    def enterDef_parameter(self, ctx:PythonParser.Def_parameterContext):
        pass

    # Exit a parse tree produced by PythonParser#def_parameter.
    def exitDef_parameter(self, ctx:PythonParser.Def_parameterContext):
        pass


    # Enter a parse tree produced by PythonParser#named_parameter.
    def enterNamed_parameter(self, ctx:PythonParser.Named_parameterContext):
        pass

    # Exit a parse tree produced by PythonParser#named_parameter.
    def exitNamed_parameter(self, ctx:PythonParser.Named_parameterContext):
        pass


    # Enter a parse tree produced by PythonParser#simple_stmt.
    def enterSimple_stmt(self, ctx:PythonParser.Simple_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#simple_stmt.
    def exitSimple_stmt(self, ctx:PythonParser.Simple_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#expr_stmt.
    def enterExpr_stmt(self, ctx:PythonParser.Expr_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#expr_stmt.
    def exitExpr_stmt(self, ctx:PythonParser.Expr_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#print_stmt.
    def enterPrint_stmt(self, ctx:PythonParser.Print_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#print_stmt.
    def exitPrint_stmt(self, ctx:PythonParser.Print_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#del_stmt.
    def enterDel_stmt(self, ctx:PythonParser.Del_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#del_stmt.
    def exitDel_stmt(self, ctx:PythonParser.Del_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#pass_stmt.
    def enterPass_stmt(self, ctx:PythonParser.Pass_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#pass_stmt.
    def exitPass_stmt(self, ctx:PythonParser.Pass_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#break_stmt.
    def enterBreak_stmt(self, ctx:PythonParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#break_stmt.
    def exitBreak_stmt(self, ctx:PythonParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#continue_stmt.
    def enterContinue_stmt(self, ctx:PythonParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#continue_stmt.
    def exitContinue_stmt(self, ctx:PythonParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#return_stmt.
    def enterReturn_stmt(self, ctx:PythonParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#return_stmt.
    def exitReturn_stmt(self, ctx:PythonParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#raise_stmt.
    def enterRaise_stmt(self, ctx:PythonParser.Raise_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#raise_stmt.
    def exitRaise_stmt(self, ctx:PythonParser.Raise_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#yield_stmt.
    def enterYield_stmt(self, ctx:PythonParser.Yield_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#yield_stmt.
    def exitYield_stmt(self, ctx:PythonParser.Yield_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#import_stmt.
    def enterImport_stmt(self, ctx:PythonParser.Import_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#import_stmt.
    def exitImport_stmt(self, ctx:PythonParser.Import_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#from_stmt.
    def enterFrom_stmt(self, ctx:PythonParser.From_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#from_stmt.
    def exitFrom_stmt(self, ctx:PythonParser.From_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#global_stmt.
    def enterGlobal_stmt(self, ctx:PythonParser.Global_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#global_stmt.
    def exitGlobal_stmt(self, ctx:PythonParser.Global_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#exec_stmt.
    def enterExec_stmt(self, ctx:PythonParser.Exec_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#exec_stmt.
    def exitExec_stmt(self, ctx:PythonParser.Exec_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#assert_stmt.
    def enterAssert_stmt(self, ctx:PythonParser.Assert_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#assert_stmt.
    def exitAssert_stmt(self, ctx:PythonParser.Assert_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#nonlocal_stmt.
    def enterNonlocal_stmt(self, ctx:PythonParser.Nonlocal_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#nonlocal_stmt.
    def exitNonlocal_stmt(self, ctx:PythonParser.Nonlocal_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#testlist_star_expr.
    def enterTestlist_star_expr(self, ctx:PythonParser.Testlist_star_exprContext):
        pass

    # Exit a parse tree produced by PythonParser#testlist_star_expr.
    def exitTestlist_star_expr(self, ctx:PythonParser.Testlist_star_exprContext):
        pass


    # Enter a parse tree produced by PythonParser#star_expr.
    def enterStar_expr(self, ctx:PythonParser.Star_exprContext):
        pass

    # Exit a parse tree produced by PythonParser#star_expr.
    def exitStar_expr(self, ctx:PythonParser.Star_exprContext):
        pass


    # Enter a parse tree produced by PythonParser#assign_part.
    def enterAssign_part(self, ctx:PythonParser.Assign_partContext):
        pass

    # Exit a parse tree produced by PythonParser#assign_part.
    def exitAssign_part(self, ctx:PythonParser.Assign_partContext):
        pass


    # Enter a parse tree produced by PythonParser#exprlist.
    def enterExprlist(self, ctx:PythonParser.ExprlistContext):
        pass

    # Exit a parse tree produced by PythonParser#exprlist.
    def exitExprlist(self, ctx:PythonParser.ExprlistContext):
        pass


    # Enter a parse tree produced by PythonParser#import_as_names.
    def enterImport_as_names(self, ctx:PythonParser.Import_as_namesContext):
        pass

    # Exit a parse tree produced by PythonParser#import_as_names.
    def exitImport_as_names(self, ctx:PythonParser.Import_as_namesContext):
        pass


    # Enter a parse tree produced by PythonParser#import_as_name.
    def enterImport_as_name(self, ctx:PythonParser.Import_as_nameContext):
        pass

    # Exit a parse tree produced by PythonParser#import_as_name.
    def exitImport_as_name(self, ctx:PythonParser.Import_as_nameContext):
        pass


    # Enter a parse tree produced by PythonParser#dotted_as_names.
    def enterDotted_as_names(self, ctx:PythonParser.Dotted_as_namesContext):
        pass

    # Exit a parse tree produced by PythonParser#dotted_as_names.
    def exitDotted_as_names(self, ctx:PythonParser.Dotted_as_namesContext):
        pass


    # Enter a parse tree produced by PythonParser#dotted_as_name.
    def enterDotted_as_name(self, ctx:PythonParser.Dotted_as_nameContext):
        pass

    # Exit a parse tree produced by PythonParser#dotted_as_name.
    def exitDotted_as_name(self, ctx:PythonParser.Dotted_as_nameContext):
        pass


    # Enter a parse tree produced by PythonParser#test.
    def enterTest(self, ctx:PythonParser.TestContext):
        pass

    # Exit a parse tree produced by PythonParser#test.
    def exitTest(self, ctx:PythonParser.TestContext):
        pass


    # Enter a parse tree produced by PythonParser#varargslist.
    def enterVarargslist(self, ctx:PythonParser.VarargslistContext):
        pass

    # Exit a parse tree produced by PythonParser#varargslist.
    def exitVarargslist(self, ctx:PythonParser.VarargslistContext):
        pass


    # Enter a parse tree produced by PythonParser#vardef_parameters.
    def enterVardef_parameters(self, ctx:PythonParser.Vardef_parametersContext):
        pass

    # Exit a parse tree produced by PythonParser#vardef_parameters.
    def exitVardef_parameters(self, ctx:PythonParser.Vardef_parametersContext):
        pass


    # Enter a parse tree produced by PythonParser#vardef_parameter.
    def enterVardef_parameter(self, ctx:PythonParser.Vardef_parameterContext):
        pass

    # Exit a parse tree produced by PythonParser#vardef_parameter.
    def exitVardef_parameter(self, ctx:PythonParser.Vardef_parameterContext):
        pass


    # Enter a parse tree produced by PythonParser#varargs.
    def enterVarargs(self, ctx:PythonParser.VarargsContext):
        pass

    # Exit a parse tree produced by PythonParser#varargs.
    def exitVarargs(self, ctx:PythonParser.VarargsContext):
        pass


    # Enter a parse tree produced by PythonParser#varkwargs.
    def enterVarkwargs(self, ctx:PythonParser.VarkwargsContext):
        pass

    # Exit a parse tree produced by PythonParser#varkwargs.
    def exitVarkwargs(self, ctx:PythonParser.VarkwargsContext):
        pass


    # Enter a parse tree produced by PythonParser#logical_test.
    def enterLogical_test(self, ctx:PythonParser.Logical_testContext):
        pass

    # Exit a parse tree produced by PythonParser#logical_test.
    def exitLogical_test(self, ctx:PythonParser.Logical_testContext):
        pass


    # Enter a parse tree produced by PythonParser#comparison.
    def enterComparison(self, ctx:PythonParser.ComparisonContext):
        pass

    # Exit a parse tree produced by PythonParser#comparison.
    def exitComparison(self, ctx:PythonParser.ComparisonContext):
        pass


    # Enter a parse tree produced by PythonParser#expr.
    def enterExpr(self, ctx:PythonParser.ExprContext):
        pass

    # Exit a parse tree produced by PythonParser#expr.
    def exitExpr(self, ctx:PythonParser.ExprContext):
        pass


    # Enter a parse tree produced by PythonParser#atom.
    def enterAtom(self, ctx:PythonParser.AtomContext):
        pass

    # Exit a parse tree produced by PythonParser#atom.
    def exitAtom(self, ctx:PythonParser.AtomContext):
        pass


    # Enter a parse tree produced by PythonParser#dictorsetmaker.
    def enterDictorsetmaker(self, ctx:PythonParser.DictorsetmakerContext):
        pass

    # Exit a parse tree produced by PythonParser#dictorsetmaker.
    def exitDictorsetmaker(self, ctx:PythonParser.DictorsetmakerContext):
        pass


    # Enter a parse tree produced by PythonParser#testlist_comp.
    def enterTestlist_comp(self, ctx:PythonParser.Testlist_compContext):
        pass

    # Exit a parse tree produced by PythonParser#testlist_comp.
    def exitTestlist_comp(self, ctx:PythonParser.Testlist_compContext):
        pass


    # Enter a parse tree produced by PythonParser#testlist.
    def enterTestlist(self, ctx:PythonParser.TestlistContext):
        pass

    # Exit a parse tree produced by PythonParser#testlist.
    def exitTestlist(self, ctx:PythonParser.TestlistContext):
        pass


    # Enter a parse tree produced by PythonParser#dotted_name.
    def enterDotted_name(self, ctx:PythonParser.Dotted_nameContext):
        pass

    # Exit a parse tree produced by PythonParser#dotted_name.
    def exitDotted_name(self, ctx:PythonParser.Dotted_nameContext):
        pass


    # Enter a parse tree produced by PythonParser#name.
    def enterName(self, ctx:PythonParser.NameContext):
        pass

    # Exit a parse tree produced by PythonParser#name.
    def exitName(self, ctx:PythonParser.NameContext):
        pass


    # Enter a parse tree produced by PythonParser#number.
    def enterNumber(self, ctx:PythonParser.NumberContext):
        pass

    # Exit a parse tree produced by PythonParser#number.
    def exitNumber(self, ctx:PythonParser.NumberContext):
        pass


    # Enter a parse tree produced by PythonParser#integer.
    def enterInteger(self, ctx:PythonParser.IntegerContext):
        pass

    # Exit a parse tree produced by PythonParser#integer.
    def exitInteger(self, ctx:PythonParser.IntegerContext):
        pass


    # Enter a parse tree produced by PythonParser#yield_expr.
    def enterYield_expr(self, ctx:PythonParser.Yield_exprContext):
        pass

    # Exit a parse tree produced by PythonParser#yield_expr.
    def exitYield_expr(self, ctx:PythonParser.Yield_exprContext):
        pass


    # Enter a parse tree produced by PythonParser#yield_arg.
    def enterYield_arg(self, ctx:PythonParser.Yield_argContext):
        pass

    # Exit a parse tree produced by PythonParser#yield_arg.
    def exitYield_arg(self, ctx:PythonParser.Yield_argContext):
        pass


    # Enter a parse tree produced by PythonParser#trailer.
    def enterTrailer(self, ctx:PythonParser.TrailerContext):
        pass

    # Exit a parse tree produced by PythonParser#trailer.
    def exitTrailer(self, ctx:PythonParser.TrailerContext):
        pass


    # Enter a parse tree produced by PythonParser#arguments.
    def enterArguments(self, ctx:PythonParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by PythonParser#arguments.
    def exitArguments(self, ctx:PythonParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by PythonParser#arglist.
    def enterArglist(self, ctx:PythonParser.ArglistContext):
        pass

    # Exit a parse tree produced by PythonParser#arglist.
    def exitArglist(self, ctx:PythonParser.ArglistContext):
        pass


    # Enter a parse tree produced by PythonParser#argument.
    def enterArgument(self, ctx:PythonParser.ArgumentContext):
        pass

    # Exit a parse tree produced by PythonParser#argument.
    def exitArgument(self, ctx:PythonParser.ArgumentContext):
        pass


    # Enter a parse tree produced by PythonParser#subscriptlist.
    def enterSubscriptlist(self, ctx:PythonParser.SubscriptlistContext):
        pass

    # Exit a parse tree produced by PythonParser#subscriptlist.
    def exitSubscriptlist(self, ctx:PythonParser.SubscriptlistContext):
        pass


    # Enter a parse tree produced by PythonParser#subscript.
    def enterSubscript(self, ctx:PythonParser.SubscriptContext):
        pass

    # Exit a parse tree produced by PythonParser#subscript.
    def exitSubscript(self, ctx:PythonParser.SubscriptContext):
        pass


    # Enter a parse tree produced by PythonParser#sliceop.
    def enterSliceop(self, ctx:PythonParser.SliceopContext):
        pass

    # Exit a parse tree produced by PythonParser#sliceop.
    def exitSliceop(self, ctx:PythonParser.SliceopContext):
        pass


    # Enter a parse tree produced by PythonParser#comp_for.
    def enterComp_for(self, ctx:PythonParser.Comp_forContext):
        pass

    # Exit a parse tree produced by PythonParser#comp_for.
    def exitComp_for(self, ctx:PythonParser.Comp_forContext):
        pass


    # Enter a parse tree produced by PythonParser#comp_iter.
    def enterComp_iter(self, ctx:PythonParser.Comp_iterContext):
        pass

    # Exit a parse tree produced by PythonParser#comp_iter.
    def exitComp_iter(self, ctx:PythonParser.Comp_iterContext):
        pass



del PythonParser