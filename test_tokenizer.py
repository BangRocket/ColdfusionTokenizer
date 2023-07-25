import unittest
from tokenizer import tokenize

class TokenizerTestCase(unittest.TestCase):
    def test_tokenize_empty_string(self):
        code = ""
        expected_tokens = []
        tokens = tokenize(code)
        self.assertEqual(tokens, expected_tokens)

    def test_tokenize_single_line_comment(self):
        code = "// This is a single line comment"
        expected_tokens = [
            {"type": "comment", "value": "// This is a single line comment"}
        ]
        tokens = tokenize(code)
        self.assertEqual(tokens, expected_tokens)

    def test_tokenize_multi_line_comment(self):
        code = "/* This is a\nmulti-line\ncomment */"
        expected_tokens = [
            {"type": "comment", "value": "/* This is a\nmulti-line\ncomment */"}
        ]
        tokens = tokenize(code)
        self.assertEqual(tokens, expected_tokens)

    def test_tokenize_string_literal(self):
        code = '"This is a string literal"'
        expected_tokens = [
            {"type": "string", "value": '"This is a string literal"'}
        ]
        tokens = tokenize(code)
        self.assertEqual(tokens, expected_tokens)

    def test_tokenize_number_literal(self):
        code = "123.45"
        expected_tokens = [
            {"type": "number", "value": "123.45"}
        ]
        tokens = tokenize(code)
        self.assertEqual(tokens, expected_tokens)

    def test_tokenize_variable_declaration(self):
        code = "var x = 10;"
        expected_tokens = [
            {"type": "keyword", "value": "var"},
            {"type": "identifier", "value": "x"},
            {"type": "operator", "value": "="},
            {"type": "number", "value": "10"},
            {"type": "delimiter", "value": ";"}
        ]
        tokens = tokenize(code)
        self.assertEqual(tokens, expected_tokens)

    def test_tokenize_function_call(self):
        code = "foo(1, 2, 3)"
        expected_tokens = [
            {"type": "identifier", "value": "foo"},
            {"type": "delimiter", "value": "("},
            {"type": "number", "value": "1"},
            {"type": "delimiter", "value": ","},
            {"type": "number", "value": "2"},
            {"type": "delimiter", "value": ","},
            {"type": "number", "value": "3"},
            {"type": "delimiter", "value": ")"}
        ]
        tokens = tokenize(code)
        self.assertEqual(tokens, expected_tokens)

if __name__ == "__main__":
    unittest.main()
