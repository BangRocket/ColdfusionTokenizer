import os
import json
from datetime import datetime
from cfml_tokenizer import CFMLTokenizer

data_dir = 'data'
json_dir = 'json'

if not os.path.exists(json_dir):
    os.makedirs(json_dir)

def tokenize_files():
    files = [f for f in os.listdir(data_dir) if f.endswith('.cfm') or f.endswith('.cfc')]
    
    for file in files:
        filepath = os.path.join(data_dir, file)
        with open(filepath) as f:
            code = f.read()
        
        #print(code[:20])

        print(f"Tokenizing {file}")
        
        tokenizer = CFMLTokenizer(code)
        tokens = tokenizer.tokenize()
        
        for token in tokens:
            print(f"{file} (line {token.line}): {token.value}")
        
        # Output JSON to 'json' subfolder
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        out_file = f'json/tokens_{file}_{now}.json'
        with open(out_file,'w') as f:
            json.dump(tokens, f, indent=4, default=CFMLTokenizer.to_json_serializable,)
        
if __name__ == '__main__':
    tokenize_files()