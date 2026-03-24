# Generated from CSharpParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CSharpParser import CSharpParser
else:
    from CSharpParser import CSharpParser

# This class defines a complete generic visitor for a parse tree produced by CSharpParser.

class CSharpParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSharpParser#compilation_unit.
    def visitCompilation_unit(self, ctx:CSharpParser.Compilation_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#namespace_or_type_name.
    def visitNamespace_or_type_name(self, ctx:CSharpParser.Namespace_or_type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#type_.
    def visitType_(self, ctx:CSharpParser.Type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#base_type.
    def visitBase_type(self, ctx:CSharpParser.Base_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#tuple_type.
    def visitTuple_type(self, ctx:CSharpParser.Tuple_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#tuple_element.
    def visitTuple_element(self, ctx:CSharpParser.Tuple_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#simple_type.
    def visitSimple_type(self, ctx:CSharpParser.Simple_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#numeric_type.
    def visitNumeric_type(self, ctx:CSharpParser.Numeric_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#integral_type.
    def visitIntegral_type(self, ctx:CSharpParser.Integral_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#floating_point_type.
    def visitFloating_point_type(self, ctx:CSharpParser.Floating_point_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#class_type.
    def visitClass_type(self, ctx:CSharpParser.Class_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#type_argument_list.
    def visitType_argument_list(self, ctx:CSharpParser.Type_argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#argument_list.
    def visitArgument_list(self, ctx:CSharpParser.Argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#argument.
    def visitArgument(self, ctx:CSharpParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#expression.
    def visitExpression(self, ctx:CSharpParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#non_assignment_expression.
    def visitNon_assignment_expression(self, ctx:CSharpParser.Non_assignment_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#assignment.
    def visitAssignment(self, ctx:CSharpParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#assignment_operator.
    def visitAssignment_operator(self, ctx:CSharpParser.Assignment_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#conditional_expression.
    def visitConditional_expression(self, ctx:CSharpParser.Conditional_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#null_coalescing_expression.
    def visitNull_coalescing_expression(self, ctx:CSharpParser.Null_coalescing_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#conditional_or_expression.
    def visitConditional_or_expression(self, ctx:CSharpParser.Conditional_or_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#conditional_and_expression.
    def visitConditional_and_expression(self, ctx:CSharpParser.Conditional_and_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#inclusive_or_expression.
    def visitInclusive_or_expression(self, ctx:CSharpParser.Inclusive_or_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#exclusive_or_expression.
    def visitExclusive_or_expression(self, ctx:CSharpParser.Exclusive_or_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#and_expression.
    def visitAnd_expression(self, ctx:CSharpParser.And_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#equality_expression.
    def visitEquality_expression(self, ctx:CSharpParser.Equality_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#relational_expression.
    def visitRelational_expression(self, ctx:CSharpParser.Relational_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#shift_expression.
    def visitShift_expression(self, ctx:CSharpParser.Shift_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#additive_expression.
    def visitAdditive_expression(self, ctx:CSharpParser.Additive_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#multiplicative_expression.
    def visitMultiplicative_expression(self, ctx:CSharpParser.Multiplicative_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#switch_expression.
    def visitSwitch_expression(self, ctx:CSharpParser.Switch_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#switch_expression_arms.
    def visitSwitch_expression_arms(self, ctx:CSharpParser.Switch_expression_armsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#switch_expression_arm.
    def visitSwitch_expression_arm(self, ctx:CSharpParser.Switch_expression_armContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#range_expression.
    def visitRange_expression(self, ctx:CSharpParser.Range_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#unary_expression.
    def visitUnary_expression(self, ctx:CSharpParser.Unary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#cast_expression.
    def visitCast_expression(self, ctx:CSharpParser.Cast_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#primary_expression.
    def visitPrimary_expression(self, ctx:CSharpParser.Primary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#literalExpression.
    def visitLiteralExpression(self, ctx:CSharpParser.LiteralExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#simpleNameExpression.
    def visitSimpleNameExpression(self, ctx:CSharpParser.SimpleNameExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#parenthesisExpressions.
    def visitParenthesisExpressions(self, ctx:CSharpParser.ParenthesisExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#memberAccessExpression.
    def visitMemberAccessExpression(self, ctx:CSharpParser.MemberAccessExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#literalAccessExpression.
    def visitLiteralAccessExpression(self, ctx:CSharpParser.LiteralAccessExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#thisReferenceExpression.
    def visitThisReferenceExpression(self, ctx:CSharpParser.ThisReferenceExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#baseAccessExpression.
    def visitBaseAccessExpression(self, ctx:CSharpParser.BaseAccessExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#objectCreationExpression.
    def visitObjectCreationExpression(self, ctx:CSharpParser.ObjectCreationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#tupleExpression.
    def visitTupleExpression(self, ctx:CSharpParser.TupleExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#typeofExpression.
    def visitTypeofExpression(self, ctx:CSharpParser.TypeofExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#checkedExpression.
    def visitCheckedExpression(self, ctx:CSharpParser.CheckedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#uncheckedExpression.
    def visitUncheckedExpression(self, ctx:CSharpParser.UncheckedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#defaultValueExpression.
    def visitDefaultValueExpression(self, ctx:CSharpParser.DefaultValueExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#anonymousMethodExpression.
    def visitAnonymousMethodExpression(self, ctx:CSharpParser.AnonymousMethodExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#sizeofExpression.
    def visitSizeofExpression(self, ctx:CSharpParser.SizeofExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#nameofExpression.
    def visitNameofExpression(self, ctx:CSharpParser.NameofExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#throwable_expression.
    def visitThrowable_expression(self, ctx:CSharpParser.Throwable_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#throw_expression.
    def visitThrow_expression(self, ctx:CSharpParser.Throw_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#member_access.
    def visitMember_access(self, ctx:CSharpParser.Member_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#bracket_expression.
    def visitBracket_expression(self, ctx:CSharpParser.Bracket_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#indexer_argument.
    def visitIndexer_argument(self, ctx:CSharpParser.Indexer_argumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#predefined_type.
    def visitPredefined_type(self, ctx:CSharpParser.Predefined_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#expression_list.
    def visitExpression_list(self, ctx:CSharpParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#object_or_collection_initializer.
    def visitObject_or_collection_initializer(self, ctx:CSharpParser.Object_or_collection_initializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#object_initializer.
    def visitObject_initializer(self, ctx:CSharpParser.Object_initializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#member_initializer_list.
    def visitMember_initializer_list(self, ctx:CSharpParser.Member_initializer_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#member_initializer.
    def visitMember_initializer(self, ctx:CSharpParser.Member_initializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#initializer_value.
    def visitInitializer_value(self, ctx:CSharpParser.Initializer_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#collection_initializer.
    def visitCollection_initializer(self, ctx:CSharpParser.Collection_initializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#element_initializer.
    def visitElement_initializer(self, ctx:CSharpParser.Element_initializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#anonymous_object_initializer.
    def visitAnonymous_object_initializer(self, ctx:CSharpParser.Anonymous_object_initializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#member_declarator_list.
    def visitMember_declarator_list(self, ctx:CSharpParser.Member_declarator_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#member_declarator.
    def visitMember_declarator(self, ctx:CSharpParser.Member_declaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#unbound_type_name.
    def visitUnbound_type_name(self, ctx:CSharpParser.Unbound_type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#generic_dimension_specifier.
    def visitGeneric_dimension_specifier(self, ctx:CSharpParser.Generic_dimension_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#isType.
    def visitIsType(self, ctx:CSharpParser.IsTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#isTypePatternArms.
    def visitIsTypePatternArms(self, ctx:CSharpParser.IsTypePatternArmsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#isTypePatternArm.
    def visitIsTypePatternArm(self, ctx:CSharpParser.IsTypePatternArmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#lambda_expression.
    def visitLambda_expression(self, ctx:CSharpParser.Lambda_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#anonymous_function_signature.
    def visitAnonymous_function_signature(self, ctx:CSharpParser.Anonymous_function_signatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#explicit_anonymous_function_parameter_list.
    def visitExplicit_anonymous_function_parameter_list(self, ctx:CSharpParser.Explicit_anonymous_function_parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#explicit_anonymous_function_parameter.
    def visitExplicit_anonymous_function_parameter(self, ctx:CSharpParser.Explicit_anonymous_function_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#implicit_anonymous_function_parameter_list.
    def visitImplicit_anonymous_function_parameter_list(self, ctx:CSharpParser.Implicit_anonymous_function_parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#anonymous_function_body.
    def visitAnonymous_function_body(self, ctx:CSharpParser.Anonymous_function_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#query_expression.
    def visitQuery_expression(self, ctx:CSharpParser.Query_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#from_clause.
    def visitFrom_clause(self, ctx:CSharpParser.From_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#query_body.
    def visitQuery_body(self, ctx:CSharpParser.Query_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#query_body_clause.
    def visitQuery_body_clause(self, ctx:CSharpParser.Query_body_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#let_clause.
    def visitLet_clause(self, ctx:CSharpParser.Let_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#where_clause.
    def visitWhere_clause(self, ctx:CSharpParser.Where_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#combined_join_clause.
    def visitCombined_join_clause(self, ctx:CSharpParser.Combined_join_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#orderby_clause.
    def visitOrderby_clause(self, ctx:CSharpParser.Orderby_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#ordering.
    def visitOrdering(self, ctx:CSharpParser.OrderingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#select_or_group_clause.
    def visitSelect_or_group_clause(self, ctx:CSharpParser.Select_or_group_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#query_continuation.
    def visitQuery_continuation(self, ctx:CSharpParser.Query_continuationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#statement.
    def visitStatement(self, ctx:CSharpParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#declarationStatement.
    def visitDeclarationStatement(self, ctx:CSharpParser.DeclarationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#local_function_declaration.
    def visitLocal_function_declaration(self, ctx:CSharpParser.Local_function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#local_function_header.
    def visitLocal_function_header(self, ctx:CSharpParser.Local_function_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#local_function_modifiers.
    def visitLocal_function_modifiers(self, ctx:CSharpParser.Local_function_modifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#local_function_body.
    def visitLocal_function_body(self, ctx:CSharpParser.Local_function_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#labeled_Statement.
    def visitLabeled_Statement(self, ctx:CSharpParser.Labeled_StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#embedded_statement.
    def visitEmbedded_statement(self, ctx:CSharpParser.Embedded_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#theEmptyStatement.
    def visitTheEmptyStatement(self, ctx:CSharpParser.TheEmptyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#expressionStatement.
    def visitExpressionStatement(self, ctx:CSharpParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#ifStatement.
    def visitIfStatement(self, ctx:CSharpParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#switchStatement.
    def visitSwitchStatement(self, ctx:CSharpParser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#whileStatement.
    def visitWhileStatement(self, ctx:CSharpParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#doStatement.
    def visitDoStatement(self, ctx:CSharpParser.DoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#forStatement.
    def visitForStatement(self, ctx:CSharpParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#foreachStatement.
    def visitForeachStatement(self, ctx:CSharpParser.ForeachStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#breakStatement.
    def visitBreakStatement(self, ctx:CSharpParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#continueStatement.
    def visitContinueStatement(self, ctx:CSharpParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#gotoStatement.
    def visitGotoStatement(self, ctx:CSharpParser.GotoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#returnStatement.
    def visitReturnStatement(self, ctx:CSharpParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#throwStatement.
    def visitThrowStatement(self, ctx:CSharpParser.ThrowStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#tryStatement.
    def visitTryStatement(self, ctx:CSharpParser.TryStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#checkedStatement.
    def visitCheckedStatement(self, ctx:CSharpParser.CheckedStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#uncheckedStatement.
    def visitUncheckedStatement(self, ctx:CSharpParser.UncheckedStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#lockStatement.
    def visitLockStatement(self, ctx:CSharpParser.LockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#usingStatement.
    def visitUsingStatement(self, ctx:CSharpParser.UsingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#yieldStatement.
    def visitYieldStatement(self, ctx:CSharpParser.YieldStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#unsafeStatement.
    def visitUnsafeStatement(self, ctx:CSharpParser.UnsafeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#fixedStatement.
    def visitFixedStatement(self, ctx:CSharpParser.FixedStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#block.
    def visitBlock(self, ctx:CSharpParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#local_variable_declaration.
    def visitLocal_variable_declaration(self, ctx:CSharpParser.Local_variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#local_variable_type.
    def visitLocal_variable_type(self, ctx:CSharpParser.Local_variable_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#local_variable_declarator.
    def visitLocal_variable_declarator(self, ctx:CSharpParser.Local_variable_declaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#local_variable_initializer.
    def visitLocal_variable_initializer(self, ctx:CSharpParser.Local_variable_initializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#local_constant_declaration.
    def visitLocal_constant_declaration(self, ctx:CSharpParser.Local_constant_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#if_body.
    def visitIf_body(self, ctx:CSharpParser.If_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#switch_section.
    def visitSwitch_section(self, ctx:CSharpParser.Switch_sectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#switch_label.
    def visitSwitch_label(self, ctx:CSharpParser.Switch_labelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#case_guard.
    def visitCase_guard(self, ctx:CSharpParser.Case_guardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#statement_list.
    def visitStatement_list(self, ctx:CSharpParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#for_initializer.
    def visitFor_initializer(self, ctx:CSharpParser.For_initializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#for_iterator.
    def visitFor_iterator(self, ctx:CSharpParser.For_iteratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#catch_clauses.
    def visitCatch_clauses(self, ctx:CSharpParser.Catch_clausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#specific_catch_clause.
    def visitSpecific_catch_clause(self, ctx:CSharpParser.Specific_catch_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#general_catch_clause.
    def visitGeneral_catch_clause(self, ctx:CSharpParser.General_catch_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#exception_filter.
    def visitException_filter(self, ctx:CSharpParser.Exception_filterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#finally_clause.
    def visitFinally_clause(self, ctx:CSharpParser.Finally_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#resource_acquisition.
    def visitResource_acquisition(self, ctx:CSharpParser.Resource_acquisitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#namespace_declaration.
    def visitNamespace_declaration(self, ctx:CSharpParser.Namespace_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#qualified_identifier.
    def visitQualified_identifier(self, ctx:CSharpParser.Qualified_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#namespace_body.
    def visitNamespace_body(self, ctx:CSharpParser.Namespace_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#extern_alias_directives.
    def visitExtern_alias_directives(self, ctx:CSharpParser.Extern_alias_directivesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#extern_alias_directive.
    def visitExtern_alias_directive(self, ctx:CSharpParser.Extern_alias_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#using_directives.
    def visitUsing_directives(self, ctx:CSharpParser.Using_directivesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#usingAliasDirective.
    def visitUsingAliasDirective(self, ctx:CSharpParser.UsingAliasDirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#usingNamespaceDirective.
    def visitUsingNamespaceDirective(self, ctx:CSharpParser.UsingNamespaceDirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#usingStaticDirective.
    def visitUsingStaticDirective(self, ctx:CSharpParser.UsingStaticDirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#namespace_member_declarations.
    def visitNamespace_member_declarations(self, ctx:CSharpParser.Namespace_member_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#namespace_member_declaration.
    def visitNamespace_member_declaration(self, ctx:CSharpParser.Namespace_member_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#type_declaration.
    def visitType_declaration(self, ctx:CSharpParser.Type_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#qualified_alias_member.
    def visitQualified_alias_member(self, ctx:CSharpParser.Qualified_alias_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#type_parameter_list.
    def visitType_parameter_list(self, ctx:CSharpParser.Type_parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#type_parameter.
    def visitType_parameter(self, ctx:CSharpParser.Type_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#class_base.
    def visitClass_base(self, ctx:CSharpParser.Class_baseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#interface_type_list.
    def visitInterface_type_list(self, ctx:CSharpParser.Interface_type_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#type_parameter_constraints_clauses.
    def visitType_parameter_constraints_clauses(self, ctx:CSharpParser.Type_parameter_constraints_clausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#type_parameter_constraints_clause.
    def visitType_parameter_constraints_clause(self, ctx:CSharpParser.Type_parameter_constraints_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#type_parameter_constraints.
    def visitType_parameter_constraints(self, ctx:CSharpParser.Type_parameter_constraintsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#primary_constraint.
    def visitPrimary_constraint(self, ctx:CSharpParser.Primary_constraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#secondary_constraints.
    def visitSecondary_constraints(self, ctx:CSharpParser.Secondary_constraintsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#constructor_constraint.
    def visitConstructor_constraint(self, ctx:CSharpParser.Constructor_constraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#class_body.
    def visitClass_body(self, ctx:CSharpParser.Class_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#class_member_declarations.
    def visitClass_member_declarations(self, ctx:CSharpParser.Class_member_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#class_member_declaration.
    def visitClass_member_declaration(self, ctx:CSharpParser.Class_member_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#all_member_modifiers.
    def visitAll_member_modifiers(self, ctx:CSharpParser.All_member_modifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#all_member_modifier.
    def visitAll_member_modifier(self, ctx:CSharpParser.All_member_modifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#common_member_declaration.
    def visitCommon_member_declaration(self, ctx:CSharpParser.Common_member_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#typed_member_declaration.
    def visitTyped_member_declaration(self, ctx:CSharpParser.Typed_member_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#constant_declarators.
    def visitConstant_declarators(self, ctx:CSharpParser.Constant_declaratorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#constant_declarator.
    def visitConstant_declarator(self, ctx:CSharpParser.Constant_declaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#variable_declarators.
    def visitVariable_declarators(self, ctx:CSharpParser.Variable_declaratorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#variable_declarator.
    def visitVariable_declarator(self, ctx:CSharpParser.Variable_declaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#variable_initializer.
    def visitVariable_initializer(self, ctx:CSharpParser.Variable_initializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#return_type.
    def visitReturn_type(self, ctx:CSharpParser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#member_name.
    def visitMember_name(self, ctx:CSharpParser.Member_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#method_body.
    def visitMethod_body(self, ctx:CSharpParser.Method_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#formal_parameter_list.
    def visitFormal_parameter_list(self, ctx:CSharpParser.Formal_parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#fixed_parameters.
    def visitFixed_parameters(self, ctx:CSharpParser.Fixed_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#fixed_parameter.
    def visitFixed_parameter(self, ctx:CSharpParser.Fixed_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#parameter_modifier.
    def visitParameter_modifier(self, ctx:CSharpParser.Parameter_modifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#parameter_array.
    def visitParameter_array(self, ctx:CSharpParser.Parameter_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#accessor_declarations.
    def visitAccessor_declarations(self, ctx:CSharpParser.Accessor_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#get_accessor_declaration.
    def visitGet_accessor_declaration(self, ctx:CSharpParser.Get_accessor_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#set_accessor_declaration.
    def visitSet_accessor_declaration(self, ctx:CSharpParser.Set_accessor_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#accessor_modifier.
    def visitAccessor_modifier(self, ctx:CSharpParser.Accessor_modifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#accessor_body.
    def visitAccessor_body(self, ctx:CSharpParser.Accessor_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#event_accessor_declarations.
    def visitEvent_accessor_declarations(self, ctx:CSharpParser.Event_accessor_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#add_accessor_declaration.
    def visitAdd_accessor_declaration(self, ctx:CSharpParser.Add_accessor_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#remove_accessor_declaration.
    def visitRemove_accessor_declaration(self, ctx:CSharpParser.Remove_accessor_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#overloadable_operator.
    def visitOverloadable_operator(self, ctx:CSharpParser.Overloadable_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#conversion_operator_declarator.
    def visitConversion_operator_declarator(self, ctx:CSharpParser.Conversion_operator_declaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#constructor_initializer.
    def visitConstructor_initializer(self, ctx:CSharpParser.Constructor_initializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#body.
    def visitBody(self, ctx:CSharpParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#struct_interfaces.
    def visitStruct_interfaces(self, ctx:CSharpParser.Struct_interfacesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#struct_body.
    def visitStruct_body(self, ctx:CSharpParser.Struct_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#struct_member_declaration.
    def visitStruct_member_declaration(self, ctx:CSharpParser.Struct_member_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#array_type.
    def visitArray_type(self, ctx:CSharpParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#rank_specifier.
    def visitRank_specifier(self, ctx:CSharpParser.Rank_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#array_initializer.
    def visitArray_initializer(self, ctx:CSharpParser.Array_initializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#variant_type_parameter_list.
    def visitVariant_type_parameter_list(self, ctx:CSharpParser.Variant_type_parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#variant_type_parameter.
    def visitVariant_type_parameter(self, ctx:CSharpParser.Variant_type_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#variance_annotation.
    def visitVariance_annotation(self, ctx:CSharpParser.Variance_annotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#interface_base.
    def visitInterface_base(self, ctx:CSharpParser.Interface_baseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#interface_body.
    def visitInterface_body(self, ctx:CSharpParser.Interface_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#interface_member_declaration.
    def visitInterface_member_declaration(self, ctx:CSharpParser.Interface_member_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#interface_accessors.
    def visitInterface_accessors(self, ctx:CSharpParser.Interface_accessorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#enum_base.
    def visitEnum_base(self, ctx:CSharpParser.Enum_baseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#enum_body.
    def visitEnum_body(self, ctx:CSharpParser.Enum_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#enum_member_declaration.
    def visitEnum_member_declaration(self, ctx:CSharpParser.Enum_member_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#global_attribute_section.
    def visitGlobal_attribute_section(self, ctx:CSharpParser.Global_attribute_sectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#global_attribute_target.
    def visitGlobal_attribute_target(self, ctx:CSharpParser.Global_attribute_targetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#attributes.
    def visitAttributes(self, ctx:CSharpParser.AttributesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#attribute_section.
    def visitAttribute_section(self, ctx:CSharpParser.Attribute_sectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#attribute_target.
    def visitAttribute_target(self, ctx:CSharpParser.Attribute_targetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#attribute_list.
    def visitAttribute_list(self, ctx:CSharpParser.Attribute_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#attribute.
    def visitAttribute(self, ctx:CSharpParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#attribute_argument.
    def visitAttribute_argument(self, ctx:CSharpParser.Attribute_argumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#pointer_type.
    def visitPointer_type(self, ctx:CSharpParser.Pointer_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#fixed_pointer_declarators.
    def visitFixed_pointer_declarators(self, ctx:CSharpParser.Fixed_pointer_declaratorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#fixed_pointer_declarator.
    def visitFixed_pointer_declarator(self, ctx:CSharpParser.Fixed_pointer_declaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#fixed_pointer_initializer.
    def visitFixed_pointer_initializer(self, ctx:CSharpParser.Fixed_pointer_initializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#fixed_size_buffer_declarator.
    def visitFixed_size_buffer_declarator(self, ctx:CSharpParser.Fixed_size_buffer_declaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#stackalloc_initializer.
    def visitStackalloc_initializer(self, ctx:CSharpParser.Stackalloc_initializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#right_arrow.
    def visitRight_arrow(self, ctx:CSharpParser.Right_arrowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#right_shift.
    def visitRight_shift(self, ctx:CSharpParser.Right_shiftContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#right_shift_assignment.
    def visitRight_shift_assignment(self, ctx:CSharpParser.Right_shift_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#literal.
    def visitLiteral(self, ctx:CSharpParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#boolean_literal.
    def visitBoolean_literal(self, ctx:CSharpParser.Boolean_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#string_literal.
    def visitString_literal(self, ctx:CSharpParser.String_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#interpolated_regular_string.
    def visitInterpolated_regular_string(self, ctx:CSharpParser.Interpolated_regular_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#interpolated_verbatium_string.
    def visitInterpolated_verbatium_string(self, ctx:CSharpParser.Interpolated_verbatium_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#interpolated_regular_string_part.
    def visitInterpolated_regular_string_part(self, ctx:CSharpParser.Interpolated_regular_string_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#interpolated_verbatium_string_part.
    def visitInterpolated_verbatium_string_part(self, ctx:CSharpParser.Interpolated_verbatium_string_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#interpolated_string_expression.
    def visitInterpolated_string_expression(self, ctx:CSharpParser.Interpolated_string_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#keyword.
    def visitKeyword(self, ctx:CSharpParser.KeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#class_definition.
    def visitClass_definition(self, ctx:CSharpParser.Class_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#struct_definition.
    def visitStruct_definition(self, ctx:CSharpParser.Struct_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#interface_definition.
    def visitInterface_definition(self, ctx:CSharpParser.Interface_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#enum_definition.
    def visitEnum_definition(self, ctx:CSharpParser.Enum_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#delegate_definition.
    def visitDelegate_definition(self, ctx:CSharpParser.Delegate_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#event_declaration.
    def visitEvent_declaration(self, ctx:CSharpParser.Event_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#field_declaration.
    def visitField_declaration(self, ctx:CSharpParser.Field_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#property_declaration.
    def visitProperty_declaration(self, ctx:CSharpParser.Property_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#constant_declaration.
    def visitConstant_declaration(self, ctx:CSharpParser.Constant_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#indexer_declaration.
    def visitIndexer_declaration(self, ctx:CSharpParser.Indexer_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#destructor_definition.
    def visitDestructor_definition(self, ctx:CSharpParser.Destructor_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#constructor_declaration.
    def visitConstructor_declaration(self, ctx:CSharpParser.Constructor_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#method_declaration.
    def visitMethod_declaration(self, ctx:CSharpParser.Method_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#method_member_name.
    def visitMethod_member_name(self, ctx:CSharpParser.Method_member_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#operator_declaration.
    def visitOperator_declaration(self, ctx:CSharpParser.Operator_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#arg_declaration.
    def visitArg_declaration(self, ctx:CSharpParser.Arg_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#method_invocation.
    def visitMethod_invocation(self, ctx:CSharpParser.Method_invocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#object_creation_expression.
    def visitObject_creation_expression(self, ctx:CSharpParser.Object_creation_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSharpParser#identifier.
    def visitIdentifier(self, ctx:CSharpParser.IdentifierContext):
        return self.visitChildren(ctx)



del CSharpParser