from dataclasses import dataclass
from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    NUMBER = 0
    PLUS = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4
    MOD = 5
    LPAREN = 6
    RPAREN = 7

@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value != None else "")
