import sys
import re
from antlr4 import *
from antlr4.InputStream import InputStream
from antlr4.tree.Trees import Trees
from lyric.LyricLexer import LyricLexer
from lyric.LyricParser import LyricParser
from lyric.LyricVisitor import LyricVisitor

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    file_name = sys.argv[1].rsplit('.', 1)[0]
    lexer = LyricLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = LyricParser(token_stream, file_name)
    tree = parser.program()

    visitor = LyricVisitor()
    visitor.visit(tree)
    visitor.debug_symbol_table()
