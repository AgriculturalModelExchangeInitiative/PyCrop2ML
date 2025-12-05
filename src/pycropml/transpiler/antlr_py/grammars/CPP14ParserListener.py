# Generated from CPP14Parser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CPP14Parser import CPP14Parser
else:
    from CPP14Parser import CPP14Parser

# This class defines a complete listener for a parse tree produced by CPP14Parser.
class CPP14ParserListener(ParseTreeListener):

    # Enter a parse tree produced by CPP14Parser#translationUnit.
    def enterTranslationUnit(self, ctx:CPP14Parser.TranslationUnitContext):
        pass

    # Exit a parse tree produced by CPP14Parser#translationUnit.
    def exitTranslationUnit(self, ctx:CPP14Parser.TranslationUnitContext):
        pass


    # Enter a parse tree produced by CPP14Parser#primaryExpression.
    def enterPrimaryExpression(self, ctx:CPP14Parser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#primaryExpression.
    def exitPrimaryExpression(self, ctx:CPP14Parser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#idExpression.
    def enterIdExpression(self, ctx:CPP14Parser.IdExpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#idExpression.
    def exitIdExpression(self, ctx:CPP14Parser.IdExpressionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#unqualifiedId.
    def enterUnqualifiedId(self, ctx:CPP14Parser.UnqualifiedIdContext):
        pass

    # Exit a parse tree produced by CPP14Parser#unqualifiedId.
    def exitUnqualifiedId(self, ctx:CPP14Parser.UnqualifiedIdContext):
        pass


    # Enter a parse tree produced by CPP14Parser#qualifiedId.
    def enterQualifiedId(self, ctx:CPP14Parser.QualifiedIdContext):
        pass

    # Exit a parse tree produced by CPP14Parser#qualifiedId.
    def exitQualifiedId(self, ctx:CPP14Parser.QualifiedIdContext):
        pass


    # Enter a parse tree produced by CPP14Parser#nestedNameSpecifier.
    def enterNestedNameSpecifier(self, ctx:CPP14Parser.NestedNameSpecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#nestedNameSpecifier.
    def exitNestedNameSpecifier(self, ctx:CPP14Parser.NestedNameSpecifierContext):
        pass


    # Enter a parse tree produced by CPP14Parser#lambdaExpression.
    def enterLambdaExpression(self, ctx:CPP14Parser.LambdaExpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#lambdaExpression.
    def exitLambdaExpression(self, ctx:CPP14Parser.LambdaExpressionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#lambdaIntroducer.
    def enterLambdaIntroducer(self, ctx:CPP14Parser.LambdaIntroducerContext):
        pass

    # Exit a parse tree produced by CPP14Parser#lambdaIntroducer.
    def exitLambdaIntroducer(self, ctx:CPP14Parser.LambdaIntroducerContext):
        pass


    # Enter a parse tree produced by CPP14Parser#lambdaCapture.
    def enterLambdaCapture(self, ctx:CPP14Parser.LambdaCaptureContext):
        pass

    # Exit a parse tree produced by CPP14Parser#lambdaCapture.
    def exitLambdaCapture(self, ctx:CPP14Parser.LambdaCaptureContext):
        pass


    # Enter a parse tree produced by CPP14Parser#captureDefault.
    def enterCaptureDefault(self, ctx:CPP14Parser.CaptureDefaultContext):
        pass

    # Exit a parse tree produced by CPP14Parser#captureDefault.
    def exitCaptureDefault(self, ctx:CPP14Parser.CaptureDefaultContext):
        pass


    # Enter a parse tree produced by CPP14Parser#captureList.
    def enterCaptureList(self, ctx:CPP14Parser.CaptureListContext):
        pass

    # Exit a parse tree produced by CPP14Parser#captureList.
    def exitCaptureList(self, ctx:CPP14Parser.CaptureListContext):
        pass


    # Enter a parse tree produced by CPP14Parser#capture.
    def enterCapture(self, ctx:CPP14Parser.CaptureContext):
        pass

    # Exit a parse tree produced by CPP14Parser#capture.
    def exitCapture(self, ctx:CPP14Parser.CaptureContext):
        pass


    # Enter a parse tree produced by CPP14Parser#simpleCapture.
    def enterSimpleCapture(self, ctx:CPP14Parser.SimpleCaptureContext):
        pass

    # Exit a parse tree produced by CPP14Parser#simpleCapture.
    def exitSimpleCapture(self, ctx:CPP14Parser.SimpleCaptureContext):
        pass


    # Enter a parse tree produced by CPP14Parser#initcapture.
    def enterInitcapture(self, ctx:CPP14Parser.InitcaptureContext):
        pass

    # Exit a parse tree produced by CPP14Parser#initcapture.
    def exitInitcapture(self, ctx:CPP14Parser.InitcaptureContext):
        pass


    # Enter a parse tree produced by CPP14Parser#lambdaDeclarator.
    def enterLambdaDeclarator(self, ctx:CPP14Parser.LambdaDeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#lambdaDeclarator.
    def exitLambdaDeclarator(self, ctx:CPP14Parser.LambdaDeclaratorContext):
        pass


    # Enter a parse tree produced by CPP14Parser#postfixExpression.
    def enterPostfixExpression(self, ctx:CPP14Parser.PostfixExpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#postfixExpression.
    def exitPostfixExpression(self, ctx:CPP14Parser.PostfixExpressionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#typeIdOfTheTypeId.
    def enterTypeIdOfTheTypeId(self, ctx:CPP14Parser.TypeIdOfTheTypeIdContext):
        pass

    # Exit a parse tree produced by CPP14Parser#typeIdOfTheTypeId.
    def exitTypeIdOfTheTypeId(self, ctx:CPP14Parser.TypeIdOfTheTypeIdContext):
        pass


    # Enter a parse tree produced by CPP14Parser#expressionList.
    def enterExpressionList(self, ctx:CPP14Parser.ExpressionListContext):
        pass

    # Exit a parse tree produced by CPP14Parser#expressionList.
    def exitExpressionList(self, ctx:CPP14Parser.ExpressionListContext):
        pass


    # Enter a parse tree produced by CPP14Parser#pseudoDestructorName.
    def enterPseudoDestructorName(self, ctx:CPP14Parser.PseudoDestructorNameContext):
        pass

    # Exit a parse tree produced by CPP14Parser#pseudoDestructorName.
    def exitPseudoDestructorName(self, ctx:CPP14Parser.PseudoDestructorNameContext):
        pass


    # Enter a parse tree produced by CPP14Parser#unaryExpression.
    def enterUnaryExpression(self, ctx:CPP14Parser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#unaryExpression.
    def exitUnaryExpression(self, ctx:CPP14Parser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#unaryOperator.
    def enterUnaryOperator(self, ctx:CPP14Parser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#unaryOperator.
    def exitUnaryOperator(self, ctx:CPP14Parser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by CPP14Parser#newExpression_.
    def enterNewExpression_(self, ctx:CPP14Parser.NewExpression_Context):
        pass

    # Exit a parse tree produced by CPP14Parser#newExpression_.
    def exitNewExpression_(self, ctx:CPP14Parser.NewExpression_Context):
        pass


    # Enter a parse tree produced by CPP14Parser#newPlacement.
    def enterNewPlacement(self, ctx:CPP14Parser.NewPlacementContext):
        pass

    # Exit a parse tree produced by CPP14Parser#newPlacement.
    def exitNewPlacement(self, ctx:CPP14Parser.NewPlacementContext):
        pass


    # Enter a parse tree produced by CPP14Parser#newTypeId.
    def enterNewTypeId(self, ctx:CPP14Parser.NewTypeIdContext):
        pass

    # Exit a parse tree produced by CPP14Parser#newTypeId.
    def exitNewTypeId(self, ctx:CPP14Parser.NewTypeIdContext):
        pass


    # Enter a parse tree produced by CPP14Parser#newDeclarator_.
    def enterNewDeclarator_(self, ctx:CPP14Parser.NewDeclarator_Context):
        pass

    # Exit a parse tree produced by CPP14Parser#newDeclarator_.
    def exitNewDeclarator_(self, ctx:CPP14Parser.NewDeclarator_Context):
        pass


    # Enter a parse tree produced by CPP14Parser#noPointerNewDeclarator.
    def enterNoPointerNewDeclarator(self, ctx:CPP14Parser.NoPointerNewDeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#noPointerNewDeclarator.
    def exitNoPointerNewDeclarator(self, ctx:CPP14Parser.NoPointerNewDeclaratorContext):
        pass


    # Enter a parse tree produced by CPP14Parser#newInitializer_.
    def enterNewInitializer_(self, ctx:CPP14Parser.NewInitializer_Context):
        pass

    # Exit a parse tree produced by CPP14Parser#newInitializer_.
    def exitNewInitializer_(self, ctx:CPP14Parser.NewInitializer_Context):
        pass


    # Enter a parse tree produced by CPP14Parser#deleteExpression.
    def enterDeleteExpression(self, ctx:CPP14Parser.DeleteExpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#deleteExpression.
    def exitDeleteExpression(self, ctx:CPP14Parser.DeleteExpressionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#noExceptExpression.
    def enterNoExceptExpression(self, ctx:CPP14Parser.NoExceptExpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#noExceptExpression.
    def exitNoExceptExpression(self, ctx:CPP14Parser.NoExceptExpressionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#castExpression.
    def enterCastExpression(self, ctx:CPP14Parser.CastExpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#castExpression.
    def exitCastExpression(self, ctx:CPP14Parser.CastExpressionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#pointerMemberExpression.
    def enterPointerMemberExpression(self, ctx:CPP14Parser.PointerMemberExpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#pointerMemberExpression.
    def exitPointerMemberExpression(self, ctx:CPP14Parser.PointerMemberExpressionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:CPP14Parser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:CPP14Parser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#additiveExpression.
    def enterAdditiveExpression(self, ctx:CPP14Parser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#additiveExpression.
    def exitAdditiveExpression(self, ctx:CPP14Parser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#shiftExpression.
    def enterShiftExpression(self, ctx:CPP14Parser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#shiftExpression.
    def exitShiftExpression(self, ctx:CPP14Parser.ShiftExpressionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#shiftOperator.
    def enterShiftOperator(self, ctx:CPP14Parser.ShiftOperatorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#shiftOperator.
    def exitShiftOperator(self, ctx:CPP14Parser.ShiftOperatorContext):
        pass


    # Enter a parse tree produced by CPP14Parser#relationalExpression.
    def enterRelationalExpression(self, ctx:CPP14Parser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#relationalExpression.
    def exitRelationalExpression(self, ctx:CPP14Parser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#equalityExpression.
    def enterEqualityExpression(self, ctx:CPP14Parser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#equalityExpression.
    def exitEqualityExpression(self, ctx:CPP14Parser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#andExpression.
    def enterAndExpression(self, ctx:CPP14Parser.AndExpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#andExpression.
    def exitAndExpression(self, ctx:CPP14Parser.AndExpressionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#exclusiveOrExpression.
    def enterExclusiveOrExpression(self, ctx:CPP14Parser.ExclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#exclusiveOrExpression.
    def exitExclusiveOrExpression(self, ctx:CPP14Parser.ExclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#inclusiveOrExpression.
    def enterInclusiveOrExpression(self, ctx:CPP14Parser.InclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#inclusiveOrExpression.
    def exitInclusiveOrExpression(self, ctx:CPP14Parser.InclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:CPP14Parser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:CPP14Parser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:CPP14Parser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:CPP14Parser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#conditionalExpression.
    def enterConditionalExpression(self, ctx:CPP14Parser.ConditionalExpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#conditionalExpression.
    def exitConditionalExpression(self, ctx:CPP14Parser.ConditionalExpressionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:CPP14Parser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:CPP14Parser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:CPP14Parser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:CPP14Parser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by CPP14Parser#expression.
    def enterExpression(self, ctx:CPP14Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#expression.
    def exitExpression(self, ctx:CPP14Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#constantExpression.
    def enterConstantExpression(self, ctx:CPP14Parser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#constantExpression.
    def exitConstantExpression(self, ctx:CPP14Parser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#statement.
    def enterStatement(self, ctx:CPP14Parser.StatementContext):
        pass

    # Exit a parse tree produced by CPP14Parser#statement.
    def exitStatement(self, ctx:CPP14Parser.StatementContext):
        pass


    # Enter a parse tree produced by CPP14Parser#labeledStatement.
    def enterLabeledStatement(self, ctx:CPP14Parser.LabeledStatementContext):
        pass

    # Exit a parse tree produced by CPP14Parser#labeledStatement.
    def exitLabeledStatement(self, ctx:CPP14Parser.LabeledStatementContext):
        pass


    # Enter a parse tree produced by CPP14Parser#expressionStatement.
    def enterExpressionStatement(self, ctx:CPP14Parser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by CPP14Parser#expressionStatement.
    def exitExpressionStatement(self, ctx:CPP14Parser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by CPP14Parser#compoundStatement.
    def enterCompoundStatement(self, ctx:CPP14Parser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by CPP14Parser#compoundStatement.
    def exitCompoundStatement(self, ctx:CPP14Parser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by CPP14Parser#statementSeq.
    def enterStatementSeq(self, ctx:CPP14Parser.StatementSeqContext):
        pass

    # Exit a parse tree produced by CPP14Parser#statementSeq.
    def exitStatementSeq(self, ctx:CPP14Parser.StatementSeqContext):
        pass


    # Enter a parse tree produced by CPP14Parser#selectionStatement.
    def enterSelectionStatement(self, ctx:CPP14Parser.SelectionStatementContext):
        pass

    # Exit a parse tree produced by CPP14Parser#selectionStatement.
    def exitSelectionStatement(self, ctx:CPP14Parser.SelectionStatementContext):
        pass


    # Enter a parse tree produced by CPP14Parser#condition.
    def enterCondition(self, ctx:CPP14Parser.ConditionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#condition.
    def exitCondition(self, ctx:CPP14Parser.ConditionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#iterationStatement.
    def enterIterationStatement(self, ctx:CPP14Parser.IterationStatementContext):
        pass

    # Exit a parse tree produced by CPP14Parser#iterationStatement.
    def exitIterationStatement(self, ctx:CPP14Parser.IterationStatementContext):
        pass


    # Enter a parse tree produced by CPP14Parser#forInitStatement.
    def enterForInitStatement(self, ctx:CPP14Parser.ForInitStatementContext):
        pass

    # Exit a parse tree produced by CPP14Parser#forInitStatement.
    def exitForInitStatement(self, ctx:CPP14Parser.ForInitStatementContext):
        pass


    # Enter a parse tree produced by CPP14Parser#forRangeDeclaration.
    def enterForRangeDeclaration(self, ctx:CPP14Parser.ForRangeDeclarationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#forRangeDeclaration.
    def exitForRangeDeclaration(self, ctx:CPP14Parser.ForRangeDeclarationContext):
        pass


    # Enter a parse tree produced by CPP14Parser#forRangeInitializer.
    def enterForRangeInitializer(self, ctx:CPP14Parser.ForRangeInitializerContext):
        pass

    # Exit a parse tree produced by CPP14Parser#forRangeInitializer.
    def exitForRangeInitializer(self, ctx:CPP14Parser.ForRangeInitializerContext):
        pass


    # Enter a parse tree produced by CPP14Parser#jumpStatement.
    def enterJumpStatement(self, ctx:CPP14Parser.JumpStatementContext):
        pass

    # Exit a parse tree produced by CPP14Parser#jumpStatement.
    def exitJumpStatement(self, ctx:CPP14Parser.JumpStatementContext):
        pass


    # Enter a parse tree produced by CPP14Parser#declarationStatement.
    def enterDeclarationStatement(self, ctx:CPP14Parser.DeclarationStatementContext):
        pass

    # Exit a parse tree produced by CPP14Parser#declarationStatement.
    def exitDeclarationStatement(self, ctx:CPP14Parser.DeclarationStatementContext):
        pass


    # Enter a parse tree produced by CPP14Parser#declarationseq.
    def enterDeclarationseq(self, ctx:CPP14Parser.DeclarationseqContext):
        pass

    # Exit a parse tree produced by CPP14Parser#declarationseq.
    def exitDeclarationseq(self, ctx:CPP14Parser.DeclarationseqContext):
        pass


    # Enter a parse tree produced by CPP14Parser#declaration.
    def enterDeclaration(self, ctx:CPP14Parser.DeclarationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#declaration.
    def exitDeclaration(self, ctx:CPP14Parser.DeclarationContext):
        pass


    # Enter a parse tree produced by CPP14Parser#blockDeclaration.
    def enterBlockDeclaration(self, ctx:CPP14Parser.BlockDeclarationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#blockDeclaration.
    def exitBlockDeclaration(self, ctx:CPP14Parser.BlockDeclarationContext):
        pass


    # Enter a parse tree produced by CPP14Parser#aliasDeclaration.
    def enterAliasDeclaration(self, ctx:CPP14Parser.AliasDeclarationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#aliasDeclaration.
    def exitAliasDeclaration(self, ctx:CPP14Parser.AliasDeclarationContext):
        pass


    # Enter a parse tree produced by CPP14Parser#simpleDeclaration.
    def enterSimpleDeclaration(self, ctx:CPP14Parser.SimpleDeclarationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#simpleDeclaration.
    def exitSimpleDeclaration(self, ctx:CPP14Parser.SimpleDeclarationContext):
        pass


    # Enter a parse tree produced by CPP14Parser#staticAssertDeclaration.
    def enterStaticAssertDeclaration(self, ctx:CPP14Parser.StaticAssertDeclarationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#staticAssertDeclaration.
    def exitStaticAssertDeclaration(self, ctx:CPP14Parser.StaticAssertDeclarationContext):
        pass


    # Enter a parse tree produced by CPP14Parser#emptyDeclaration_.
    def enterEmptyDeclaration_(self, ctx:CPP14Parser.EmptyDeclaration_Context):
        pass

    # Exit a parse tree produced by CPP14Parser#emptyDeclaration_.
    def exitEmptyDeclaration_(self, ctx:CPP14Parser.EmptyDeclaration_Context):
        pass


    # Enter a parse tree produced by CPP14Parser#attributeDeclaration.
    def enterAttributeDeclaration(self, ctx:CPP14Parser.AttributeDeclarationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#attributeDeclaration.
    def exitAttributeDeclaration(self, ctx:CPP14Parser.AttributeDeclarationContext):
        pass


    # Enter a parse tree produced by CPP14Parser#declSpecifier.
    def enterDeclSpecifier(self, ctx:CPP14Parser.DeclSpecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#declSpecifier.
    def exitDeclSpecifier(self, ctx:CPP14Parser.DeclSpecifierContext):
        pass


    # Enter a parse tree produced by CPP14Parser#declSpecifierSeq.
    def enterDeclSpecifierSeq(self, ctx:CPP14Parser.DeclSpecifierSeqContext):
        pass

    # Exit a parse tree produced by CPP14Parser#declSpecifierSeq.
    def exitDeclSpecifierSeq(self, ctx:CPP14Parser.DeclSpecifierSeqContext):
        pass


    # Enter a parse tree produced by CPP14Parser#storageClassSpecifier.
    def enterStorageClassSpecifier(self, ctx:CPP14Parser.StorageClassSpecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#storageClassSpecifier.
    def exitStorageClassSpecifier(self, ctx:CPP14Parser.StorageClassSpecifierContext):
        pass


    # Enter a parse tree produced by CPP14Parser#functionSpecifier.
    def enterFunctionSpecifier(self, ctx:CPP14Parser.FunctionSpecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#functionSpecifier.
    def exitFunctionSpecifier(self, ctx:CPP14Parser.FunctionSpecifierContext):
        pass


    # Enter a parse tree produced by CPP14Parser#typedefName.
    def enterTypedefName(self, ctx:CPP14Parser.TypedefNameContext):
        pass

    # Exit a parse tree produced by CPP14Parser#typedefName.
    def exitTypedefName(self, ctx:CPP14Parser.TypedefNameContext):
        pass


    # Enter a parse tree produced by CPP14Parser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:CPP14Parser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:CPP14Parser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by CPP14Parser#trailingTypeSpecifier.
    def enterTrailingTypeSpecifier(self, ctx:CPP14Parser.TrailingTypeSpecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#trailingTypeSpecifier.
    def exitTrailingTypeSpecifier(self, ctx:CPP14Parser.TrailingTypeSpecifierContext):
        pass


    # Enter a parse tree produced by CPP14Parser#typeSpecifierSeq.
    def enterTypeSpecifierSeq(self, ctx:CPP14Parser.TypeSpecifierSeqContext):
        pass

    # Exit a parse tree produced by CPP14Parser#typeSpecifierSeq.
    def exitTypeSpecifierSeq(self, ctx:CPP14Parser.TypeSpecifierSeqContext):
        pass


    # Enter a parse tree produced by CPP14Parser#trailingTypeSpecifierSeq.
    def enterTrailingTypeSpecifierSeq(self, ctx:CPP14Parser.TrailingTypeSpecifierSeqContext):
        pass

    # Exit a parse tree produced by CPP14Parser#trailingTypeSpecifierSeq.
    def exitTrailingTypeSpecifierSeq(self, ctx:CPP14Parser.TrailingTypeSpecifierSeqContext):
        pass


    # Enter a parse tree produced by CPP14Parser#simpleTypeLengthModifier.
    def enterSimpleTypeLengthModifier(self, ctx:CPP14Parser.SimpleTypeLengthModifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#simpleTypeLengthModifier.
    def exitSimpleTypeLengthModifier(self, ctx:CPP14Parser.SimpleTypeLengthModifierContext):
        pass


    # Enter a parse tree produced by CPP14Parser#simpleTypeSignednessModifier.
    def enterSimpleTypeSignednessModifier(self, ctx:CPP14Parser.SimpleTypeSignednessModifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#simpleTypeSignednessModifier.
    def exitSimpleTypeSignednessModifier(self, ctx:CPP14Parser.SimpleTypeSignednessModifierContext):
        pass


    # Enter a parse tree produced by CPP14Parser#simpleTypeSpecifier.
    def enterSimpleTypeSpecifier(self, ctx:CPP14Parser.SimpleTypeSpecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#simpleTypeSpecifier.
    def exitSimpleTypeSpecifier(self, ctx:CPP14Parser.SimpleTypeSpecifierContext):
        pass


    # Enter a parse tree produced by CPP14Parser#theTypeName.
    def enterTheTypeName(self, ctx:CPP14Parser.TheTypeNameContext):
        pass

    # Exit a parse tree produced by CPP14Parser#theTypeName.
    def exitTheTypeName(self, ctx:CPP14Parser.TheTypeNameContext):
        pass


    # Enter a parse tree produced by CPP14Parser#decltypeSpecifier.
    def enterDecltypeSpecifier(self, ctx:CPP14Parser.DecltypeSpecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#decltypeSpecifier.
    def exitDecltypeSpecifier(self, ctx:CPP14Parser.DecltypeSpecifierContext):
        pass


    # Enter a parse tree produced by CPP14Parser#elaboratedTypeSpecifier.
    def enterElaboratedTypeSpecifier(self, ctx:CPP14Parser.ElaboratedTypeSpecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#elaboratedTypeSpecifier.
    def exitElaboratedTypeSpecifier(self, ctx:CPP14Parser.ElaboratedTypeSpecifierContext):
        pass


    # Enter a parse tree produced by CPP14Parser#enumName.
    def enterEnumName(self, ctx:CPP14Parser.EnumNameContext):
        pass

    # Exit a parse tree produced by CPP14Parser#enumName.
    def exitEnumName(self, ctx:CPP14Parser.EnumNameContext):
        pass


    # Enter a parse tree produced by CPP14Parser#enumSpecifier.
    def enterEnumSpecifier(self, ctx:CPP14Parser.EnumSpecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#enumSpecifier.
    def exitEnumSpecifier(self, ctx:CPP14Parser.EnumSpecifierContext):
        pass


    # Enter a parse tree produced by CPP14Parser#enumHead.
    def enterEnumHead(self, ctx:CPP14Parser.EnumHeadContext):
        pass

    # Exit a parse tree produced by CPP14Parser#enumHead.
    def exitEnumHead(self, ctx:CPP14Parser.EnumHeadContext):
        pass


    # Enter a parse tree produced by CPP14Parser#opaqueEnumDeclaration.
    def enterOpaqueEnumDeclaration(self, ctx:CPP14Parser.OpaqueEnumDeclarationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#opaqueEnumDeclaration.
    def exitOpaqueEnumDeclaration(self, ctx:CPP14Parser.OpaqueEnumDeclarationContext):
        pass


    # Enter a parse tree produced by CPP14Parser#enumkey.
    def enterEnumkey(self, ctx:CPP14Parser.EnumkeyContext):
        pass

    # Exit a parse tree produced by CPP14Parser#enumkey.
    def exitEnumkey(self, ctx:CPP14Parser.EnumkeyContext):
        pass


    # Enter a parse tree produced by CPP14Parser#enumbase.
    def enterEnumbase(self, ctx:CPP14Parser.EnumbaseContext):
        pass

    # Exit a parse tree produced by CPP14Parser#enumbase.
    def exitEnumbase(self, ctx:CPP14Parser.EnumbaseContext):
        pass


    # Enter a parse tree produced by CPP14Parser#enumeratorList.
    def enterEnumeratorList(self, ctx:CPP14Parser.EnumeratorListContext):
        pass

    # Exit a parse tree produced by CPP14Parser#enumeratorList.
    def exitEnumeratorList(self, ctx:CPP14Parser.EnumeratorListContext):
        pass


    # Enter a parse tree produced by CPP14Parser#enumeratorDefinition.
    def enterEnumeratorDefinition(self, ctx:CPP14Parser.EnumeratorDefinitionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#enumeratorDefinition.
    def exitEnumeratorDefinition(self, ctx:CPP14Parser.EnumeratorDefinitionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#enumerator.
    def enterEnumerator(self, ctx:CPP14Parser.EnumeratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#enumerator.
    def exitEnumerator(self, ctx:CPP14Parser.EnumeratorContext):
        pass


    # Enter a parse tree produced by CPP14Parser#namespaceName.
    def enterNamespaceName(self, ctx:CPP14Parser.NamespaceNameContext):
        pass

    # Exit a parse tree produced by CPP14Parser#namespaceName.
    def exitNamespaceName(self, ctx:CPP14Parser.NamespaceNameContext):
        pass


    # Enter a parse tree produced by CPP14Parser#originalNamespaceName.
    def enterOriginalNamespaceName(self, ctx:CPP14Parser.OriginalNamespaceNameContext):
        pass

    # Exit a parse tree produced by CPP14Parser#originalNamespaceName.
    def exitOriginalNamespaceName(self, ctx:CPP14Parser.OriginalNamespaceNameContext):
        pass


    # Enter a parse tree produced by CPP14Parser#namespaceDefinition.
    def enterNamespaceDefinition(self, ctx:CPP14Parser.NamespaceDefinitionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#namespaceDefinition.
    def exitNamespaceDefinition(self, ctx:CPP14Parser.NamespaceDefinitionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#namespaceAlias.
    def enterNamespaceAlias(self, ctx:CPP14Parser.NamespaceAliasContext):
        pass

    # Exit a parse tree produced by CPP14Parser#namespaceAlias.
    def exitNamespaceAlias(self, ctx:CPP14Parser.NamespaceAliasContext):
        pass


    # Enter a parse tree produced by CPP14Parser#namespaceAliasDefinition.
    def enterNamespaceAliasDefinition(self, ctx:CPP14Parser.NamespaceAliasDefinitionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#namespaceAliasDefinition.
    def exitNamespaceAliasDefinition(self, ctx:CPP14Parser.NamespaceAliasDefinitionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#qualifiednamespacespecifier.
    def enterQualifiednamespacespecifier(self, ctx:CPP14Parser.QualifiednamespacespecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#qualifiednamespacespecifier.
    def exitQualifiednamespacespecifier(self, ctx:CPP14Parser.QualifiednamespacespecifierContext):
        pass


    # Enter a parse tree produced by CPP14Parser#usingDeclaration.
    def enterUsingDeclaration(self, ctx:CPP14Parser.UsingDeclarationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#usingDeclaration.
    def exitUsingDeclaration(self, ctx:CPP14Parser.UsingDeclarationContext):
        pass


    # Enter a parse tree produced by CPP14Parser#usingDirective.
    def enterUsingDirective(self, ctx:CPP14Parser.UsingDirectiveContext):
        pass

    # Exit a parse tree produced by CPP14Parser#usingDirective.
    def exitUsingDirective(self, ctx:CPP14Parser.UsingDirectiveContext):
        pass


    # Enter a parse tree produced by CPP14Parser#asmDefinition.
    def enterAsmDefinition(self, ctx:CPP14Parser.AsmDefinitionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#asmDefinition.
    def exitAsmDefinition(self, ctx:CPP14Parser.AsmDefinitionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#linkageSpecification.
    def enterLinkageSpecification(self, ctx:CPP14Parser.LinkageSpecificationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#linkageSpecification.
    def exitLinkageSpecification(self, ctx:CPP14Parser.LinkageSpecificationContext):
        pass


    # Enter a parse tree produced by CPP14Parser#attributeSpecifierSeq.
    def enterAttributeSpecifierSeq(self, ctx:CPP14Parser.AttributeSpecifierSeqContext):
        pass

    # Exit a parse tree produced by CPP14Parser#attributeSpecifierSeq.
    def exitAttributeSpecifierSeq(self, ctx:CPP14Parser.AttributeSpecifierSeqContext):
        pass


    # Enter a parse tree produced by CPP14Parser#attributeSpecifier.
    def enterAttributeSpecifier(self, ctx:CPP14Parser.AttributeSpecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#attributeSpecifier.
    def exitAttributeSpecifier(self, ctx:CPP14Parser.AttributeSpecifierContext):
        pass


    # Enter a parse tree produced by CPP14Parser#alignmentspecifier.
    def enterAlignmentspecifier(self, ctx:CPP14Parser.AlignmentspecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#alignmentspecifier.
    def exitAlignmentspecifier(self, ctx:CPP14Parser.AlignmentspecifierContext):
        pass


    # Enter a parse tree produced by CPP14Parser#attributeList.
    def enterAttributeList(self, ctx:CPP14Parser.AttributeListContext):
        pass

    # Exit a parse tree produced by CPP14Parser#attributeList.
    def exitAttributeList(self, ctx:CPP14Parser.AttributeListContext):
        pass


    # Enter a parse tree produced by CPP14Parser#attribute.
    def enterAttribute(self, ctx:CPP14Parser.AttributeContext):
        pass

    # Exit a parse tree produced by CPP14Parser#attribute.
    def exitAttribute(self, ctx:CPP14Parser.AttributeContext):
        pass


    # Enter a parse tree produced by CPP14Parser#attributeNamespace.
    def enterAttributeNamespace(self, ctx:CPP14Parser.AttributeNamespaceContext):
        pass

    # Exit a parse tree produced by CPP14Parser#attributeNamespace.
    def exitAttributeNamespace(self, ctx:CPP14Parser.AttributeNamespaceContext):
        pass


    # Enter a parse tree produced by CPP14Parser#attributeArgumentClause.
    def enterAttributeArgumentClause(self, ctx:CPP14Parser.AttributeArgumentClauseContext):
        pass

    # Exit a parse tree produced by CPP14Parser#attributeArgumentClause.
    def exitAttributeArgumentClause(self, ctx:CPP14Parser.AttributeArgumentClauseContext):
        pass


    # Enter a parse tree produced by CPP14Parser#balancedTokenSeq.
    def enterBalancedTokenSeq(self, ctx:CPP14Parser.BalancedTokenSeqContext):
        pass

    # Exit a parse tree produced by CPP14Parser#balancedTokenSeq.
    def exitBalancedTokenSeq(self, ctx:CPP14Parser.BalancedTokenSeqContext):
        pass


    # Enter a parse tree produced by CPP14Parser#balancedtoken.
    def enterBalancedtoken(self, ctx:CPP14Parser.BalancedtokenContext):
        pass

    # Exit a parse tree produced by CPP14Parser#balancedtoken.
    def exitBalancedtoken(self, ctx:CPP14Parser.BalancedtokenContext):
        pass


    # Enter a parse tree produced by CPP14Parser#initDeclaratorList.
    def enterInitDeclaratorList(self, ctx:CPP14Parser.InitDeclaratorListContext):
        pass

    # Exit a parse tree produced by CPP14Parser#initDeclaratorList.
    def exitInitDeclaratorList(self, ctx:CPP14Parser.InitDeclaratorListContext):
        pass


    # Enter a parse tree produced by CPP14Parser#initDeclarator.
    def enterInitDeclarator(self, ctx:CPP14Parser.InitDeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#initDeclarator.
    def exitInitDeclarator(self, ctx:CPP14Parser.InitDeclaratorContext):
        pass


    # Enter a parse tree produced by CPP14Parser#declarator.
    def enterDeclarator(self, ctx:CPP14Parser.DeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#declarator.
    def exitDeclarator(self, ctx:CPP14Parser.DeclaratorContext):
        pass


    # Enter a parse tree produced by CPP14Parser#pointerDeclarator.
    def enterPointerDeclarator(self, ctx:CPP14Parser.PointerDeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#pointerDeclarator.
    def exitPointerDeclarator(self, ctx:CPP14Parser.PointerDeclaratorContext):
        pass


    # Enter a parse tree produced by CPP14Parser#noPointerDeclarator.
    def enterNoPointerDeclarator(self, ctx:CPP14Parser.NoPointerDeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#noPointerDeclarator.
    def exitNoPointerDeclarator(self, ctx:CPP14Parser.NoPointerDeclaratorContext):
        pass


    # Enter a parse tree produced by CPP14Parser#parametersAndQualifiers.
    def enterParametersAndQualifiers(self, ctx:CPP14Parser.ParametersAndQualifiersContext):
        pass

    # Exit a parse tree produced by CPP14Parser#parametersAndQualifiers.
    def exitParametersAndQualifiers(self, ctx:CPP14Parser.ParametersAndQualifiersContext):
        pass


    # Enter a parse tree produced by CPP14Parser#trailingReturnType.
    def enterTrailingReturnType(self, ctx:CPP14Parser.TrailingReturnTypeContext):
        pass

    # Exit a parse tree produced by CPP14Parser#trailingReturnType.
    def exitTrailingReturnType(self, ctx:CPP14Parser.TrailingReturnTypeContext):
        pass


    # Enter a parse tree produced by CPP14Parser#pointerOperator.
    def enterPointerOperator(self, ctx:CPP14Parser.PointerOperatorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#pointerOperator.
    def exitPointerOperator(self, ctx:CPP14Parser.PointerOperatorContext):
        pass


    # Enter a parse tree produced by CPP14Parser#cvqualifierseq.
    def enterCvqualifierseq(self, ctx:CPP14Parser.CvqualifierseqContext):
        pass

    # Exit a parse tree produced by CPP14Parser#cvqualifierseq.
    def exitCvqualifierseq(self, ctx:CPP14Parser.CvqualifierseqContext):
        pass


    # Enter a parse tree produced by CPP14Parser#cvQualifier.
    def enterCvQualifier(self, ctx:CPP14Parser.CvQualifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#cvQualifier.
    def exitCvQualifier(self, ctx:CPP14Parser.CvQualifierContext):
        pass


    # Enter a parse tree produced by CPP14Parser#refqualifier.
    def enterRefqualifier(self, ctx:CPP14Parser.RefqualifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#refqualifier.
    def exitRefqualifier(self, ctx:CPP14Parser.RefqualifierContext):
        pass


    # Enter a parse tree produced by CPP14Parser#declaratorid.
    def enterDeclaratorid(self, ctx:CPP14Parser.DeclaratoridContext):
        pass

    # Exit a parse tree produced by CPP14Parser#declaratorid.
    def exitDeclaratorid(self, ctx:CPP14Parser.DeclaratoridContext):
        pass


    # Enter a parse tree produced by CPP14Parser#theTypeId.
    def enterTheTypeId(self, ctx:CPP14Parser.TheTypeIdContext):
        pass

    # Exit a parse tree produced by CPP14Parser#theTypeId.
    def exitTheTypeId(self, ctx:CPP14Parser.TheTypeIdContext):
        pass


    # Enter a parse tree produced by CPP14Parser#abstractDeclarator.
    def enterAbstractDeclarator(self, ctx:CPP14Parser.AbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#abstractDeclarator.
    def exitAbstractDeclarator(self, ctx:CPP14Parser.AbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by CPP14Parser#pointerAbstractDeclarator.
    def enterPointerAbstractDeclarator(self, ctx:CPP14Parser.PointerAbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#pointerAbstractDeclarator.
    def exitPointerAbstractDeclarator(self, ctx:CPP14Parser.PointerAbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by CPP14Parser#noPointerAbstractDeclarator.
    def enterNoPointerAbstractDeclarator(self, ctx:CPP14Parser.NoPointerAbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#noPointerAbstractDeclarator.
    def exitNoPointerAbstractDeclarator(self, ctx:CPP14Parser.NoPointerAbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by CPP14Parser#abstractPackDeclarator.
    def enterAbstractPackDeclarator(self, ctx:CPP14Parser.AbstractPackDeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#abstractPackDeclarator.
    def exitAbstractPackDeclarator(self, ctx:CPP14Parser.AbstractPackDeclaratorContext):
        pass


    # Enter a parse tree produced by CPP14Parser#noPointerAbstractPackDeclarator.
    def enterNoPointerAbstractPackDeclarator(self, ctx:CPP14Parser.NoPointerAbstractPackDeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#noPointerAbstractPackDeclarator.
    def exitNoPointerAbstractPackDeclarator(self, ctx:CPP14Parser.NoPointerAbstractPackDeclaratorContext):
        pass


    # Enter a parse tree produced by CPP14Parser#parameterDeclarationClause.
    def enterParameterDeclarationClause(self, ctx:CPP14Parser.ParameterDeclarationClauseContext):
        pass

    # Exit a parse tree produced by CPP14Parser#parameterDeclarationClause.
    def exitParameterDeclarationClause(self, ctx:CPP14Parser.ParameterDeclarationClauseContext):
        pass


    # Enter a parse tree produced by CPP14Parser#parameterDeclarationList.
    def enterParameterDeclarationList(self, ctx:CPP14Parser.ParameterDeclarationListContext):
        pass

    # Exit a parse tree produced by CPP14Parser#parameterDeclarationList.
    def exitParameterDeclarationList(self, ctx:CPP14Parser.ParameterDeclarationListContext):
        pass


    # Enter a parse tree produced by CPP14Parser#parameterDeclaration.
    def enterParameterDeclaration(self, ctx:CPP14Parser.ParameterDeclarationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#parameterDeclaration.
    def exitParameterDeclaration(self, ctx:CPP14Parser.ParameterDeclarationContext):
        pass


    # Enter a parse tree produced by CPP14Parser#functionDefinition.
    def enterFunctionDefinition(self, ctx:CPP14Parser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#functionDefinition.
    def exitFunctionDefinition(self, ctx:CPP14Parser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#functionBody.
    def enterFunctionBody(self, ctx:CPP14Parser.FunctionBodyContext):
        pass

    # Exit a parse tree produced by CPP14Parser#functionBody.
    def exitFunctionBody(self, ctx:CPP14Parser.FunctionBodyContext):
        pass


    # Enter a parse tree produced by CPP14Parser#initializer.
    def enterInitializer(self, ctx:CPP14Parser.InitializerContext):
        pass

    # Exit a parse tree produced by CPP14Parser#initializer.
    def exitInitializer(self, ctx:CPP14Parser.InitializerContext):
        pass


    # Enter a parse tree produced by CPP14Parser#braceOrEqualInitializer.
    def enterBraceOrEqualInitializer(self, ctx:CPP14Parser.BraceOrEqualInitializerContext):
        pass

    # Exit a parse tree produced by CPP14Parser#braceOrEqualInitializer.
    def exitBraceOrEqualInitializer(self, ctx:CPP14Parser.BraceOrEqualInitializerContext):
        pass


    # Enter a parse tree produced by CPP14Parser#initializerClause.
    def enterInitializerClause(self, ctx:CPP14Parser.InitializerClauseContext):
        pass

    # Exit a parse tree produced by CPP14Parser#initializerClause.
    def exitInitializerClause(self, ctx:CPP14Parser.InitializerClauseContext):
        pass


    # Enter a parse tree produced by CPP14Parser#initializerList.
    def enterInitializerList(self, ctx:CPP14Parser.InitializerListContext):
        pass

    # Exit a parse tree produced by CPP14Parser#initializerList.
    def exitInitializerList(self, ctx:CPP14Parser.InitializerListContext):
        pass


    # Enter a parse tree produced by CPP14Parser#bracedInitList.
    def enterBracedInitList(self, ctx:CPP14Parser.BracedInitListContext):
        pass

    # Exit a parse tree produced by CPP14Parser#bracedInitList.
    def exitBracedInitList(self, ctx:CPP14Parser.BracedInitListContext):
        pass


    # Enter a parse tree produced by CPP14Parser#className.
    def enterClassName(self, ctx:CPP14Parser.ClassNameContext):
        pass

    # Exit a parse tree produced by CPP14Parser#className.
    def exitClassName(self, ctx:CPP14Parser.ClassNameContext):
        pass


    # Enter a parse tree produced by CPP14Parser#classSpecifier.
    def enterClassSpecifier(self, ctx:CPP14Parser.ClassSpecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#classSpecifier.
    def exitClassSpecifier(self, ctx:CPP14Parser.ClassSpecifierContext):
        pass


    # Enter a parse tree produced by CPP14Parser#classHead.
    def enterClassHead(self, ctx:CPP14Parser.ClassHeadContext):
        pass

    # Exit a parse tree produced by CPP14Parser#classHead.
    def exitClassHead(self, ctx:CPP14Parser.ClassHeadContext):
        pass


    # Enter a parse tree produced by CPP14Parser#classHeadName.
    def enterClassHeadName(self, ctx:CPP14Parser.ClassHeadNameContext):
        pass

    # Exit a parse tree produced by CPP14Parser#classHeadName.
    def exitClassHeadName(self, ctx:CPP14Parser.ClassHeadNameContext):
        pass


    # Enter a parse tree produced by CPP14Parser#classVirtSpecifier.
    def enterClassVirtSpecifier(self, ctx:CPP14Parser.ClassVirtSpecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#classVirtSpecifier.
    def exitClassVirtSpecifier(self, ctx:CPP14Parser.ClassVirtSpecifierContext):
        pass


    # Enter a parse tree produced by CPP14Parser#classKey.
    def enterClassKey(self, ctx:CPP14Parser.ClassKeyContext):
        pass

    # Exit a parse tree produced by CPP14Parser#classKey.
    def exitClassKey(self, ctx:CPP14Parser.ClassKeyContext):
        pass


    # Enter a parse tree produced by CPP14Parser#memberSpecification.
    def enterMemberSpecification(self, ctx:CPP14Parser.MemberSpecificationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#memberSpecification.
    def exitMemberSpecification(self, ctx:CPP14Parser.MemberSpecificationContext):
        pass


    # Enter a parse tree produced by CPP14Parser#memberdeclaration.
    def enterMemberdeclaration(self, ctx:CPP14Parser.MemberdeclarationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#memberdeclaration.
    def exitMemberdeclaration(self, ctx:CPP14Parser.MemberdeclarationContext):
        pass


    # Enter a parse tree produced by CPP14Parser#memberDeclaratorList.
    def enterMemberDeclaratorList(self, ctx:CPP14Parser.MemberDeclaratorListContext):
        pass

    # Exit a parse tree produced by CPP14Parser#memberDeclaratorList.
    def exitMemberDeclaratorList(self, ctx:CPP14Parser.MemberDeclaratorListContext):
        pass


    # Enter a parse tree produced by CPP14Parser#memberDeclarator.
    def enterMemberDeclarator(self, ctx:CPP14Parser.MemberDeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#memberDeclarator.
    def exitMemberDeclarator(self, ctx:CPP14Parser.MemberDeclaratorContext):
        pass


    # Enter a parse tree produced by CPP14Parser#virtualSpecifierSeq.
    def enterVirtualSpecifierSeq(self, ctx:CPP14Parser.VirtualSpecifierSeqContext):
        pass

    # Exit a parse tree produced by CPP14Parser#virtualSpecifierSeq.
    def exitVirtualSpecifierSeq(self, ctx:CPP14Parser.VirtualSpecifierSeqContext):
        pass


    # Enter a parse tree produced by CPP14Parser#virtualSpecifier.
    def enterVirtualSpecifier(self, ctx:CPP14Parser.VirtualSpecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#virtualSpecifier.
    def exitVirtualSpecifier(self, ctx:CPP14Parser.VirtualSpecifierContext):
        pass


    # Enter a parse tree produced by CPP14Parser#pureSpecifier.
    def enterPureSpecifier(self, ctx:CPP14Parser.PureSpecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#pureSpecifier.
    def exitPureSpecifier(self, ctx:CPP14Parser.PureSpecifierContext):
        pass


    # Enter a parse tree produced by CPP14Parser#baseClause.
    def enterBaseClause(self, ctx:CPP14Parser.BaseClauseContext):
        pass

    # Exit a parse tree produced by CPP14Parser#baseClause.
    def exitBaseClause(self, ctx:CPP14Parser.BaseClauseContext):
        pass


    # Enter a parse tree produced by CPP14Parser#baseSpecifierList.
    def enterBaseSpecifierList(self, ctx:CPP14Parser.BaseSpecifierListContext):
        pass

    # Exit a parse tree produced by CPP14Parser#baseSpecifierList.
    def exitBaseSpecifierList(self, ctx:CPP14Parser.BaseSpecifierListContext):
        pass


    # Enter a parse tree produced by CPP14Parser#baseSpecifier.
    def enterBaseSpecifier(self, ctx:CPP14Parser.BaseSpecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#baseSpecifier.
    def exitBaseSpecifier(self, ctx:CPP14Parser.BaseSpecifierContext):
        pass


    # Enter a parse tree produced by CPP14Parser#classOrDeclType.
    def enterClassOrDeclType(self, ctx:CPP14Parser.ClassOrDeclTypeContext):
        pass

    # Exit a parse tree produced by CPP14Parser#classOrDeclType.
    def exitClassOrDeclType(self, ctx:CPP14Parser.ClassOrDeclTypeContext):
        pass


    # Enter a parse tree produced by CPP14Parser#baseTypeSpecifier.
    def enterBaseTypeSpecifier(self, ctx:CPP14Parser.BaseTypeSpecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#baseTypeSpecifier.
    def exitBaseTypeSpecifier(self, ctx:CPP14Parser.BaseTypeSpecifierContext):
        pass


    # Enter a parse tree produced by CPP14Parser#accessSpecifier.
    def enterAccessSpecifier(self, ctx:CPP14Parser.AccessSpecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#accessSpecifier.
    def exitAccessSpecifier(self, ctx:CPP14Parser.AccessSpecifierContext):
        pass


    # Enter a parse tree produced by CPP14Parser#conversionFunctionId.
    def enterConversionFunctionId(self, ctx:CPP14Parser.ConversionFunctionIdContext):
        pass

    # Exit a parse tree produced by CPP14Parser#conversionFunctionId.
    def exitConversionFunctionId(self, ctx:CPP14Parser.ConversionFunctionIdContext):
        pass


    # Enter a parse tree produced by CPP14Parser#conversionTypeId.
    def enterConversionTypeId(self, ctx:CPP14Parser.ConversionTypeIdContext):
        pass

    # Exit a parse tree produced by CPP14Parser#conversionTypeId.
    def exitConversionTypeId(self, ctx:CPP14Parser.ConversionTypeIdContext):
        pass


    # Enter a parse tree produced by CPP14Parser#conversionDeclarator.
    def enterConversionDeclarator(self, ctx:CPP14Parser.ConversionDeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#conversionDeclarator.
    def exitConversionDeclarator(self, ctx:CPP14Parser.ConversionDeclaratorContext):
        pass


    # Enter a parse tree produced by CPP14Parser#constructorInitializer.
    def enterConstructorInitializer(self, ctx:CPP14Parser.ConstructorInitializerContext):
        pass

    # Exit a parse tree produced by CPP14Parser#constructorInitializer.
    def exitConstructorInitializer(self, ctx:CPP14Parser.ConstructorInitializerContext):
        pass


    # Enter a parse tree produced by CPP14Parser#memInitializerList.
    def enterMemInitializerList(self, ctx:CPP14Parser.MemInitializerListContext):
        pass

    # Exit a parse tree produced by CPP14Parser#memInitializerList.
    def exitMemInitializerList(self, ctx:CPP14Parser.MemInitializerListContext):
        pass


    # Enter a parse tree produced by CPP14Parser#memInitializer.
    def enterMemInitializer(self, ctx:CPP14Parser.MemInitializerContext):
        pass

    # Exit a parse tree produced by CPP14Parser#memInitializer.
    def exitMemInitializer(self, ctx:CPP14Parser.MemInitializerContext):
        pass


    # Enter a parse tree produced by CPP14Parser#meminitializerid.
    def enterMeminitializerid(self, ctx:CPP14Parser.MeminitializeridContext):
        pass

    # Exit a parse tree produced by CPP14Parser#meminitializerid.
    def exitMeminitializerid(self, ctx:CPP14Parser.MeminitializeridContext):
        pass


    # Enter a parse tree produced by CPP14Parser#operatorFunctionId.
    def enterOperatorFunctionId(self, ctx:CPP14Parser.OperatorFunctionIdContext):
        pass

    # Exit a parse tree produced by CPP14Parser#operatorFunctionId.
    def exitOperatorFunctionId(self, ctx:CPP14Parser.OperatorFunctionIdContext):
        pass


    # Enter a parse tree produced by CPP14Parser#literalOperatorId.
    def enterLiteralOperatorId(self, ctx:CPP14Parser.LiteralOperatorIdContext):
        pass

    # Exit a parse tree produced by CPP14Parser#literalOperatorId.
    def exitLiteralOperatorId(self, ctx:CPP14Parser.LiteralOperatorIdContext):
        pass


    # Enter a parse tree produced by CPP14Parser#templateDeclaration.
    def enterTemplateDeclaration(self, ctx:CPP14Parser.TemplateDeclarationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#templateDeclaration.
    def exitTemplateDeclaration(self, ctx:CPP14Parser.TemplateDeclarationContext):
        pass


    # Enter a parse tree produced by CPP14Parser#templateparameterList.
    def enterTemplateparameterList(self, ctx:CPP14Parser.TemplateparameterListContext):
        pass

    # Exit a parse tree produced by CPP14Parser#templateparameterList.
    def exitTemplateparameterList(self, ctx:CPP14Parser.TemplateparameterListContext):
        pass


    # Enter a parse tree produced by CPP14Parser#templateParameter.
    def enterTemplateParameter(self, ctx:CPP14Parser.TemplateParameterContext):
        pass

    # Exit a parse tree produced by CPP14Parser#templateParameter.
    def exitTemplateParameter(self, ctx:CPP14Parser.TemplateParameterContext):
        pass


    # Enter a parse tree produced by CPP14Parser#typeParameter.
    def enterTypeParameter(self, ctx:CPP14Parser.TypeParameterContext):
        pass

    # Exit a parse tree produced by CPP14Parser#typeParameter.
    def exitTypeParameter(self, ctx:CPP14Parser.TypeParameterContext):
        pass


    # Enter a parse tree produced by CPP14Parser#simpleTemplateId.
    def enterSimpleTemplateId(self, ctx:CPP14Parser.SimpleTemplateIdContext):
        pass

    # Exit a parse tree produced by CPP14Parser#simpleTemplateId.
    def exitSimpleTemplateId(self, ctx:CPP14Parser.SimpleTemplateIdContext):
        pass


    # Enter a parse tree produced by CPP14Parser#templateId.
    def enterTemplateId(self, ctx:CPP14Parser.TemplateIdContext):
        pass

    # Exit a parse tree produced by CPP14Parser#templateId.
    def exitTemplateId(self, ctx:CPP14Parser.TemplateIdContext):
        pass


    # Enter a parse tree produced by CPP14Parser#templateName.
    def enterTemplateName(self, ctx:CPP14Parser.TemplateNameContext):
        pass

    # Exit a parse tree produced by CPP14Parser#templateName.
    def exitTemplateName(self, ctx:CPP14Parser.TemplateNameContext):
        pass


    # Enter a parse tree produced by CPP14Parser#templateArgumentList.
    def enterTemplateArgumentList(self, ctx:CPP14Parser.TemplateArgumentListContext):
        pass

    # Exit a parse tree produced by CPP14Parser#templateArgumentList.
    def exitTemplateArgumentList(self, ctx:CPP14Parser.TemplateArgumentListContext):
        pass


    # Enter a parse tree produced by CPP14Parser#templateArgument.
    def enterTemplateArgument(self, ctx:CPP14Parser.TemplateArgumentContext):
        pass

    # Exit a parse tree produced by CPP14Parser#templateArgument.
    def exitTemplateArgument(self, ctx:CPP14Parser.TemplateArgumentContext):
        pass


    # Enter a parse tree produced by CPP14Parser#typeNameSpecifier.
    def enterTypeNameSpecifier(self, ctx:CPP14Parser.TypeNameSpecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#typeNameSpecifier.
    def exitTypeNameSpecifier(self, ctx:CPP14Parser.TypeNameSpecifierContext):
        pass


    # Enter a parse tree produced by CPP14Parser#explicitInstantiation.
    def enterExplicitInstantiation(self, ctx:CPP14Parser.ExplicitInstantiationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#explicitInstantiation.
    def exitExplicitInstantiation(self, ctx:CPP14Parser.ExplicitInstantiationContext):
        pass


    # Enter a parse tree produced by CPP14Parser#explicitSpecialization.
    def enterExplicitSpecialization(self, ctx:CPP14Parser.ExplicitSpecializationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#explicitSpecialization.
    def exitExplicitSpecialization(self, ctx:CPP14Parser.ExplicitSpecializationContext):
        pass


    # Enter a parse tree produced by CPP14Parser#tryBlock.
    def enterTryBlock(self, ctx:CPP14Parser.TryBlockContext):
        pass

    # Exit a parse tree produced by CPP14Parser#tryBlock.
    def exitTryBlock(self, ctx:CPP14Parser.TryBlockContext):
        pass


    # Enter a parse tree produced by CPP14Parser#functionTryBlock.
    def enterFunctionTryBlock(self, ctx:CPP14Parser.FunctionTryBlockContext):
        pass

    # Exit a parse tree produced by CPP14Parser#functionTryBlock.
    def exitFunctionTryBlock(self, ctx:CPP14Parser.FunctionTryBlockContext):
        pass


    # Enter a parse tree produced by CPP14Parser#handlerSeq.
    def enterHandlerSeq(self, ctx:CPP14Parser.HandlerSeqContext):
        pass

    # Exit a parse tree produced by CPP14Parser#handlerSeq.
    def exitHandlerSeq(self, ctx:CPP14Parser.HandlerSeqContext):
        pass


    # Enter a parse tree produced by CPP14Parser#handler.
    def enterHandler(self, ctx:CPP14Parser.HandlerContext):
        pass

    # Exit a parse tree produced by CPP14Parser#handler.
    def exitHandler(self, ctx:CPP14Parser.HandlerContext):
        pass


    # Enter a parse tree produced by CPP14Parser#exceptionDeclaration.
    def enterExceptionDeclaration(self, ctx:CPP14Parser.ExceptionDeclarationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#exceptionDeclaration.
    def exitExceptionDeclaration(self, ctx:CPP14Parser.ExceptionDeclarationContext):
        pass


    # Enter a parse tree produced by CPP14Parser#throwExpression.
    def enterThrowExpression(self, ctx:CPP14Parser.ThrowExpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#throwExpression.
    def exitThrowExpression(self, ctx:CPP14Parser.ThrowExpressionContext):
        pass


    # Enter a parse tree produced by CPP14Parser#exceptionSpecification.
    def enterExceptionSpecification(self, ctx:CPP14Parser.ExceptionSpecificationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#exceptionSpecification.
    def exitExceptionSpecification(self, ctx:CPP14Parser.ExceptionSpecificationContext):
        pass


    # Enter a parse tree produced by CPP14Parser#dynamicExceptionSpecification.
    def enterDynamicExceptionSpecification(self, ctx:CPP14Parser.DynamicExceptionSpecificationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#dynamicExceptionSpecification.
    def exitDynamicExceptionSpecification(self, ctx:CPP14Parser.DynamicExceptionSpecificationContext):
        pass


    # Enter a parse tree produced by CPP14Parser#typeIdList.
    def enterTypeIdList(self, ctx:CPP14Parser.TypeIdListContext):
        pass

    # Exit a parse tree produced by CPP14Parser#typeIdList.
    def exitTypeIdList(self, ctx:CPP14Parser.TypeIdListContext):
        pass


    # Enter a parse tree produced by CPP14Parser#noeExceptSpecification.
    def enterNoeExceptSpecification(self, ctx:CPP14Parser.NoeExceptSpecificationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#noeExceptSpecification.
    def exitNoeExceptSpecification(self, ctx:CPP14Parser.NoeExceptSpecificationContext):
        pass


    # Enter a parse tree produced by CPP14Parser#theOperator.
    def enterTheOperator(self, ctx:CPP14Parser.TheOperatorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#theOperator.
    def exitTheOperator(self, ctx:CPP14Parser.TheOperatorContext):
        pass


    # Enter a parse tree produced by CPP14Parser#literal.
    def enterLiteral(self, ctx:CPP14Parser.LiteralContext):
        pass

    # Exit a parse tree produced by CPP14Parser#literal.
    def exitLiteral(self, ctx:CPP14Parser.LiteralContext):
        pass



del CPP14Parser