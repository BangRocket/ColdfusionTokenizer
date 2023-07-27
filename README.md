Here is the README in Markdown syntax:

# cftokenizer.py

## Overview

cftokenizer.py is a Python module for tokenizing ColdFusion code. It can break up ColdFusion tags, strings, and other elements into tokens that can be used for parsing, analyzing, or processing ColdFusion code.

The module provides the following classes:

- **CFToken** - Base token class  
- **CFTagToken** - Tokens for ColdFusion tags
- **CFStringToken** - Tokens for ColdFusion strings
- **CFTokenizer** - Tokenizer class

## Usage

To use the tokenizer:

```python
from cftokenizer import CFTokenizer

code = "<cfset x = 1>"

tokenizer = CFTokenizer(code)
tokens = tokenizer.tokenize_code()

for token in tokens:
  print(token)
```

This will break the code into `CFTagToken` and `CFStringToken` instances. 

The tokens contain the value, line number, and column number where they occurred in the code.

## CFTokenizer

The `CFTokenizer` class handles tokenizing the ColdFusion code.

It takes the source code as a constructor parameter.

The `tokenize_code()` method breaks the code into lines, then calls `tokenize_line()` to generate tokens for each line.

`tokenize_line()` handles finding tags using a regex, and strings using a separate regex. It uses the match positions to determine the line and column numbers.

## CFToken

The `CFToken` base class holds the token value, line number, and column number.

## CFTagToken

The `CFTagToken` subclass holds ColdFusion tag tokens. It parses the tag name from the value.

## CFStringToken  

The `CFStringToken` subclass holds ColdFusion string tokens. It classifies strings as literals or single-quoted.

## Resources

See the [ColdFusion documentation](http://cfdocs.org) for more details on ColdFusion syntax.