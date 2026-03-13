from antlr4 import *
from Expr3Lexer import Expr3Lexer
from Expr3Parser import Expr3Parser

def main():
    while True:
        try:
            text = input("Expr> ")
        except EOFError:
            break
        
        if not text:
            continue

        input_stream = InputStream(text)
        lexer = Expr3Lexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = Expr3Parser(stream)
        
        tree = parser.expr()
        print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()