import re
from cftoken import CFToken

class CFKeyword(CFToken):

    STRING_REGEX = re.compile(r'(".*?")|(\'.*?\')')
    LITERAL = 'literal'
    SINGLE_QUOTE = 'single quote'

    def __init__(self, value, line, col):
        super().__init__(value, line, col)
        self.type = self.LITERAL if value.startswith(
            '"') else self.SINGLE_QUOTE
        
    def tokenize_strings(self, text, line):
        for match in CFKeyword.STRING_REGEX.finditer(text):
            token = CFKeyword(match.group(), line, match.start()+1)
            self.tokens.append(token)