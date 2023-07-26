from typing import List
from cftoken import CFToken

class Tokenizer:
    def __init__(self, code: str):
        self.code = code
        self.tokens = []

    def get_tokens(self) -> List[CFToken]:
        line = 1
        column = 1

        i = 0
        while i < len(self.code):
            char = self.code[i]

            # Skip whitespace
            if char.isspace():
                if char == '\n':
                    line += 1
                    column = 1
                else:
                    column += 1
                i += 1
                continue

            # Identifier or keyword
            if char.isalpha() or char == '_':
                start = i
                while i < len(self.code) and (self.code[i].isalnum() or self.code[i] == '_'):
                    i += 1
                value = self.code[start:i]
                token_type = 'identifier' if value.isidentifier() else 'keyword'
                self.tokens.append(CFToken(token_type, value, line, column))
                column += i - start
                continue

            # Number
            if char.isdigit():
                start = i
                while i < len(self.code) and self.code[i].isdigit():
                    i += 1
                if i < len(self.code) and self.code[i] == '.':
                    i += 1
                    while i < len(self.code) and self.code[i].isdigit():
                        i += 1
                value = self.code[start:i]
                self.tokens.append(CFToken('number', value, line, column))
                column += i - start
                continue

            # String
            if char == '"' or char == "'":
                start = i
                i += 1
                while i < len(self.code) and self.code[i] != char:
                    i += 1
                if i < len(self.code) and self.code[i] == char:
                    i += 1
                value = self.code[start:i]
                self.tokens.append(CFToken('string', value, line, column))
                column += i - start
                continue

            # Operator
            if char in '+-*/%=&|<>!':
                start = i
                i += 1
                while i < len(self.code) and self.code[i] in '+-*/%=&|<>!':
                    i += 1
                value = self.code[start:i]
                self.tokens.append(CFToken('operator', value, line, column))
                column += i - start
                continue

            # Other characters
            self.tokens.append(CFToken('other', char, line, column))
            column += 1
            i += 1

        return self.tokens