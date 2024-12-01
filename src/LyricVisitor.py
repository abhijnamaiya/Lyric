# Generated from Lyric.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LyricParser import LyricParser
else:
    from LyricParser import LyricParser

# This class defines a complete generic visitor for a parse tree produced by LyricParser.


class LyricVisitor(ParseTreeVisitor):

    def __init__(self):
        self.symbol_table = {}
        pass

    def debug_symbol_table(self):
        print("symbol_table: ", self.symbol_table)

    # Visit a parse tree produced by LyricParser#program.
    def visitProgram(self, ctx: LyricParser.ProgramContext):
        self.visit(ctx.stmtlists())

    # Visit a parse tree produced by LyricParser#stmtlists.
    def visitStmtlists(self, ctx: LyricParser.StmtlistsContext):
        if (ctx.stmt()):
            self.visit(ctx.stmtlists())
            self.visit(ctx.stmt())

    # Visit a parse tree produced by LyricParser#stmt.
    def visitStmt(self, ctx: LyricParser.StmtContext):
        if (ctx.expr()):
            self.visit(ctx.expr())
        elif (ctx.dec_stmt()):
            self.visit(ctx.dec_stmt())
        elif (ctx.loop_stmt()):
            self.visit(ctx.loop_stmt())
        elif (ctx.repeat_stmt()):
            self.visit(ctx.repeat_stmt())
        elif (ctx.check_stmt()):
            self.visit(ctx.check_stmt())
        elif (ctx.stmtlists()):
            self.visit(ctx.stmtlists())
        else:
            if (ctx.getChild(0).getText() == "release "):
                if (ctx.num()):
                    print(self.visit(ctx.num()))
                elif (ctx.STRING()):
                    print(ctx.STRING())
                elif (ctx.IDENT()):
                    ident = ctx.IDENT().getText()
                    if (ident.startswith("\"")):
                        print(ident[1: -1])
                    else:
                        print(self.getIdent(ident))

    # Visit a parse tree produced by LyricParser#expr.

    def visitExpr(self, ctx: LyricParser.ExprContext):
        if (ctx.assign_expr()):
            return self.visit(ctx.assign_expr())
        elif (ctx.math_expr()):
            return self.visit(ctx.math_expr())
        elif (ctx.cpr_expr()):
            return self.visit(ctx.cpr_expr())
        return ctx.getChild(0).getText()

    # Visit a parse tree produced by LyricParser#dec_stmt.

    def visitDec_stmt(self, ctx: LyricParser.Dec_stmtContext):
        varType = ""
        default = 0
        match(ctx.getChild(0).getText()):
            case 'num ':
                varType = "num"
                default = 0
            case 'bool ':
                varType = "bool"
                default = False
            case 'str ':
                varType = "str"
                default = ""
            case _:
                print("ERROR")

        name = ""
        if ctx.assign_expr():
            name = ctx.assign_expr().getChild(1).getText()
            self.symbol_table[name] = (varType, default)
            self.visit(ctx.assign_expr())
        else:
            name = ctx.getChild(1).getText()
            self.symbol_table[name] = (varType, default)

    # Visit a parse tree produced by LyricParser#assign_expr.
    def visitAssign_expr(self, ctx: LyricParser.Assign_exprContext):
        name = ctx.getChild(1).getText()
        value = self.visit(ctx.expr())
        (varType, old) = self.symbol_table[name]

        match varType:
            case "num":
                value = int(value)
            case "bool":
                match value:
                    case "yeah":
                        value = True
                    case "nah":
                        value = False
                    case _:
                        value = False
            case "str":
                value = value[1: -1]
                pass

        self.symbol_table[name] = (varType, value)

    # Visit a parse tree produced by LyricParser#math_expr.

    def visitMath_expr(self, ctx: LyricParser.Math_exprContext):
        if (ctx.getChild(1)):
            match ctx.getChild(1).getText():
                case '+':
                    return self.visit(ctx.math_expr()) + self.visit(ctx.math_term())
                case '-':
                    return self.visit(ctx.math_expr()) - self.visit(ctx.math_term())
        else:
            return self.visit(ctx.math_term())

    # Visit a parse tree produced by LyricParser#math_term.

    def visitMath_term(self, ctx: LyricParser.Math_termContext):
        if (ctx.getChild(1)):
            match ctx.getChild(1).getText():
                case '*':
                    return self.visit(ctx.math_term()) * self.visit(ctx.math_factor())
                case '/':
                    return self.visit(ctx.math_term()) / self.visit(ctx.math_factor())
                case k:
                    print(k)
        else:
            return self.visit(ctx.math_factor())

    # Visit a parse tree produced by LyricParser#math_factor.
    def visitMath_factor(self, ctx: LyricParser.Math_factorContext):
        if (ctx.num()):
            return self.visit(ctx.num())
        elif (ctx.math_expr()):
            return self.visit(ctx.math_expr())
        else:
            return self.getIdent(ctx.getChild(0).getText())

    # Visit a parse tree produced by LyricParser#loop_stmt.
    def visitLoop_stmt(self, ctx: LyricParser.Loop_stmtContext):
        while (self.visit(ctx.expr())):
            self.visit(ctx.stmt())

    # Visit a parse tree produced by LyricParser#repeat_stmt.
    def visitRepeat_stmt(self, ctx: LyricParser.Repeat_stmtContext):
        val = self.visit(ctx.expr())
        for i in range(val):
            self.visit(ctx.stmt())

    # Visit a parse tree produced by LyricParser#check_stmt.
    def visitCheck_stmt(self, ctx: LyricParser.Check_stmtContext):

        if self.visit(ctx.expr()):
            self.visit(ctx.stmt())
        else:
            else_stmt = ctx.else_stmt()
            if (else_stmt):
                self.visit(else_stmt)

    # Visit a parse tree produced by LyricParser#else_stmt.
    def visitElse_stmt(self, ctx: LyricParser.Else_stmtContext):
        self.visit(ctx.stmt())

    # Visit a parse tree produced by LyricParser#cpr_expr.
    def visitCpr_expr(self, ctx: LyricParser.Cpr_exprContext):
        terms = ctx.cpr_term()
        a = self.visit(terms[0])
        b = self.visit(terms[1])
        match (ctx.CPR_SYMBOL().getText()):
            case "<":
                return a < b
            case "<=":
                return a <= b
            case ">":
                return a > b
            case ">=":
                return a >= b
            case "==":
                return a == b

    # Visit a parse tree produced by LyricParser#cpr_term.

    def visitCpr_term(self, ctx: LyricParser.Cpr_termContext):
        if (ctx.num()):
            return self.visit(ctx.num())
        elif (ctx.math_expr()):
            return self.visit(ctx.math_expr())
        return self.getIdent(ctx.getChild(0).getText())

    # Visit a parse tree produced by LyricParser#num.
    def visitNum(self, ctx: LyricParser.NumContext):
        return int(ctx.getText())

    def getIdent(self, ident):
        return self.symbol_table[ident][1]


del LyricParser
