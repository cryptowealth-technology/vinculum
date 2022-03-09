from lexer import Lexer
from genast import Parser
from interpreter import Interpreter

while True:
    try:
        text = input("Vinculum > ")
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        ast = parser.parse()
        if not ast:
            continue
        interpreter = Interpreter()
        value = interpreter.visit(ast)
        print(value)
    except Exception as e:
        print(e)