from abc import ABC, abstractmethod
import json
import io
import tokenize
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
import re
import keyword

class Abs_Translator(ABC):
    @abstractmethod 
    def map_name_token(token: str)-> str:
        changed_token = 'hlo'
        return changed_token 
    
    
    @abstractmethod
    def throw_error():
        return

    @abstractmethod
    def ask_user(token_to_verify: str) -> str:
        return 


    @abstractmethod
    def untokenize_tokens(token_list: list)-> str:
        return 

    # @abstractmethod 
    # def replace_with_crct_token(token: str)-> str:
    #     replace_token = 'hlo'
    #     return replace_token
    

    # @abstractmethod 
    # def convert_token(map_token,original_token )-> str:
    #     convert = 'hlo'
    #     return convert


    # @abstractmethod
    # def is_code_corpus(code: str) -> bool:
    #     return True
    

    # @abstractmethod
    # def get_answer_from_user(token: str) -> str:
    #     response = 'hlo'
    #     return response



    '''
    Handle the event when map_name_token() function cant find the right map in language pack
    '''


    '''
    #response = self.map_name_token(token, lang_pack) 
    # is useful when we want to use some efficient algorithm in finding the correct map       
    '''    
    

    '''
    Current approach: Just take the input, and check if it has [a-zA-Z] if yes return is english (BUT IT FAILS IF LANGUAGE IS RELATED TO LATIN, LIKE SPANISH, FRENCH.....)

    After tokenization use regex on tokens to identify is_eng and is_Code_corpus
    '''

    '''
    Current Approach: Make a set of all python keywords => Make set of all words in input => If difference of set gives output, Highlight the output and return

    I think this is efficient try this
    '''




class Translator(Abs_Translator):
    def __init__(self, lang: str, code: str):
        self.lang = lang
        self.code = code
        lang_pack = self.get_dict(lang)
        self.latest_code, self.unidentified = self.translate(self.code, lang_pack)
        # self.translate_code(code, lang)
        return
    


    def get_dict(self, lang: str)-> dict:
        pack_path = ""

        if(lang.lower() == 'hindi'):
            print('hlo')
            pack_path ="backend/language_packs/hindi.json"
            
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



    def untokenize_tokens(token_list: list)-> str:
        return tokenize.untokenize(token_list)



    def tokenize_code(code: str) -> list:
        source_stream = io.StringIO(code)
        return tokenize.generate_tokens(source_stream.readline)



    '''
    Handle predicted case
    '''
    def ask_user(self, token_to_verify: str, prediction: bool = False) -> str:
        if(prediction):
            print('Please verify the token')
            print(f'Is it \'\'{token_to_verify}\'\'')
            reply = int(input('If yes select 1 else 0'))
            if(reply):
                return token_to_verify
            else:
                response = self.ask_user(token_to_verify)
                return response
        else:
            self.throw_error()
            response = str(input('Please enter the right token')) 
        return response



    def map_name_token(token: str, lang_pack)-> str:
        changed_token = 'hlo'
        return changed_token
    


    def guess_token(user_token: str)-> str:
        predict = 'hlo'
        return predict 



    def translate(self, source_code: str, lang_pack: dict) -> str :  #also returns a list of unidentified tokens
        """
        Flag to replace the token immediately following a backtick (`) with "transliterated word".
        """
        token_generator = self.tokenize_code(source_code)
        modified_tokens = []

        is_next_name = False 
        unidentified_tokens = []
        for token in token_generator:
            token_type = token.type
            token_string = token.string
            
            # --- State Change Logic ---
            
            if token_string == '`':
                is_next_name = True
                continue 
            
            if token_type == tokenize.NAME:

                if is_next_name:
                    transliterate_string = token_string
                    '''
                    1) try taking each letter in word lies in ascii range of english aphabets
                    2) Use ascii of the corresponding characters range with regex to check if word belong to user mentioned language or not
                    3) Also store if the errors or  unidentified words in a seperate list to throw to user easily
                    '''
                    pattern = r"\b\p{L}+\b"
                    match_result = re.search(pattern, transliterate_string)

                    if(bool(match_result)):
                        new_string = transliterate(transliterate_string, sanscript.DEVANAGARI, sanscript.ITRANS).lower()
                    else:
                        new_string = token_string

                    is_next_name = False
                else :
                    if(keyword.iskeyword(token_string)):
                        new_string = token_string
                    elif token_string in lang_pack:
                        new_string = lang_pack[token_string]
                    else:
                        pred = self.guess_token(token)
                        '''
                        1) It verifies predicted value and also corrects from the users response if the prediction is false
                        2) Use unidentified tokens for correcting and training the model                        
                        '''
                        new_string = self.ask_user(pred, predicted=True)
                        unidentified_tokens.append(token)
            else:
                new_string = token_string

            modified_tokens.append((token_type, new_string))

        reconstructed_code_string = self.untokenize_tokens(modified_tokens)
        return reconstructed_code_string, unidentified_tokens

    def throw_error():
        return






    
    '''
    Removed all the unnecessary code part
        Done check in translate module
    '''
    # def translate_code(self, source_code: str, lang: str) -> str:
    #     Handle tokens.lang bcoz its directly asking tokens [list] 
    #     #implement a class token details wehich have info of is_eng and is_code corpus along with original tokens info
    #             # for i,token in enumerate(tokens):
    #                 # Handle the logic for unidentified english keywords
    #                 # if(token.type != 'KeyWord'):
    #                 #     pred = self.guess_token(token)
    #                 #     response = self.ask_user(pred, predicted=True)


    '''
    Not necessary
    '''  
    # def replace_with_crct_token(token: str)-> str:
    #     replace_token = 'hlo'
    #     return replace_token
    
    '''
    Not necessary
    '''
    # def convert_token(map_token,original_token )-> str:
    #     convert = 'hlo'
    #     return convert


    '''
    Not necessary
    '''
    # def is_code_corpus(code: str) -> bool:
    #     code 
    #     return True
    

    '''
    Not necessary
    '''
    # class ChangedToken:
    #         def __init__(self, token: str):
    #              self.original = token
    #              self.changed
    #              self.type
    #              self.startpoint
    #              self.endpoint




python_code = '''
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



trans = Translator('Hindi', python_code)
trans.get_dict()
trans.latest_code
trans.unidentified