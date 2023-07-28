### Tokenizer Improvements TODO
- [ ] Support multiline strings
- [ ] Support nested tags  
- [ ] Extract tag attributes 
- [ ] Extract tag body content
- [ ] Recognize common CF constructs  
- [ ] Tokenize `<cfscript>` blocks
- [ ] Extract comments
- [ ] Recognize more operators
- [ ] Retain whitespace  
- [ ] Support preprocessor directives
- [ ] Use more robust regexes
- [ ] Add recursive parsing 
- [ ] Improve CFML syntax awareness
- [ ] Properly tokenize to clean token stream

- [ ] Distinguish between HTML and CFML tags
- [ ] Handle self-closing tags properly
- [ ] Track open CF tags separately from HTML
- [ ] Validate only CF tags are closed

- [ ] Support complex CF tags like `<cfloop>`, `<cfif>`, etc
- [ ] Handle `<cfquery>` tags appropriately
- [ ] Process contents of `<cfoutput>` correctly
- [ ] Parse `<cfsavecontent>` bodies into tokens
- [ ] Deal with `<cfinclude>` and `<cfmodule>` tags

- [ ] Tokenize CF expressions correctly
- [ ] Support string concatenation and interpolation  
- [ ] Handle complex functions like `ArrayNew()`, `StructNew()` etc.
- [ ] Process ColdFusion variables properly
- [ ] Parse comment syntax consistently 

- [ ] Preserve formatting and whitespace 
- [ ] Track token start and end indexes 
- [ ] Maintain origin file and line info
- [ ] Category tokens into a hierarchy
- [ ] Build an appropriate AST from tokens

- [ ] Write tests for all major use cases
- [ ] Measure performance on large codebases 
- [ ] Improve speed and lower memory usage