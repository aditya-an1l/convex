from abc import ABC, abstractmethod
import json
class Abs_Translator(ABC):
    # @abstractmethod
    # def tokenize(code: str) -> list:
    #     tokens= 'hlo'
    #     return tokens

    @abstractmethod
    def is_eng(code: str) -> bool:
        return 
    
    
    @abstractmethod 
    def map_name_token(token: str)-> str:
        changed_token = 'hlo'
        return changed_token 
    
    # @abstractmethod 
    # def guess_original_token(user_token: str)-> str:
    #     predict = 'hlo'
    #     return predict
    
    @abstractmethod 
    def replace_with_crct_token(token: str)-> str:
        replace_token = 'hlo'
        return replace_token
    
    @abstractmethod 
    def convert_token(map_token,original_token )-> str:
        convert = 'hlo'
        return convert
    
    @abstractmethod
    def throw_error():
        return
    
    @abstractmethod
    def is_code_corpus(code: str) -> bool:
        return True
    
    @abstractmethod
    def ask_user(token_to_verify: str) -> str:
        return 

    @abstractmethod
    def untokenize_tokens(token_list: list)-> str:
        return 
    
    # @abstractmethod
    # def get_answer_from_user(token: str) -> str:
    #     response = 'hlo'
    #     return response


class Translator(Abs_Translator):
    def __init__(self, lang: str, code: str):
        self.lang = lang
        self.code = code
        # self.translate_code(code, lang)
        return
    
    '''
    Handle the event when map_name_token() function cant find the right map in language pack
    '''
    def translate_code(self) -> str:
        tokens = self.tokenize_code(self.code)
        '''
        Handle tokens.lang bcoz its directly asking tokens [list] 
        '''
        token_list = tokens.copy()
        if(self.is_eng(tokens.lang)):
            if(self.is_code_corpus(tokens)):
                return self.code
            else:
                for i,token in enumerate(tokens):
                    # Handle the logic for unidentified english keywords
                    if(token.type != 'KeyWord'):
                        pred = self.guess_token(token)
                        response = self.ask_user(pred, predicted=True)
                        token_list.replace(i, response)

        else:
            lang_pack = self.get_dict()
            for i,token in enumerate(tokens):
                if(token.type == 'NAME'):
                    response = self.map_name_token(token, lang_pack)
                    token_list.replace(i,response)

        latest_code = self.untokenize_tokens(token_list)
        return latest_code
    

    def get_dict(self)-> dict:
        pack_path = ""

        if(self.lang == 'Hindi'):
            print('hlo')
            pack_path ="backend/language_packs/hindi.json"
            
        try:
            with open(pack_path, 'r') as lang_file:
                data = json.load(lang_file)
                print(f"Successfully read JSON data: {type(data)}")
                return data
            
        except FileNotFoundError:
            print(f"The file {pack_path} is not found")
            print(f"Sorry, {self.lang} lang_pack is currently not available")
        except json.JSONDecodeError:

            print("Error: The file content is not valid JSON.")

        return {}
    
    def untokenize_tokens(token_list: list)-> str:
        code = 'hlo'
        return code

    def tokenize_code(code: str) -> list:
        tokens= ['hlo']
        return tokens
    '''
    Current approach: Just take the input, and check if it has [a-zA-Z] if yes return is english (BUT IT FAILS IF LANGUAGE IS RELATED TO LATIN, LIKE SPANISH, FRENCH.....)
    '''
    def is_eng(code: str) -> bool:
        return 
    
    def map_name_token(token: str, lang_pack)-> str:
        changed_token = 'hlo'
        return changed_token 
    
    def guess_token(user_token: str)-> str:
        predict = 'hlo'
        return predict
    
    def replace_with_crct_token(token: str)-> str:
        replace_token = 'hlo'
        return replace_token
    
    def convert_token(map_token,original_token )-> str:
        convert = 'hlo'
        return convert

    def throw_error():
        return
    '''
    Current Approach: Make a set of all python keywords => Make set of all words in input => If difference of set gives output, Highlight the output and return
    '''
    def is_code_corpus(code: str) -> bool:
        code 
        return True
    

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

    class ChangedToken:
            def __init__(self, token: str):
                 self.original = token
                 self.changed
                 self.type
                 self.startpoint
                 self.endpoint


python_code = """
def `नमस्ते_दुनिया():
    print("नमस्ते दुनिया!")

def `जोड़(`संख्या१, `संख्या२):
    return संख्या१ + संख्या२

नमस्ते_दुनिया()
परिणाम = जोड़(५, ३)
print(f"जोड़ का परिणाम: {परिणाम}")
"""


trans = Translator('Hindi', python_code)
trans.get_dict()