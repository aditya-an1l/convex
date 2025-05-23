# ===============================================
# Hindi to Python Parser
# -----------------------------------------------
# Description   : Translates code written in Hindi to 
#                 Python syntax.
# Author(s)     : aditya-an1l,sproutcake23
# Created       : 2025-05-22
# Last Modified : 2025-05-22 18:10 (sproutcake23)
# Comment       : improve robustness of the model
# ===============================================

import json
import re

class MultilingualToPythonParser:
    def __init__(self, language_pack_path: str):
        """
        Load the language pack JSON file into a keyword map.
        Compiles word-based regex patterns for accurate replacement.
        """
        with open(language_pack_path, 'r', encoding='utf-8') as f:
            self.keyword_map = json.load(f)

        # pre-compile patterns, might be a plus for performance
        self.patterns = {
            re.compile(rf"(?<!\w){re.escape(k)}(?!\w)"): v
            for k, v in self.keyword_map.items()
        }

    def translate_line(self, line: str) -> str:
        """
        Translates a single line by replacing language-specific keywords 
        with their corresponding Python equivalents.
        """
        translated = line
        for pattern, replacement in self.patterns.items():
            translated = pattern.sub(replacement, translated)
        return translated

    def translate_code(self, code: str) -> str:
        """
        Translates an entire code block line-by-line from the source 
        language to Python syntax.
        """
        lines = code.strip().split("\n")
        return "\n".join(self.translate_line(line) for line in lines)


if __name__ == "__main__":
    # initialise a parser with a Hindi language pack
    parser = MultilingualToPythonParser("./language_packs/hindi.json")

    # sample hindi code that is fed as an input code
    hindi_code = """
अगर x > 0:
    छापो("सकारात्मक संख्या")
"""

    # translate and print the resulting python code
    translated_code = parser.translate_code(hindi_code)
    print("Translated Python Code:\n")
    print(translated_code)
