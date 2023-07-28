import os
import json
from cfml_tokenizer import CFMLTokenizer

DATA_DIR = 'data'

def tokenize_files():
    
    tokens = {}
    
    for filename in os.listdir(DATA_DIR):
        if filename.endswith('.cfm'):
            
            with open(os.path.join(DATA_DIR, filename)) as f:
                code = f.read()
                
            tokenizer = CFMLTokenizer(code)
            tokens[filename] = tokenizer.tokenize()
            
    # Write tokens to JSON file
    with open('tokens.json', 'w') as f:
        json.dump(tokens, f, indent=4)
        
if __name__ == '__main__':
    tokenize_files()