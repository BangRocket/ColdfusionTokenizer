import re
from cftoken import CFToken

class CFTag(CFToken):
    """Represents start, end tags"""

    TAG_REGEX = re.compile(r'<(/?cf[\w]*)([^>]*)/?>', re.I)

    def __init__(self, value, line, col, is_closing=False, is_self_closing=False):
        super().__init__(value, line, col)
        self.is_closing = is_closing
        self.is_self_closing = is_self_closing

    @staticmethod
    def tokenize_tags(self, text, line_num):
        """Extract tags into tokens"""

        pos = 0
        while pos < len(text):
            match = CFTag.TAG_REGEX.match(text, pos)
            if match is not None: print(match)
            if match:
                tag_name = match.group(1)
                is_closing = tag_name.startswith('/')
                is_self_closing = match.group(2).strip().endswith('/')
                tag_token = CFTag(match.group(0), line_num, match.start(), is_closing, is_self_closing)
                self.tokens.append(tag_token)
                pos = match.end()
            else:
                break

        return self.tokens
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            'is_closing': self.is_closing,
            'is_self_closing': self.is_self_closing,
        })
        return data
