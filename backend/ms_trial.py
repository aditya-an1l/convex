import io
import tokenize
# import keyword

import json
import re
# import argparse
# import os
# import sys

from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
# from deep_translator import GoogleTranslator


# class Trans():
#     def transliteration():
#         transliterated_word_pairs = {word : transliterate(word, sanscript.DEVANAGARI, sanscript.ITRANS) for word in words}

#     def translation():
        
#     def parserIntegration():

#     def classification():

#     def integration(): "Integrate transliterate and traanslate code"

# Example Python code with valid identifiers (backticks removed)
python_code = """
def `नमस्ते_दुनिया():
    print("नमस्ते दुनिया!")

def `जोड़(`संख्या१, `संख्या२):
    return संख्या१ + संख्या२

नमस्ते_दुनिया()
परिणाम = जोड़(५, ३)
print(f"जोड़ का परिणाम: {परिणाम}")
"""

python_code2 = '''
आयात random

परिभाषा `संख्या_जांच (`संख्या):
    अगर `संख्या > 10:
        वापस सच
    वरना:
        वापस झूठ

`यादृच्छिक_संख्या = random.randint (1 , 20)
छापो (f"यादृच्छिक संख्या है: { `यादृच्छिक_संख्या }")

अगर `संख्या_जांच (`यादृच्छिक_संख्या) है सच:
    छापो ("परिणाम: संख्या 10 से बड़ी है।")
वरना:
    छापो ("परिणाम: संख्या 10 या उससे छोटी है।")

`गिनती = 1
जबतक `गिनती <= 5:
    छापो (f"गिनती चल रही है: { `गिनती }")
    `गिनती = `गिनती + 1

कोशिश:
    `परिणाम = 10 / 0
छोड़कर ZeroDivisionError:
    छापो (" ")
अंततः:
    छापो (" ")
'''


def modify_tokens_efficiently(source_code: str, lang_pack: dict) -> str:
    """
    Efficiently processes a token stream using a generator and a state flag 
    to replace the token immediately following a backtick (`) with "hello".
    """

    source_stream = io.StringIO(source_code)
    token_generator = tokenize.generate_tokens(source_stream.readline)
    
    modified_tokens = []
    
    next_name = False 
    
    for token in token_generator:
        token_type = token.type
        token_string = token.string
        
        # --- State Change Logic ---
        
        if token_string == '`':
            next_name = True
            continue 
        
        if token_type == tokenize.NAME:
            if next_name:
                transliterate_string = token_string
                pattern = r"\b\w+\b"
                match_result = re.search(pattern, transliterate_string)
                if(bool(match_result)):
                    new_string = transliterate(transliterate_string, sanscript.DEVANAGARI, sanscript.ITRANS).lower()
                    print(f"-> Efficiently replaced '{token_string}' with '{new_string}'")
                else:
                    print(token_string)
                    new_string = token_string

                next_name = False
            else :
                # translate the keyword
                if token_string in lang_pack:
                    new_string = lang_pack[token_string]
                else:
                    new_string = token_string
                
        else:
            new_string = token_string

        modified_tokens.append((token_type, new_string))

    # 4. Reconstruct the code
    reconstructed_string = tokenize.untokenize(modified_tokens)
    return reconstructed_string



pack_path ="backend/language_packs/hindi.json"
data = {}
try:
    with open(pack_path, 'r') as lang_file:
        data = json.load(lang_file)
        print(f"Successfully read JSON data: {type(data)}")
    
except FileNotFoundError:
    print(f"The file {pack_path} is not found")
    print(f"Sorry, hindi lang_pack is currently not available")

except json.JSONDecodeError:
    print("Error: The file content is not valid JSON.")

# --- Execution ---

print("## Original Code ##")
print("-" * 50)
print(python_code.strip())

modified_code = modify_tokens_efficiently(python_code2, data)

print("\n## Reconstructed Code (Efficiently Modified) ##")
print("-" * 50)
print(modified_code.strip())


    
#     # Recreate the token tuple using the original type, *new* string, and original metadata
#     # We must use all fields except the string, but untokenize only needs the first two.
#     # To preserve line numbers/positions, we use the original token object structure.
#     modified_tokens.append(tokenize.TokenInfo(
#         type=token.type,
#         string=new_string,
#         start=token.start,
#         end=token.end,
#         line=token.line
#     ))

