## 🚧 Backend

You're currently viewing the development branch for the **Convex** Project.

> **Branch:** `7/core/add-parser-logic`

**Current Goal**: Initial support for translating code written in Hindi (and soon other languages) into valid Python syntax using a rule-based parser.


## 🛠️ Setup Instructions

Follow these steps to run the parser locally:

### 1. 📥 Clone the Repository & Switch to This Branch

```sh
git clone https://github.com/aditya-an1l/convex.git
cd convex
git checkout 

```

### 2. 🐍 Create a Python Virtual Environment

```sh
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```

### 3. 📦 Install Dependencies

```sh
pip install -r requirements.txt

```

### 4. ▶️ Run the Parser

This parser translates code written in an Indian language (e.g., Hindi) into valid Python syntax using a language-specific keyword map.

#### ✅ Syntax

```sh
python parser.py --lang <language> --input <input_file>

```

or using shorthand flags:

```sh
python parser.py -l <language> -i <input_file>

```

For example:

```sh
python parser.py --lang hindi --input demo/input_hindi.py

```

or

```sh
python parser.py -l hindi -i demo/input_hindi.py

```

#### 🧠 What the input file should look like

It should contain code written in your selected language (e.g., Hindi), using keywords defined in the corresponding language pack:

```py
अगर x > 0:
    छापो("सकारात्मक संख्या")

```

#### 🆘 View Help

To see all options and usage:

```sh
python parser.py --help

```

You’ll get an output like:

```txt
usage: parser.py [-h] -l LANG -i INPUT

Translate multilingual code to Python.

options:
  -h, --help            show this help message and exit
  -l LANG, --lang LANG  Language to translate from (e.g., hindi)
  -i INPUT, --input INPUT
                        Path to the input code file

```

#### ⚠️ Before You Run

Make sure:

-   ✅ The corresponding language pack file (like `language_packs/hindi.json`) exists.
    
-   ✅ The input file is present and correctly encoded (UTF-8 recommended).
    
-   ✅ Python 3 is installed (`python --version` should be 3.x).
    


### 5. 📝 Modify or Add Language Packs

Language packs are stored in `language_packs/<language>.json`.  
You can update or create new ones using the same format.
