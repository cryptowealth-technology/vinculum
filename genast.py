from tokens import TokenType
from nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.advance()

    def raise_error(self):
        raise Exception("Invalid syntax")

    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def parse(self):
        if self.current_token == None:
            return None

        res = self.expr()

        if self.current_token != None:
            self.raise_error()

        return res

    def expr(self):
        res = self.term()

        while self.current_token != None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            if self.current_token.type == TokenType.PLUS:
                self.advance()
                res = AddNode(res, self.term())
            elif self.current_token.type == TokenType.MINUS:
                self.advance()
                res = SubtractNode(res, self.term())

        return res

    def term(self):
        res = self.factor()

        while self.current_token != None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE, TokenType.MOD):
            if self.current_token.type == TokenType.MULTIPLY:
                self.advance()
                res = MultiplyNode(res, self.factor())
            elif self.current_token.type == TokenType.DIVIDE:
                self.advance()
                res = DivideNode(res, self.factor())
            elif self.current_token.type == TokenType.MOD:
                self.advance()
                res = ModuloNode(res, self.factor())

        return res

    def factor(self):
        token = self.current_token

        if token.type == TokenType.LPAREN:
            self.advance()
            res = self.expr()

            if self.current_token.type != TokenType.RPAREN:
                self.raise_error()
            
            self.advance()
            return res

        elif token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value)

        elif token.type == TokenType.PLUS:
            self.advance()
            return PosNode(self.factor())

        elif token.type == TokenType.MINUS:
            self.advance()
            return NegateNode(self.factor())

        self.raise_error()