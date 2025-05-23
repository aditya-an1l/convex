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

```sh
python parser.py

```

### 5. 📝 Modify or Add Language Packs

Language packs are stored in `language_packs/<language>.json`.  
You can update or create new ones using the same format.
