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

    @abstractmethod
    def untokenize_tokens(token_list: list)-> str:
        return 
    
    @abstractmethod
    def get_answer_from_user(token: str) -> str:
        response = 'hlo'
        return response


class Translator(Abs_Translator):
    def __init__(self, code, lang):
        self
        self.translate_code(code)
    
    '''
    Handle the event when map_name_token() function cant find the right map in language pack
    '''
    def translate_code(self, code: str, lang: str) -> str:
        tokens = self.tokenize_code(code)
        '''
        Handle tokens.lang bcoz its directly asking tokens [list] 
        '''
        token_list = tokens.copy()
        if(self.is_eng(tokens.lang)):
            if(self.is_code_corpus(tokens)):
                return code
            else:
                for i,token in enumerate(tokens):
                    # Handle the logic for unidentified english keywords
                    if(token.type != 'KeyWord'):
                        pred = self.guess_token(token)
                        response = self.ask_user(pred, predicted=True)
                        token_list.replace(i, response)

        else:
            lang_pack = self.get_dict(lang)
            for i,token in enumerate(tokens):
                if(token.type == 'NAME'):
                    response = self.map_name_token(token, lang_pack)
                    token_list.replace(i,response)

        latest_code = self.untokenize_tokens(token_list)
        return latest_code
    

    def get_dict(lang: str)-> dict:
        lang_pack = "hlo"
        return lang_pack
    
    def untokenize_tokens(token_list: list)-> str:
        code = 'hlo'
        return code

    def tokenize_code(code: str) -> list:
        tokens= ['hlo']
        return tokens

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

    def is_code_corpus(code: str) -> bool:
        return True
    
    def get_answer_from_user(token: str) -> str:
        response = 'hlo'
        return response
    

    '''
    Handle predicted case
    '''

    def ask_user(self, token_to_verify: str, prediction: bool = False) -> str:
        if(prediction):
            user_reply = True
            if(user_reply):
                return token_to_verify
            else:
                response = self.ask_user(token_to_verify)
                return response
        else:
            self.throw_error()
            user_response = self.get_answer_from_user(token_to_verify) 
        return user_response

    class ChangedToken:
            def __init__(self, token: str):
                 self.original = token
                 self.changed
                 self.type
                 self.startpoint
                 self.endpoint
