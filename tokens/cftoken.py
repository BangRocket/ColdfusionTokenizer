class CFToken:
    """Base token class with value, line and column"""

    def __init__(self, value, line, col):
        self.value = value
        self.line = line
        self.col = col

    def __repr__(self):
        return f'{self.__class__.__name__}(value={self.value!r}, line={self.line}, col={self.col})'
    
    def to_dict(self):
        return {
            'value': self.value,
            'line': self.line,
            'col': self.col,
        }
    