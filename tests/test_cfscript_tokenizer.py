# test_cfscript_tokenizer.py

# import unittest
# import sys

# sys.path.append('..')
# from cfscript_tokenizer import CFScriptTokenizer

# class TestCFScriptTokenizer(unittest.TestCase):

#   def test_keyword_token(self):
#     tokenizer = CFScriptTokenizer('if x > 1 then')
#     tokens = tokenizer.tokenize()
#     self.assertIsInstance(tokens[0], CFKeywordToken)

#   def test_function_token(self):
#     tokenizer = CFScriptTokenizer('writeOutput("Hi")')
#     tokens = tokenizer.tokenize()
#     self.assertIsInstance(tokens[0], CFFunctionToken)  

#   def test_variable_token(self):
#     tokenizer = CFScriptTokenizer('x = 10;')
#     tokens = tokenizer.tokenize()
#     self.assertIsInstance(tokens[0], CFVariableToken)

#   def test_string_token(self):
#     tokenizer = CFScriptTokenizer('s = "Hello";')
#     tokens = tokenizer.tokenize()
#     self.assertIsInstance(tokens[2], CFStringToken)

#   def test_operator_token(self):
#     tokenizer = CFScriptTokenizer('x = 1 + 2;')
#     tokens = tokenizer.tokenize()
#     self.assertIsInstance(tokens[2], CFOperatorToken)