import unittest
from cftokenizer import CFTokenizer, CFTagToken

class TestCFTokenizer(unittest.TestCase):

  def test_tokenize_with_html(self):
    code = """
<html>
<body>

<cfset x = 1>

<p>Hello World</p>

<cfif x GT 10>
  <cfloop index="i" from="1" to="10">
    <cfoutput>#i#</cfoutput>
  </cfloop> 
</cfif>

<cffunction name="test">
  <cfargument name="x" type="numeric">
  <cfreturn x * 2>  
</cffunction>

<script>
  console.log("JS code");
</script>

"String" 'String'

</body>
</html>
"""

    tokenizer = CFTokenizer(code)
    tokens = tokenizer.tokenize_code()

    self.assertGreater(len(tokens), 20)
    
    self.assertIsInstance(tokens[0], CFTagToken) 
    self.assertEqual(tokens[0].name, "html")

    self.assertEqual(tokens[3].value, "<p>Hello World</p>")

    self.assertIsInstance(tokens[7], CFTagToken)
    self.assertEqual(tokens[7].name, "cfif")

    self.assertIsInstance(tokens[-4], CFTagToken)
    self.assertEqual(tokens[-4].name, "script")

    self.assertEqual(tokens[-2].value, '"String"')

if __name__ == '__main__':
    unittest.main()