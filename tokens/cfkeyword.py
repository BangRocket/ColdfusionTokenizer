import re
from cftoken import CFToken

class CFKeyword(CFToken):   
    KEYWORDS = ['if', 'else', 'while', 'for', 'function',
                'component', 'property', 'return', 'include',
                'import', 'param', 'try', 'catch', 'interface',
                'implements']
    
    def __init__(self, value, line, col):
        super().__init__(value, line, col)
        self.keyword = value if value in self.KEYWORDS else None

    def __str__(self):
        return f'CFKeywordToken({self.keyword})' if self.keyword else 'CFKeywordToken(UNKNOWN)'
    
    def tokenize_keywords(self, text, line):
        for word in CFKeyword.KEYWORDS:
            for match in re.finditer(rf'\\b{word}\\b', text):
                token = CFKeyword(word, line, match.start()+1)
                self.tokens.append(token)