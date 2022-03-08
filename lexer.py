from tokens import Token
from tokens import TokenType

GLOBAL_WHITESPACE = " \n\t"
GLOBAL_DIGITS = "0123456789"

class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        while self.current_char != None:
            if self.current_char in GLOBAL_WHITESPACE:
                self.advance()
            elif self.current_char == "." or self.current_char in GLOBAL_DIGITS:
                yield self.generate_number()
            elif self.current_char == "+":
                yield Token(TokenType.PLUS)
                self.advance()
            elif self.current_char == "-":
                yield Token(TokenType.MINUS)
                self.advance()
            elif self.current_char == "*":
                yield Token(TokenType.MULTIPLY)
                self.advance()
            elif self.current_char == "/":
                yield Token(TokenType.DIVIDE)
                self.advance()
            elif self.current_char == "%":
                yield Token(TokenType.MOD)
                self.advance()
            elif self.current_char == "(":
                yield Token(TokenType.LPAREN)
                self.advance()
            elif self.current_char == ")":
                yield Token(TokenType.RPAREN)
                self.advance()
            else:
                raise Exception(f"Unexpected character: {self.current_char}")
            

    def generate_number(self):
        decimal_ct = 0
        number_str = self.current_char
        self.advance()
        while self.current_char != None and (self.current_char in GLOBAL_DIGITS or self.current_char == "."):
            if self.current_char == ".":
                decimal_ct += 1
                if decimal_ct > 1:
                    break
            number_str += self.current_char
            self.advance()

        if number_str.startswith("."):
            number_str = "0" + number_str
        if number_str.endswith("."):
            number_str += "0"

        return Token(TokenType.NUMBER, float(number_str))
