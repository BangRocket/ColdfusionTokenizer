### TODOs for improving the CFML tokenizer:

- [ ] Support multiline strings 
- [ ] Support nested tags
- [ ] Extract tag attributes into separate tokens
- [ ] Extract tag body content into separate tokens  
- [ ] Recognize common CF constructs as separate tokens
- [ ] Tokenize `<cfscript>` blocks into individual tokens
- [ ] Extract comments into separate tokens
- [ ] Recognize more operators as separate tokens
- [ ] Retain whitespace as tokens 
- [ ] Support preprocessor directives like `<cfinclude>`
- [ ] Use more robust regexes
- [ ] Add recursive parsing where needed
- [ ] Improve awareness of CFML syntax