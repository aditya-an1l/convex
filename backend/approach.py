from abc import ABC, abstractmethod
class Abs_Translator(ABC):
    @abstractmethod
    def tokenize(code: str) -> list:
        tokens= 'hlo'
        return tokens

    @abstractmethod
    def is_eng(code: str) -> bool:
        return 
    
    
    @abstractmethod 
    def map_name_token(token: str)-> str:
        changed_token = 'hlo'
        return changed_token 
    
    @abstractmethod 
    def guess_original_token(user_token: str)-> str:
        predict = 'hlo'
        return predict
    
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


class Translator(Abs_Translator):
    def __init__(self, code, lang):
        self
        self.translate_code(code)
    
'''
Handle the event when map_name_token() function cant find the right map in language pack
'''
    def translate_code(self, code: str, lang: str) -> str:
        tokens = self.tokenize_code(code)
        if(self.is_eng(tokens.lang)):
            print('hlo')
        else:
            lang_pack = self.get_dict(lang)
            token_list = tokens.copy()
            for i,token in enumerate(tokens):
                if(token.type == 'NAME'):
                    token = self.map_name_token(token)
                    token_list.replace(i,token)
            modified_code = self.untokenize_tokens(token_list)
        return code
    
    def get_dict(lang: str)-> dict:
        lang_pack = "hlo"
        return lang_pack


    def tokenize_code(code: str) -> list:
        tokens= ['hlo']
        return tokens

    def is_eng(code: str) -> bool:
        return 
    
    def map_name_token(token: str)-> str:
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

    def is_code_corpus(code: str) -> bool:
        return True

    def ask_user(token_to_verify: str) -> str:
        return 
    

    class ChangedToken:
            def __init__(self, token: str):
                 self.original = token
                 self.changed
                 self.type
                 self.startpoint
                 self.endpoint
