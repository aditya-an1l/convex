import regex
import json

class Node:
    def __init__(self):
        self.node = {}
        self.is_end_of_word = False



class Trie:
    def __init__(self):
        self.head = Node()
        # self.HINDI_PATTERN = re.compile(r'[\u0900-\u097F]+', re.UNICODE)
        self.HINDI_PATTERN = regex.compile(r'[\u0900-\u097F\u09E6-\u09EF\s\p{P}]+', regex.UNICODE)



    def insert(self, word):
        if (self.HINDI_PATTERN.fullmatch(word)):
            root = self.head
            for char in word:
                if char not in root.node:
                    root.node[char] = Node()
            
                root = root.node[char]
            root.is_end_of_word = True
            print("Successfully inserted")
            return 

        else:
            print(f"Invalid character {word}")



    def _search(self, word): 
        if (self.HINDI_PATTERN.fullmatch(word)):
            root = self.head
            for char in word:
                if char not in root.node:
                    return None
                root = root.node[char]
            return root

        else:
            print(f"Invalid character {word}")  



    def search_prefix(self, prefix):
        node = self._search(prefix)
        return node is not None
    


    def search_word(self, word):
        node = self._search(word)
        if node is None:
            return False
        return node.is_end_of_word



    def _delete_node(self,word, node, depth):
        if depth == len(word) :
            if not node.is_end_of_word:
                return -1
            node.is_end_of_word = False
            return 0 if len(node.node) == 0 else 1
        
        char = word[depth]
        if char not in node.node:
            return False
        
        status= self._delete_node(word,node.node[char], depth+1)

        if status == -1:
            return -1

        if(status == 0) :
            del node.node[char]
            return 0 if len(node.node) == 0 and not node.is_end_of_word else 1
        return 1



    def delete(self, word):
        if (self.HINDI_PATTERN.fullmatch(word)):
            root = self.head
            result = self._delete_node(word, root,0)
            if result == -1:
                print(f"❌ Word '{word}' not found in the Trie.")
                return False
            else:
                print(f"✅ Word '{word}' successfully deleted/unmarked.")
                return True

        else:
            print(f"Invalid character {word}")
            return False     

    
    def get_dict(self, lang: str)-> dict:
        pack_path = ""

        if(lang.lower() == 'hindi'):
            print('hlo')
            pack_path ="backend/language_packs/hindi_keywords.json"
            
        try:
            with open(pack_path, 'r') as lang_file:
                data = json.load(lang_file)
                print(f"Successfully read JSON data: {type(data)}")
                return data
            
        except FileNotFoundError:
            print(f"The file {pack_path} is not found")
            print(f"Sorry, {lang} lang_pack is currently not available")
        except json.JSONDecodeError:

            print("Error: The file content is not valid JSON.")
        return {}




# trie = Trie()
# trie.insert("जबतक")
# print(trie.search_prefix("जबत"))
# print(trie.search_prefix("जबक"))
# print(trie.search_word("जबतक"))
# trie.delete("जबत")
# trie.delete("जबतक")
# print(trie.search_prefix("जबत"))


trie = Trie()
data = trie.get_dict("hindi")

for key in data.keys():
    trie.insert(key)

print(trie.search_word("जबतक"))



