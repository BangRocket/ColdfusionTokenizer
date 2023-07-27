# test_cfml_tokenizer.py

import unittest
import sys

sys.path.append('..')

from cfml_tokenizer import CFMLTokenizer, CFTagToken, CFStringToken, CFKeywordToken, CFFunctionToken, CFScriptToken, CFOperatorToken

class TestCFMLTokenizer(unittest.TestCase):

  def test_tag_token(self):
    tokenizer = CFMLTokenizer('<cfset foo="bar">')
    tokens = tokenizer.tokenize()
    self.assertEqual(len(tokens), 3)
    self.assertIsInstance(tokens[0], CFTagToken)

  def test_string_token(self):  
    tokenizer = CFMLTokenizer('<cfset foo="bar">')
    tokens = tokenizer.tokenize()
    self.assertIsInstance(tokens[1], CFStringToken)
  
  def test_keyword_token(self):
    tokenizer = CFMLTokenizer('if x > 1 then')
    tokens = tokenizer.tokenize()
    self.assertIsInstance(tokens[0], CFKeywordToken)
  
  def test_function_token(self):
    tokenizer = CFMLTokenizer('writeOutput("Hi")')
    tokens = tokenizer.tokenize()
    self.assertIsInstance(tokens[0], CFFunctionToken)

  def test_script_token(self):
    tokenizer = CFMLTokenizer('<cfscript>foo = 1;</cfscript>')
    tokens = tokenizer.tokenize()
    self.assertIsInstance(tokens[0], CFScriptToken)