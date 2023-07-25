## Tokenizer for ColdFusion Language Code

### Introduction
In this task, we need to write a tokenizer for the ColdFusion language code using Python. The tokenizer will take a ColdFusion code as input and tokenize it into a sequence of tokens.

### Tokenizer Architecture
The tokenizer will consist of the following main classes and functions:

1. `Token` class: This class represents a token in the ColdFusion code. It will have the following attributes:
   - `type`: The type of the token (e.g., identifier, string, number, operator, etc.).
   - `value`: The value of the token.
   - `line`: The line number where the token appears in the code.
   - `column`: The column number where the token appears in the code.

2. `Tokenizer` class: This class is responsible for tokenizing the ColdFusion code. It will have the following methods:
   - `__init__(self, code: str)`: Initializes the tokenizer with the ColdFusion code.
   - `get_tokens(self) -> List[Token]`: Tokenizes the code and returns a list of tokens.

3. `is_identifier_char(char: str) -> bool`: A helper function that checks whether a character is a valid identifier character.

4. `is_number_char(char: str) -> bool`: A helper function that checks whether a character is a valid number character.

5. `is_string_char(char: str) -> bool`: A helper function that checks whether a character is a valid string character.

6. `is_operator_char(char: str) -> bool`: A helper function that checks whether a character is a valid operator character.

### Tokenizer Implementation
Let's start by implementing the `Token` class:

[token.py]
