import re
from cftoken import CFToken

class CFOperatorToken(CFToken):
    OPERATORS = {'=': 'ASSIGN', '==': 'EQ', '!=': 'NEQ',
                 '<': 'LT', '>': 'GT', '<=': 'LTE', '>=': 'GTE',
                 '&&': 'AND', '||': 'OR', '+': 'ADD', '-': 'SUB',
                 '*': 'MUL', '/': 'DIV'}

    def __init__(self, value, line, col):
        super().__init__(value, line, col)
        self.type = self.OPERATORS.get(value, 'UNKNOWN')