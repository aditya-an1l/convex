# ===============================================
# Multilingual to Python Parser
# -----------------------------------------------
# Description   : Translates code written in Hindi (or other supported 
#                 languages) to Python syntax using a JSON keyword map.
# Author(s)     : aditya-an1l, sproutcake23
# Created       : 2025-05-22
# Last Modified : 2025-05-22 19:34 (aditya-an1l)
# Comment       : Supports CLI arguments for input file and language pack.
#                 Use the script as :
#                 $ python parser.py --lang <language> --input <input>
#                 or
#                 $ python parser.py --l <language> --i <input>
#
#                 Eg:
#                 $ python parser.py --lang hindi --input demo/input_hindi.py
#
#                 To know more about usage, execute:
#                 $ python parser.py -h
# ===============================================

import json
import re
import argparse
import os
import sys

class MultilingualToPythonParser:
    def __init__(self, language_pack_path: str):
        """
        Load the language pack JSON file into a keyword map.
        Compiles word-based regex patterns for accurate replacement.
        """
        if not os.path.isfile(language_pack_path):
            raise FileNotFoundError(f"Language pack not found: {language_pack_path}")
        
        with open(language_pack_path, 'r', encoding='utf-8') as f:
            try:
                self.keyword_map = json.load(f)
            except json.JSONDecodeError:
                raise ValueError(f"Invalid JSON in language pack: {language_pack_path}")

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

def main():
    parser = argparse.ArgumentParser(description="Translate multilingual code to Python.")
    parser.add_argument('-l', '--lang', type=str, required=True, help='Language to translate from (e.g., hindi)')
    parser.add_argument('-i', '--input', type=str, required=True, help='Path to the input code file')

    args = parser.parse_args()
    lang = args.lang.lower()
    input_path = args.input

    if not os.path.isfile(input_path):
        print(f"❌ Error: Input file not found: {input_path}")
        sys.exit(1)

    lang_pack_path = f"./language_packs/{lang}.json"

    try:
        translator = MultilingualToPythonParser(lang_pack_path)
    except (FileNotFoundError, ValueError) as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

    with open(input_path, 'r', encoding='utf-8') as file:
        source_code = file.read()

    translated_code = translator.translate_code(source_code)

    print("✅ Translated Python Code:\n")
    print(translated_code)

if __name__ == "__main__":
    main()
