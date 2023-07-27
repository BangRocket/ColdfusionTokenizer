import re

class CFToken:

  def __init__(self, value, line, col):
    self.value = value
    self.line = line 
    self.col = col

  def __repr__(self):
    return f'{self.__class__.__name__}(value={self.value!r}, line={self.line}, col={self.col})'


class CFTagToken(CFToken):
  
  def __init__(self, value, line, col):
    super().__init__(value, line, col)
    self.name = value[1:-1]


class CFStringToken(CFToken):

  LITERAL = '"literal"'
  SINGLE_QUOTE = "'single quote'"

  def __init__(self, value, line, col):
    super().__init__(value, line, col)
    if value.startswith('"'):
      self.type = self.LITERAL
    else:
      self.type = self.SINGLE_QUOTE


class CFTokenizer:

  TAG_REGEX = re.compile(r'<\/?\w.*?>')
  STRING_REGEX = re.compile(r'(".*?")|(\'.*?\')')

  def __init__(self, code):
    self.code = code
    self.tokens = []

  def tokenize_code(self):
    lines = self.code.split('\n')
    
    for i, line in enumerate(lines):
      self.tokenize_line(line, i+1)

    return self.tokens

  def tokenize_line(self, text, line_num):
    self.tokenize_tags(text, line_num)
    self.tokenize_strings(text, line_num)

  def tokenize_tags(self, text, line):
    for match in self.TAG_REGEX.finditer(text):
      token = CFTagToken(match.group(), line, match.start()+1)  
      self.tokens.append(token)

  def tokenize_strings(self, text, line):
    for match in self.STRING_REGEX.finditer(text):
      token = CFStringToken(match.group(), line, match.start()+1)
      self.tokens.append(token)