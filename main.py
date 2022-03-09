from lexer import Lexer
from genast import Parser

while True:
    text = input("Vinculum > ")
    lexer = Lexer(text)
    tokens = lexer.generate_tokens()
    parser = Parser(tokens)
    ast = parser.parse()
    print(ast)