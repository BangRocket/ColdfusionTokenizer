"""
CFMLTokenizer - Tokenizer for ColdFusion Markup Language code 

Tokens CFML code by extracting tags, strings, keywords, 
functions, script blocks etc into a token object model.

Provides nested tag support by tracking open tags during
tokenization.

"""

import re
import sys
sys.path.append('tokens/')

from cftoken import CFToken
from cftag import CFTag as CFTag
from collections import deque

class CFMLTokenizer:

    def __init__(self, code):
        self.code = code
        self.tokens = []

    def tokenize(self):
        """Tokenize entire code by line"""
        lines = self.code.split('\n')

        for line_num, line in enumerate(lines, start=1):
            self.tokenize_line(line, line_num)

        return self.tokens

    def tokenize_line(self, text, line_num):
        """Tokenize a single line of code"""

        # Tokenize parts of CFML syntax
        CFTag.tokenize_tags(self, text, line_num)
        #self.tokenize_strings(text, line_num)
        #self.tokenize_keywords(text, line_num)
        #self.tokenize_functions(text, line_num)
        #self.tokenize_script(text, line_num)

    def to_json_serializable(obj):
        if isinstance(obj, (CFToken, CFTag)):
            return obj.to_dict()
        raise TypeError(f'Type {type(obj)} not serializable')
