# ===============================================
# Multilingual to Python Translator
# -----------------------------------------------
# Description   : Executes Python code from a file safely,
#                 capturing stdout and stderr.
# Author(s)     : aditya-an1l
# Created       : 2025-05-26
# Last Modified : 2025-05-26 01:46 (aditya-an1l)
# Comment       : The code read from an input file containing 
#                 the python code. This input file, for now, is
#                 placed in `./parsed_code/` directory
#
#                 Use the script as :
#                 $ python translator.py -i <the_parsed_code>.py
#                 $ python translator.py -i parsed_code/parsed.py
# ===============================================

import io
import argparse
import contextlib
import traceback
import os


def execute_python_code(code: str) -> dict:
    """
    Executes Python code and captures stdout or runtime errors.

    Returns:
        dict with success flag, output, and error
    """
    stdout = io.StringIO()

    try:
        with contextlib.redirect_stdout(stdout):
            exec(code, {})
        return {
            "success": True,
            "output": stdout.getvalue().strip(),
            "error": None
        }
    except Exception:
        return {
            "success": False,
            "output": stdout.getvalue().strip(),
            "error": traceback.format_exc()
        }


def main():
    parser = argparse.ArgumentParser(
        description="Translate and execute parsed Python code from a file."
    )
    parser.add_argument(
        "-i", "--input", type=str, required=True,
        help="Path to the input .py file"
    )
    args = parser.parse_args()

    input_file = args.input

    if not os.path.exists(input_file):
        print(f" Error: Input file '{input_file}' not found.")
        return

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            code = f.read()
    except Exception as e:
        print(f" Failed to read file: {e}")
        return

    result = execute_python_code(code)

    # TODO:We can make the output as a JSON containing the output
    # other parameters (execution time, errors, file info, etc.)
    if result["success"]:
        print("✅ Output:\n" + "="*20 + "\n " + result["output"])
    else:
        print("❌ Error Trace:\n" + result["error"])
        print("="*5)


if __name__ == "__main__":
    main()
